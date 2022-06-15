from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_index():
    return "<p> This is a fine piece of html </p>"


@app.route("/hello")
def get_hello():
    return "<p> HELLO </p>"
