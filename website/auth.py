from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters." ,category='error')

        elif len(firstName) < 2:
            flash("Name should consist of more than 2 characters." ,category='error')

        elif password1 != password2:
            flash("The passwords doesn't match.",category='error')

        elif len(password1) < 7:
            flash("The length of the password should be greater than 7 characters.",category='error')
        else:
            # add user to the  database
            flash("Account Created.",category='success')

    return render_template("signup.html")