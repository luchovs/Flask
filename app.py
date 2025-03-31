from flask import Flask

app = Flask(__name__)

@app.route("hello world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("hola mundo")
def hola_mundo():
    return "<p>hola mundo</p>"