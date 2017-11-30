from flask import Flask, request, redirect, render_template
import cgi
import os
import re
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html', title = "Sign Up")

@app.route("/signup", methods=['POST'])
def signup():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

# Validate Username
    if username == "": 
        username_error = "Username field cannot be empty"
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
        username = ""
    elif " " in username:
        username_error = "Your username cannot contain any spaces"
        username = ""

# Validate Password
    if password == "": 
        password_error = "Password field cannot be empty"
    elif len(password) <= 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
    elif " " in password:
        password_error = "Your password cannot contain any spaces"    

#verify password
    if verify == "" or verify != password: 
        verify_error = "Passwords do not match"
        verify = ''

#Validate Email  
    if email != "": 
        # Used regex for complete email validation.
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                email_error = "Not a valid email address."

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template(
            'form.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_error = verify_error,
            email = email,
            email_error = email_error
            )
    
app.run()