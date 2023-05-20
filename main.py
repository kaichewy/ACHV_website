from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/alevel")
def alevel():
    return render_template('a.html')


@app.route("/olevel")
def olevel():
    return render_template('olevel.html')


if __name__ == "__main__":
    app.run(debug=True)
