# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

#generate URLs for static files
url_for('static', filename='style.css')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
