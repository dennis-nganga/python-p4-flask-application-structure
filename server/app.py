#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
    return  f'<h1> this is the first line of Flask</h1>'

@app.route('/<username>')
def user(Username):
    return f'<h1>heres my username{Username}</h1>'

app.run(debug=True)

