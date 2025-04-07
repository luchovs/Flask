from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def main():
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/logo.png")

    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar_dados</a>
    """

@app.route("/saludar/hola")
def hello():
    return """
    <p>Hola</p>
    <br>
    <a href="saludar/chau">Chau</a>
    <br>
    <a href="chau">Chau 2</a>
    """

@app.route("/saludar/chau")
def bye():
    return "<p>Chau</p>"

@app.route("/saludar/por-nombre/<string:nombre>")
def sxn(nombre):
    return "<p>Chau</p>"

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