import os
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('berlin_airbnb2.html')

if __name__ == '__main__':
    app.run(port=4500, debug=True)
