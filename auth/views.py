from flask import render_template,redirect,url_for, flash,request
from . import auth
from ..models import User
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,RegistrationForm
from ..email import mail_message


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    

    title = "Rental login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data,profile_pic_path= 'photos/unknown.png')
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to My Rental","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',registration_form = form,title=title)    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))