from www.model import init_db
from wsgi import app

if __name__ == "__main__":
    app.run(debug=True)
    init_db()

