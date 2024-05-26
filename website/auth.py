from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import *
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # checking whether the email exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in Successfully !!' ,category="success")
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password Try Again!',category='error')

        else:
            flash('User Doesnot Exists , Please Sign Up first',category="error")
    return render_template("login.html",user=current_user)

@auth.route("/logout")
@login_required #this makes sure that this route can only be accessed after login only
def logout():
    logout_user()
    flash("You are Logged Out!",category='success')
    return redirect(url_for("auth.login"))

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already Exists.",category="error")

        elif len(email) < 4:
            flash("Email must be greater than 4 characters." ,category='error')

        elif len(firstName) < 2:
            flash("Name should consist of more than 2 characters." ,category='error')

        elif password1 != password2:
            flash("The passwords doesn't match.",category='error')

        elif len(password1) < 7:
            flash("The length of the password should be greater than 7 characters.",category='error')
        else:
            # add user to the  database
            new_user = User(email=email,first_name=firstName,password=generate_password_hash(password1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(user,remember=True)
            flash("Account Created.",category='success')
            return redirect(url_for('views.home')) #blueprint name.function name ex : views.home
            # return redirect('/') this will also work

    return render_template("signup.html",user=current_user)