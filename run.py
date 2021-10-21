from flask import Flask

from www.app import app
from www.model import init_db

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
    init_db()

