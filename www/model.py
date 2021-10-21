from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum


# Create database connection object
from .app import app
db = SQLAlchemy(app)


class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

    def save(self):
        db.session.add(self)
        db.session.commit()


def init_db():
    try:
        db.create_all()
        db.session.commit()
    except Exception as e:
        pass
    finally:
        lg.warning('Database initialized!')
