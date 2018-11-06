# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
