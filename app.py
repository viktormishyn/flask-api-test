from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from config import TestingConfig

app = Flask(__name__)
app.config.from_object(TestingConfig)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from Planetary API!!'), 200


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f"Sorry, {name}, you are not old enough."), 401
    else:
        return jsonify(message=f"Welcome, {name}, you are old enough!")


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message=f"Sorry, {name}, you are not old enough."), 401
    else:
        return jsonify(message=f"Welcome, {name}, you are old enough!")


if __name__ == '__main__':
    app.run()
