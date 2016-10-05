#Edmond Lam
#SoftDev1 pd8
#HW04 -- Big, Heavy, Wood
#2016-10-02

from flask import Flask, render_template, request
import hashlib
import utils.authenticate

app = Flask(__name__)
#creates instance of Flask and passes env variable __name__



@app.route("/")
def mainpage():
    return render_template("triform.html", TAB="Login Page!", TITLE = "LOGIN HERE!")


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
            return render_template("triform.html", TITLE = "Success!", alert = " You have successfully logged in!")
        return render_template("triform.html", TITLE = "Sign in Unsuccessful.", alert = " You have entered an erroneous password or user does not exist!")
    return render_template("triform.html", TITLE = "Sign in Unsuccessful", alert = "Account does not exist. Please try again.")

@app.route("/register", methods=['POST'])
def register():
    print request.form
    user = request.form["user"]
    pin = request.form["pass"]
    shaHash = hashlib.sha1()
    shaHash.update(pin)
    passHash = shaHash.hexdigest()
    userslist = utils.authenticate.getUsers()
    if (user in userslist):
        return render_template("triform.html", alert="Username already exists! Please change your username or login to the account you have created already.")
    utils.authenticate.addUser(user,passHash)
    return render_template("triform.html", alert="Account created. Login.")
    
if __name__ == "__main__":
    app.debug = True
    app.run()
