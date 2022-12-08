from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User

@app.route('/')
def user_new():
    return render_template('index.html')

@app.route('/user/create', methods=['POST'])
def user_create():
    if User.validate_user(request.form) == False:
        return redirect('/')
    existing_user = User.get_user_verify_email(request.form)
    if existing_user != None:
        flash('Email already exists')
        return redirect('/')
    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)

    user_id = User.create(data)

    session['username'] = data['username']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect('/home')

@app.route('/login', methods=['POST'])
def verify_login():
    active_user = User.get_user_verify_email(request.form)
    if active_user != None:
        if not bcrypt.check_password_hash(active_user.password,request.form['password']):
            flash('Invalid login credentials')
            return redirect('/')
        session['username'] = active_user.username
        session['email'] = active_user.email
        session['user_id'] = active_user.id

        return redirect ('/home')
    else:
        flash('Invalid login credentials')
        return redirect ('/')

@app.route('/home')
def home_page():
    return render_template('dashboard.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/user/logout')
def process_logout():
    session.clear()
    return redirect('/')

# @app.route('/user/<int:id>')
# def user_show(id):
#     return render_template('user_show.html')

# @app.route('/user/<int:id>/edit')
# def user_edit(id):
#     return render_template('user_edit.html')

# @app.route('/user/<int:id>/update', methods=['POST'])
# def user_update(id):
#     return redirect('/')

# @app.route('/user/<int:id>/delete')
# def user_update(id):
#     return redirect('/')

# table_name/<int:id>/action -- RESTFUL ROUTING ARCHITECTURE