from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
#from flask_app.models.user import User  

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

