from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from authentication import auth as auth_blueprint
from models import db, User
from config import Config
import rest

#Creating app object, changing configurations and registering the blueprint
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
db.init_app(app)
api = Api(app)

# LoginManager is the most important part of flask-login which will be used for user login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()     # creating the database tables with approriate fields

api.add_resource(rest.TodoList, '/todo')
api.add_resource(rest.Todo, '/todo/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


