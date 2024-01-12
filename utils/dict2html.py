def generate_html_from_dict(element_dict):
    """
    Generates an HTML string based on the provided element dictionary.

    Parameters:
    - element_dict (dict): A dictionary representing an HTML element with keys such as 'tag', 'attributes', 'style',
      'content', 'self_closing', and 'children'.

    Raises:
    - ValueError: If the 'tag' key is missing in the element dictionary.
                 If a self-closing element has a 'content' attribute.

    Returns:
    - str: The HTML string generated from the input element dictionary.
    """
    if "tag" not in element_dict:
        raise ValueError("Missing 'tag' key in the element dictionary.")

    html_string = f"<{element_dict['tag']}"

    # Add attributes
    if "attributes" in element_dict:
        for attribute, value in element_dict["attributes"].items():
            html_string += f' {attribute}="{value}"'

    # Add style attribute
    if "style" in element_dict:
        style_string = "; ".join([f"{key.replace('_', '-')}:{value}" for key, value in element_dict["style"].items()])
        html_string += f' style="{style_string}"'

    # Add content or data
    if "content" in element_dict:
        if element_dict.get("self_closing", False):
            raise ValueError("Self-closing element cannot have 'content' attribute.")
        html_string += f">{element_dict['content']}"
    else:
        if element_dict.get("self_closing", False):
            html_string += " />"
        else:
            html_string += ">"

    # Handle nested elements
    if "children" in element_dict and isinstance(element_dict["children"], list):
        for child_element in element_dict["children"]:
            html_string += generate_html_from_dict(child_element)

    if "content" not in element_dict or not element_dict.get("self_closing", False):
        html_string += f"</{element_dict['tag']}>"

    return html_string

"""
example_element = {
    "tag": "div",
    "attributes": {"class": "container", "id": "main-container"},
    "style": {"color": "blue", "font-size": "16px"},
    "content": "Hello, <b>world</b>!",
    "children": [
        {"tag": "p", "content": "This is a paragraph."},
        {"tag": "a", "attributes": {"href": "https://example.com"}, "content": "Visit Example"},
    ]
}

generated_html = generate_html_from_dict(example_element)
print(generated_html)
"""