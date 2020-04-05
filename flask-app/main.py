import unittest
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user
from app import create_app
from app.forms import LoginForm, TodoForm, DeleteTodoForm
from app.firestore_service import get_users, get_todos, put_todo, delete_todo

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


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        flash('Tu tarea se creo con éxito')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))