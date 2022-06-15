from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def get_index():
    return "<p> This is a fine piece of html </p>"


@app.route("/hello")
def get_hello():
    return render_template('hello.html', name="david")
