from flask import Flask
from simple_recommender import get_recommendations

app = Flask(__name__)


@app.route("/")
def hello_sumacs():
    return """
    <h1>Good Morning Sumacs!</h1>
    <p>This is a line <br> going throught 2 lines</p>
    <a href="https://www.imdb.com">IMDB</a>
    <br>
    <a href="/recommendations">Get Recommendations</a>
    """


@app.route("/recommendations")
def recommender():

    top3=get_recommendations()

    return f"""
    <ul>
    <li>{top3[0]}</li>
    <li>{top3[1]}</li>
    <li>{top3[2]}</li>
    </ul>"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)
