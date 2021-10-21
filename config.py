import os


# Database initialization
if os.environ.get('DATABASE_URL') is None:
    raise Exception
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
