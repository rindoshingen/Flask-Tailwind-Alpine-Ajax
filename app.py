from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

articles = [
    {
        "id": 1,
        "title": "Article One",
        "description": "This is the content for article one.",
        "by": "Michael",
    },
    {
        "id": 2,
        "title": "Article Two",
        "description": "This is the content for article two.",
        "by": "Bodhi",
    },
    {
        "id": 3,
        "title": "Article Three",
        "description": "This is the content for article three.",
        "by": "Shingen",
    },
    {
        "id": 4,
        "title": "Article Four",
        "description": "This is the content for article four.",
        "by": "Charlie",
    },
]


@app.context_processor
def inject_current_year():
    current_year = datetime.now().year
    return dict(current_year=current_year, company_name="Flask App")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/interest")
def interest():
    return render_template("interest.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
