from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user
from flask_login.utils import login_required, logout_user
from .models import User
from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('Create.html')


@auth.route('/signup/post', methods=['POST'])
def signup_post():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user:
        flash('Username already exists')
        return redirect('/signup')

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/login')


@auth.route('/login', methods=['GET','POST'])
def login_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()


        if not user or not user.verify_password(password):
            flash('Please check your login details and try again.')
            return redirect('/login')
        
        login_user(user)
        return redirect(url_for('main.dashboard'))



        


    else:
        return render_template('Login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')