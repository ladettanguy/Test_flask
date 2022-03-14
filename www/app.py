from www import app
from flask import render_template, request
import json


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        request.make_form_data_parser()
        if request.is_json:
            data = request.data
            my_json = json.loads(data)
            return str(my_json)
            return 'Post Hello World !'
    else:
        return 'Get Hello World !'


@app.route('/index', methods=['POST', 'GET'])
@app.route('/index/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
