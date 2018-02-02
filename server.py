from flask import Flask, render_template


app = Flask(__name__)

app.secret_key = "ABC"


@app.route('/')
def index():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')