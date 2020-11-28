from flask import request, jsonify
import numpy as np

from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def hello_world():
    if request.method=='GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    if index < 0 or index > len(list):
        response = np.random.randn()
        return jsonify(response)
    return list[index]
