from flask import render_template,redirect,url_for, flash,request
from . import auth
from ..models import User
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,RegistrationForm
from ..email import mail_message


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()

     title = "New Account"
    return render_template('auth/register.html',registration_form = form,title=title) 