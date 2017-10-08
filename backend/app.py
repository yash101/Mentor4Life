import sqlite3
import os
import sys
from flask import g
from flask import Flask

app = Flask(__name__)

database_path = "../database.sqlite3.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database_path)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close() 

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
