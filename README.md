# :coffee:Task-with-Python-Flask

## Python - Flask - Docs
See info what do you need for this project
* [See docs project](Docs/README.md)
* Python 3
* Flask
* Bootstrap 4

## How to run project

Inside **flask-app folder**

Create a virtual enviroment
`python -m venv env`

Python and Flask
`pip install -r requirements.txt`

Verify
`pip freeze`

On Linux
> Create variable
> `export FLASK_APP=main.py`
>
> Verify variable
> `echo $FLASK_APP`

On Windows
> Create a varible
> `set FLASK_APP=main.py`

Run development server
`flask run` or `python -m flask run`

Enable debug if needs
> `export FLASK_DEBUG=1`

<div align="center">
  <img src="images/Screenshot_1.png">
  <small><p>Run App</p></small>
</div>

## Preview
<div align="center">
  <img src="images/Screenshot_2.png">
  <small><p>Login app</p></small>
</div>

<div align="center">
  <img src="images/Screenshot_3.png">
  <small><p>Task App</p></small>
</div>

## Deploy and Connect to GCloud DataStore and AppEngine
### Requirements

* Install Google Cloud SDK https://cloud.google.com/sdk/docs/quickstarts
* Create a Project
* Active FireStore mode DataStore

Next execute next command:

Initialize

`gcloud init`

Login

`gcloud auth login`

Configure

`gcloud config set project PROJECT_ID`

Default authentication in app

`gcloud auth application-default login`

Verify

`gcloud config list`

Deploy
`gcloud app deploy app.yaml`

`gcloud app browse`

#### FireStore
<div align="center">
  <img src="images/FireStore.png">
  <small><p>FireStore</p></small>
</div>


