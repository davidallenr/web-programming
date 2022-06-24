import json
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, make_response
from flask import session
import json

app = Flask(__name__)
app.secret_key = "ksmdflkji240[i2hjfsklnf"


@app.route("/")
@app.route("/home")
def get_index():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('get_login'))
    return render_template('home.html', name=username)


@app.route("/other")
def get_other():
    if 'username' in session:
        username = session['username']
    else:
        return redirect(url_for('get_login'))
    return render_template('other.html', name=username)


@app.route("/login", methods=['GET'])
def get_login():
    if 'username' in session:
        return redirect(url_for('get_index'))
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", None)
    if username == None:
        return redirect(url_for('get_login'))

    try:
        with open(f"storage/{username}.json", "r") as f:
            creds = json.load(f)
    except Exception as e:
        print(f"Error in reading creds. {e}")
        return redirect(url_for('get_login'))

    password = request.form.get("password", None)

    if password != creds['password']:
        print('Bad password')
        return redirect(url_for('get_login'))
    else:
        session['username'] = username
        return redirect(url_for('get_index'))


@app.route("/register", methods=['GET'])
def get_register():
    if 'username' not in session:
        return render_template('register.html')


@app.route("/register", methods=['POST'])
def post_register():
    username = request.form.get("username", None)
    if username == None:
        return redirect(url_for('get_register'))
    # for c in username.lower():
    #     if not ((c in range('a', 'z')) or (c in range('0', '9'))):
    #         print("Illegal character in username")
    #         return redirect(url_for('get_register'))
    password = request.form.get("password", None)
    if password == None:
        return redirect(url_for('register'))
    # if len(password) < 8:
    #     print("Password not long enough")
    #     return redirect(url_for('get_register'))

    password2 = request.form.get("password2", None)

    if password2 == None:
        return redirect(url_for('get_register'))
    if password2 != password:
        print("Password not matching")
        return redirect(url_for('get_register'))
    try:
        with open(f"storage/{username}.json", "r") as f:
            creds = json.load(f)
            print("user already exists")
            return redirect(url_for('get_register'))
    except Exception:
        pass

    creds = {
        "username": username,
        "password": password
    }

    with open(f"storage/{username}.json", "w") as f:
        json.dump(creds, f)

    session['username'] = username
    return redirect(url_for('get_index'))


@ app.route("/logout", methods=['GET'])
def get_logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('get_login'))
