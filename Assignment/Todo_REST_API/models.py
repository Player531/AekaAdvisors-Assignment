from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# UserMixin is a class that provides implementation of is_authenticated(), is_active, is_anonymous(), get_id() which are necessary properties for flas-login 
# Creating a user model with id, email and password

class User(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Creating a Todo class where will store the below properties in our database
# Using foregin key here helps us establish a relationship between User table and Todo Table where Todo is associated with each user
class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    task_desc = db.Column(db.String(250), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
