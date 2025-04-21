from flask import Flask, url_for, render_template
import sqlite3

app = Flask(__name__)

db = None

def dict_factory(cursor, row):
    """Arma un diccionario con los valores de la fila."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def cerrarConexion():
    global db
    db.close()
    db.row_factory = dict_factory

@app.route("/test-db")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) AS cant FROM usuarios;")
    res = cursor.fetchone
    registros = res["cant"]
    cerrarConexion()
    return f"Hay {registros} registros en la tabla usuarios"

@app.route("/crear-usuario")
def testCrear():
    nombre = "leandro"
    email = "leandro@etec.uba.ar"
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios (usuario, email) VALUES (?, ?);"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    cerrarConexion()
    return f"Registro agregado ({nombre})"

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

@app.route("/tirar-dado/<int:caras>")
def dado(caras):
    from random import randint
    n = randint(1,caras)
    return f"<p>Tire un dado de {caras} caras, salio {n}<p>"

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email, direccion, telefono FROM usuarios WHERE id = ?; ", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    direccion = None
    telefono = None
    if res != None:
        usuario=res['usuario']
        email=res['email']
        direccion=res['direccion']
        telefono=res['telefono']
    return render_template("datos.html", id=id, usuario=usuario, email=email, direccion=direccion, telefono=telefono)