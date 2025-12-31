from flask import Flask, render_template, request
from model import recommend

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def rec():
    anime = request.form["anime"]
    results = recommend(anime)
    return render_template("result.html", anime=anime, results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
