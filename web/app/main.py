from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/square/<x>')
def square(x):
    return str(float(x)**2)

