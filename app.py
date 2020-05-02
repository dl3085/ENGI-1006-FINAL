# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/youtuber")
def youtuber():
    return render_template('youtuber.html')

@app.route("/exercise")
def exercise():
    return render_template('exercise.html')

@app.route("/1006")
def eng1006():
    return "1006 homepage"
#start the server
if __name__ == "__main__":
    app.run()