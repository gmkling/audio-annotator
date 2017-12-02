from app import app
from flask import Flask, jsonify, render_template, request
#app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    #return "Hello World!"
    return render_template('index.html')

@app.route('/submit_annotation')
def submit_annotation():

	return