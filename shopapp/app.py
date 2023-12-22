from flask import render_template, request, redirect, url_for, jsonify, flash
from flask import session as login_session
from shopapp.models import User, Listing, Tag, ListingTag
from shopapp import flask_obj, db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func


@flask_obj.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@flask_obj.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not bool(db.session.execute(db.select(User).where(User.username == username)).scalar()):
        return render_template('login.html', dne_error='No account exists with this username.')
    
    if check_password_hash(db.session.execute(db.select(User.password).where(User.username == username)).scalar(), password):
        # store current user's user id for the current login session
        # we can use this later to sort by user's commonly liked tags
        # pfp storing, liked listings, etc
        login_session['id'] = db.session.execute(db.select(User.id).where(User.username == username)).scalar()
        return redirect(url_for('dashboard'))
    
    else:
        return render_template('login.html', incorrectpw_error='Incorrect password.')