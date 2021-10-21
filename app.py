from flask import Flask, render_template, request
from psycopg2 import DatabaseError, InterfaceError
from psycopg2.extensions import connection, cursor
import json

USER = ""
PWD = ""
HOST = ""
DATABASE = ""

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    request.make_form_data_parser()
    if request.is_json:
        data = request.data
        my_json = json.loads(data)
        return str(my_json)
    else:
        return 'test'+str(request.mimetype_params)


@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
