#Edmond Lam
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood
#2016-10-02

from flask import Flask, render_template, request, redirect, url_for, session
import hashlib, os, utils.authenticate

app = Flask(__name__)
#creates instance of Flask and passes env variable __name__

status = {}

status.clear()

app.secret_key = '\x1fBg\x9d\x0cLl\x12\x9aBb\xcd\x17\xb3/\xe4\xca\xf76!\xee\xf2\xc8?\x85\xdb\xd6;[\xae\xfb\xeb'

@app.route("/")
def mainpage():
    print status
    print session
    if 'action' in status:
        if status['action'] == 'start':
            return render_template("triform.html", TAB="Login Page!", TITLE = "LOGIN HERE!")
        if status['action'] == 'registered':
            return render_template("triform.html", TAB="Login Page!!", TITLE = "LOGIN HERE!", alert = "Account successfully registered. Please log in.")
        if status['action'] == 'success':
            return render_template("home.html", TITLE = "Welcome!", HEAD = "Welcome to your homepage!")
        if status['action'] == 'fail1':
            return render_template("triform.html", TITLE = "Sign in Unsuccessful.", TAB="Could not log in.", alert = " You have entered an erroneous password or user does not exist!")
        if status['action'] == 'fail2':
            return render_template("triform.html", TITLE = "Register Unsuccessful.", TAB="Could not register.", alert = "Username has been taken already!")
        if status['action'] == 'fail3':
            return render_template("triform.html", TITLE = "Register Unsuccessful.", TAB="Could not register.", alert = "Username invalid! Do not use commas or leave blank!")
        if status['action'] == 'logout':
            session.clear()
            status.clear()
            return render_template("triform.html", TITLE = "Logged out.", TAB="Login Page!", alert = "You have been logged out.")
    else:
        session.clear()
        status.clear()
        status['action']='start'
        return redirect(url_for('mainpage'))

@app.route("/jacobo")
def js():
    return redirect(url_for("mainpage"))
    

@app.route("/login", methods=['POST'])
def authenticate():
    user = request.form['username']
    pin = request.form['password']
    shaHash = hashlib.sha1()
    shaHash.update(pin)
    pinHash = shaHash.hexdigest()
    userslist = utils.authenticate.getUsers()
    print pinHash
    print userslist[user]
    if (user in userslist):
        if (userslist[user] == pinHash):
            session[user] = app.secret_key
            status['action'] = "success"
            status['username'] = user
            return redirect(url_for("mainpage"))
        status['action'] = 'fail1'
        return redirect(url_for("mainpage"))
    status['action'] = "fail1"
    return redirect(url_for("mainpage"))

@app.route("/register", methods=['POST'])
def register():
    user = request.form["user"]
    pin = request.form["pass"]
    shaHash = hashlib.sha1()
    shaHash.update(pin)
    passHash = shaHash.hexdigest()
    userslist = utils.authenticate.getUsers()
    if (user.find(',') or user == '' or pin == '') != -1:
        status['action'] = 'fail3'
        redirect(url_for("mainpage"))
    if (user in userslist):
        status['action'] = 'fail2'
        return redirect(url_for("mainpage"))
    utils.authenticate.addUser(user,passHash)
    status['action'] = 'registered'
    return redirect(url_for("mainpage"))

@app.route("/logout", methods=['POST'])
def byebye():
    session.pop(status['username'])
    status.pop('username')
    status['action'] = 'logout'
    return redirect(url_for('mainpage'))
    
if __name__ == "__main__":
    app.debug = True
    app.run()
