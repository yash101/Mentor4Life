import sqlite3
import os
from flask import g
from flask import Flask

app = Flask(__name__)

database_path = "../database.sqlite3.db"



@app.route('/')
def index():
    return "Web API is not available for use without the frontend"



@app.route('/api/v0/auth/signup', methods=['POST'])
def signup():
    
    return "Fail" # change when finised

@app.route('/api/v0/auth/login', methods=['POST'])
def login():
    
    return "Fail" # change when finished

@app.route('/api/v0/auth/signout', methods=['POST', 'GET'])
def signout():
    
    return "Fail" # change when finished

@app.route('/api/v0/nav/info', methods=['POST', 'GET'])
def navinfo():
    
    return "Fail" # change when finished

@app.route('/api/v0/dashboard/<string:requested>', methods=['POST', 'GET'])
def getDashboardFunction(requested):

    return "Fail" # change when finished

@app.route('/api/v0/headshot/<int:width>/<int:height>', methods=['GET'])
def getHeadshot(width, height):
    
    return "Fail" # change when finished

@app.route('/api/v0/headshot', methods=['POST', 'GET'])
def getUpdateHeadshot():
    
    return "Fail" # change when finished

if __name__ == '__main__':
    app.run(debug=True)