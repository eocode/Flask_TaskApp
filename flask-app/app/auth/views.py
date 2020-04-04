from flask import render_template, redirect, url_for, session, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash
from app.forms import LoginForm
from . import auth
from app.firestore_service import get_user, user_put
from app.models import UserModel, UserData

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    context = {
        'login_form': form
    }
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user_doc = get_user(username)
        if user_doc.to_dict() is not None:
            print('Hay data')
            print(user_doc)
            password_from_db = user_doc.to_dict()['password']

            if password == password_from_db:
                user_data = UserData(username,password)
                user = UserModel(user_data)

                login_user(user)
                flash('Bienvenido de nuevo')
                redirect(url_for('hello'))
            else:
                flash('La información proporcionada no coincide')
        else:
            flash('El usuario no existe')
        
        return redirect(url_for('index'))
    return render_template('login.html', **context)

@auth.route('signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    context = {
        'signup_form':form
    }

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:

            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)
            login_user(user)
            
            flash('Bienvenido')
            return redirect(url_for('hello'))
        else:
            flash('El usuario ya existe')

    return render_template('signup.html', **context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect('/')