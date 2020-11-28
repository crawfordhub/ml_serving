from flask import request, jsonify, render_template
from forms import IndexForm
import numpy as np

from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    return render_template('index.html', form=form)

def run_request():
    index = int(request.json['index'])
    list = ['red', 'green', 'blue', 'yellow', 'black']
    if index < 0 or index > len(list):
        response = np.random.randn()
        return jsonify(response)
    return list[index]
