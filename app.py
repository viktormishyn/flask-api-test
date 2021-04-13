from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from Planetary API!!'), 200


if __name__ == '__main__':
    app.run()
