from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Realizar challenge']


@app.cli.command("test")
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)
     

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET','POST'])
def hello():
    user_ip = session.get('user_ip')
    form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': form,
        'username': username
    }

    if form.validate_on_submit():
        username = form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)
