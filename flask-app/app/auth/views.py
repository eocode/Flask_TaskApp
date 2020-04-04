from flask import render_template, redirect, url_for, session, flash
from app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    context = {
        'login_form': form
    }
    if form.validate_on_submit():
        username = form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con éxito')
        
        return redirect(url_for('index'))
    return render_template('login.html', **context)