from flask import Flask, request, jsonify

app = Flask(__name__)

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    return list[index]

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='GET':
        return 'The model is up and running. Send a POST request'
    else:
        return run_request()
