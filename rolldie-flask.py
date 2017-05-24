from flask import Flask, jsonify
app = Flask(__name__)

import json
import random

def roll(numrolls = 1):
    """
    Sum of the rolls
    """
    return sum(random.randint(1,6) for i in range(numrolls))

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/rolldice')
def rolldice():
    """
    Return a json object
    """
    return jsonify ({'value': roll(numrolls=1), 'rolls': 2})

if __name__ == '__main__':
 app.debug = True
 app.run()
