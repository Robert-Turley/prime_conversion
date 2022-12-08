from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.number import Number


@app.route('/number/create', methods=['POST'])
def number_create():
    if Number.validate_number(request.form) == False:
        return redirect('/')

    return redirect('/home') #How to render table on same page using JS?

