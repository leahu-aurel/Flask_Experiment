from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_blog import db, bcrypt
from flask_blog.users.forms import (ResetPasswordForm, RequestResetForm,
                                    RegistrationForm, UpdateAccountForm, LoginForm)
from flask_blog.models import User, Post

bp = Blueprint('users', __name__)


bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', title='Register', form=form)