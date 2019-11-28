import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from entrysystem import app, db, bcrypt, mail
from entrysystem.forms import LoginForm
from entrysystem.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from datetime import datetime, timedelta
from pytz import timezone
import pytz

uname = ''
umail = ''
uphone = ''
check_in = ''

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    global uname
    uname  = form.username.data
    global umail
    umail = form.email.data
    global uphone
    uphone = form.password.data

    if form.validate_on_submit():
        user = User.query.filter_by(email='kakaricardo771@gmail.com').first()
        
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        send_reset_email(user, uname, umail, uphone)
        flash('Thanks for Checking In!', 'info')
        return redirect(next_page) if next_page else redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/logout")
def logout():
    
    user = User.query.filter_by(email='kakaricardo771@gmail.com').first()
    logout_user()
    send_logout_email(user, uname, umail, uphone)
    flash('Successfully Checked Out!', 'info')
    return redirect(url_for('home'))

    return render_template('home.html', title='Home', form=form)
    return redirect(url_for('home'))


def send_reset_email(user, uname, umail, uphone):
    
    
    now = datetime.now()
    timezone = pytz.timezone("Asia/Kolkata")
    d_aware = timezone.localize(now)
    d_aware.tzinfo

    current_time = now.strftime("%H:%M:%S")
    global check_in
    check_in = current_time
    token = user.get_reset_token()
    msg = Message('Checked In', 
                    sender='odinson947@gmail.com', 
                    recipients=[user.email])
    form = LoginForm()

    msg.html = "<h1>NAME:</h1>"+uname+"<h1>EMAIL:</h1>"+umail+"<h1>PHONE NUMBER:</h1>"+uphone+"<h1>CHECK-IN TIME:</h1>"+current_time

    mail.send(msg)

def send_logout_email(user, uname, umail, uphone):
    
    now = datetime.now()
    timezone = pytz.timezone("Asia/Kolkata")
    d_aware = timezone.localize(now)
    d_aware.tzinfo
    current_time = now.strftime("%H:%M:%S")
    
    token = user.get_reset_token()
    msg = Message('Checked Out', 
                    sender='odinson947@gmail.com', 
                    recipients=[umail])
    form = LoginForm()

    msg.html = "<h1>NAME:</h1>"+uname+"<h1>EMAIL:</h1>"+umail+"<h1>PHONE NUMBER:</h1>"+uphone+"<h1>CHECK-IN TIME:</h1>"+check_in+"<h1>CHECK-OUT TIME:</h1>"+current_time+"<h1>HOST NAME:</h1>"+'Mr. Host'+"<h1>ADDRESS:</h1>"+'Innovaccer Offices, Noida.'

    mail.send(msg)




















