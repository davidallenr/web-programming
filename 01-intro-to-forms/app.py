from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def get_index():
    return "<p> This is a fine piece of html </p>"


@app.route("/hello")
def get_hello(name="Default"):
    return render_template('hello.html', name=name)


@app.route("/login", methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", "<missing name>")
    password = request.form.get("password", "<missing password>")
    if password == "password1":
        return redirect(url_for('get_hello', name=username))
    else:
        return redirect(url_for('get_login'))
