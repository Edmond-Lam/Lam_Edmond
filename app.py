from flask import Flask, render_template
import Divine
#python can be object oriented

app = Flask(__name__)
#creates instance of Flask and passes env variable __name__


prob = Divine.calc()

print prob

@app.route("/")
def mainpage():
    return '''<html>
              <head>
              <title>Edmond's Homepage</title>
              </head>
              <body>
              <a href="http://127.0.0.1:5000/Grovyle!">Grovyle!</a><br>
              <a href="http://127.0.0.1:5000/occupations">Occupations</a><br>
              </body>
              </html> '''

@app.route("/Grovyle!")
def grovyle():
    return Divine.calc() + '''<html>
              <head>
              <title>Grovyle!!!</title>
              </head>
              <body>
              <font size=20px color:green><b>Grov Grovyle!</b></font><br>
              <a href="http://127.0.0.1:5000/">back</a>
              </body>
              </html> '''

@app.route("/occupations")

def test_tmplt():
    return render_template("basic.html", GROVYLE = "Job Occupations", fool = prob, SCEPTILE = Divine.randOcc(Divine.calc()))
            

if __name__ == "__main__":
    app.debug = True
    app.run()
