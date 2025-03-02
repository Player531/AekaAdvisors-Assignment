from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from models import db, User

# Creating a blue print for authentication
auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST']) # /auth/signup will be the route
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'Email already exists'}), 409 #conflict because the user already exists
    new_user = User(email=email, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message':'User created Successfully'}), 201 #request successful and new resource was created

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Login Failed. Check your email and password'}), 401 #authentication to server failed
    login_user(user)
    return jsonify({'message': "Logged in Successfully"}), 200 #request was successful to the server

@auth.route('/logout')
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200
