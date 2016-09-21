from flask import Flask
#python can be object oriented

app = Flask(__name__)
#creates instance of Flask and passes env variable __name__

@app.route("/")
def hello_world():
    return '''<html>
              <head>
              <title>Grovyle!!!</title>
              </head>
              <body>
              <a href="http://127.0.0.1:5000/Grovyle!">Grovyle!</a><br>
              <a href="http://127.0.0.1:5000/car">Car</a><br>
              </body>
              </html> '''

@app.route("/Grovyle!")
def hello_world2():
    return '''<html>
              <head>
              <title>Grovyle!!!</title>
              </head>
              <body>
              <font size=20px color:green><b>Grov Grovyle!</b></font><br>
              <a href="http://127.0.0.1:5000/">back</a>
              </body>
              </html> '''
@app.route("/car")
def hello_world3():
    return  '''<html>
              <head>
              <title>Great News!</title>
              </head>
              <body>
              <font size=20px><b>Great News! - James May</b></font><br>
              <img src="http://127.0.0.1:5000/Sandero.jpeg" alt="Great News! - James May">
              <a href="http://127.0.0.1:5000/">back</a>
              </body>
              </html> '''
if(__name__ == "__main__"):
    app.run()
