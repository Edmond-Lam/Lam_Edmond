from flask import Flask, render_template, request

app = Flask(__name__)
#creates instance of Flask and passes env variable __name__




@app.route("/")
def mainpage():
    print "\n\n\n"
    print ":::DIAG::: this Flask obj"
    print app
    print ":::DIAG::: this request obj"
    print request
    print ":::DIAG::: this request.headers"
    print request.headers
    print ":::DIAG::: this request.method"
    print request.method 
    print ":::DIAG::: this request.args"
    print request.args
    print ":::DIAG::: this request.args['username']"
    # print request.args['username']
    print ":::DIAG::: this request.form"
    print request.form
    return render_template("triform.html", VARIABLE="Test Form!", TITLE = "LOGIN HERE!")

@app.route("/auth", methods=['POST','GET'])
def authenticate():
    user = "GROVYLE"
    pin = "dex253"
    if request.form['username'] != user:
        return render_template("loginstatus.html", TITLE = "Sign in Unsuccessful", SCEPTILE = "Username is erroneous or does not exist.")
    elif request.form['password'] != pin:
        return render_template("loginstatus.html", TITLE = "Sign in Unsuccessful", SCEPTILE = "Username or password is erroneous or user does not exist.")
    return request.form['username'] + "\n" + request.form['password']
    
if __name__ == "__main__":
    app.debug = True
    app.run()
