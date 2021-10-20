from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    if request.is_json:
        data = request.data
        my_json = json.loads(data)
        return str(my_json)
    elif request.is


if __name__ == '__main__':
    app.run()
