# Python - Flask <!-- omit in toc -->

<div align="center">
  <img src="images/flask.png">
  <small><p>Flask Logo</p></small>
</div>

- [Fundamentos](#fundamentos)
  - [Aplicaciones web](#aplicaciones-web)
    - [Ventajas](#ventajas)
  - [¿Qué es Flask?](#%c2%bfqu%c3%a9-es-flask)
  - [Request y Response](#request-y-response)
- [Templates](#templates)
  - [Hot reload](#hot-reload)
- [Extensiones](#extensiones)
  - [Flask-Bootstrap](#flask-bootstrap)
  - [Desarrollo](#desarrollo)
- [Códigos de estado HTTP](#c%c3%b3digos-de-estado-http)
- [Protección CSRF](#protecci%c3%b3n-csrf)
- [Bases de datoy y App Engine con Flask](#bases-de-datoy-y-app-engine-con-flask)
  - [Bases de datos SQL](#bases-de-datos-sql)
  - [Bases de datos NoSQL](#bases-de-datos-nosql)
    - [DataStore](#datastore)

# Fundamentos

## Aplicaciones web
Flask permite procesar un aplicación web en una red de servidores. Estos servidores unen su poder de procesamiento con el fin de transmitir solicitudes a todo el mundo.

El servidor procesa la información obtenida por el navegador, luego realiza procedimientos de acuerdo a la lógica de negocio para que está sea enviada de regreso al cliente que la solicito.

### Ventajas
* Muchas de las aplicaciones web que existen son gratuitas
* Puedes acceder a tu información en cualquier momento y lugar
* No dependes de un dispositivo específico ya que la aplicación se encuentra almacenada en la web

## ¿Qué es Flask?
Es un microframework, su estructura fundamental es simple y personalizable
* No tiene un sistema de autenticación o base de datos específica
* Se puede extender con los flask extensions
* Flask sirve para hacer una cosa de forma simple
* Templete engine JinJa2
* Flask no tiene una arquitectura
* Flask no tiene un ORM

## Request y Response
El browser hace un petición y el servidor envia una respuesta

```python
from flask import Flask, request, make_response, redirect
app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello World Flask {user_ip}'
```

# Templates
JinJa 2
https://jinja.palletsprojects.com/en/2.11.x/

Expandir un diccionario con **variables

## Hot reload

Para aplicar los cambios sin que afecte el cache teclear en Chrome:
> CTRL + SHIFT + R

# Extensiones

Flask permite extender sus capacidades con extenciones

## Flask-Bootstrap

https://pythonhosted.org/Flask-Bootstrap/

<div align="center">
  <img src="images/bootstrap.png">
  <small><p>Bootstrap</p></small>
</div>

## Desarrollo

**Blueprints:** Son una serie de rutas que podemos integrar en nuestra aplicación, pero desde otro directorio, es decir, permite modular la aplicación en pequeñas aplicaciones que hagan cosas específicas, como autenticación o el welcome.
* Se crea un blueprint para tareas específicas y es más fácil de manejar

# Códigos de estado HTTP

Códigos de estado

<div align="center">
  <img src="images/codes.gif">
  <small><p>Flask Logo</p></small>
</div>

# Protección CSRF

El CSRF (del inglés Cross-site request forgery o falsificación de petición en sitios cruzados) es un tipo de exploit malicioso de un sitio web en el que comandos no autorizados son transmitidos por un usuario en el cual el sitio web confía.

<div align="center">
  <img src="images/csrf.png">
  <small><p>Flask Logo</p></small>
</div>

# Bases de datoy y App Engine con Flask

## Bases de datos SQL
Se compone de bases de datos con tablas y filas que contiene campos estructurados. No es muy flexible y mientras más compleja sea la base de datos más procesamiento necesitará

* ORM Flask SQL Alchemy
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/

## Bases de datos NoSQL
Su composición es abierta, no estructurada, flexible a diferentes tipos de datos y no necesita demasiados recursos para ejecutarse, no necesitan una tabla fija como las BD relacionales y es altamente escalable a un bajo costo

<div align="center">
  <img src="images/datastore.png">
  <small><p>DataStore Comparación</p></small>
</div>


### DataStore
https://cloud.google.com/sdk