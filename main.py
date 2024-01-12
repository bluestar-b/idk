from flask import Flask, render_template_string
from utils.dict2html import generate_html_from_dict
app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string(generate_html_from_dict(({
        "tag": "body",
        "attributes": {"class": "container"},
        "style": {"background-color": "black"},

    })))


if __name__ == "__main__":
    app.run(debug=True)
