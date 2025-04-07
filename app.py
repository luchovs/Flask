from flask import Flask

app = Flask(__name__)

@app.route("/hello world")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hola mundo")
def hola_mundo():
    return "<p>hola mundo</p>"

@app.rout("/tirar-dado/<int:caras>")
def caras():
    from random import randint
    n = randint(1,caras)
    return f"<p>Tire un dado de {caras} caras, salio {n}<p>"