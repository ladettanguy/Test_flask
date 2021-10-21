from www.app import app
from www.model import init_db

if __name__ == "__main__":
    app.run(debug=True)
    init_db()

