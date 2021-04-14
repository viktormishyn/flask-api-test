import os

basedir = os.path.abspath(os.path.dirname(__file__))


class TestingConfig(object):
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY') or '-very-very-SECRET-KEY-'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tests/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '-very-very-SECRET-KEY-'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://user:password@localhost:33060/departments_app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
