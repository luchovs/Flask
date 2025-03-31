# Flask

## Entorno Virtual

Para crear el entorno virtual:

```
python -m venv .venv
```
Para activar el entorno virtual:

```
source .venv/bin/activate
```
Para instalar la dependencias:

```
pip install flask
```

## Para correr el programa

Para acceder sólo desde la máquina local:
```
flask run
```

Para acceder desde cualquier máquina de la red:
```
flask run -h 0.0.0.0
```