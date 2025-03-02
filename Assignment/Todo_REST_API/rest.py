from flask import request
from flask_restful import Resource
from flask_login import login_required, current_user
from models import TodoModel, db

class TodoList(Resource):
    @login_required
    def get(self):      #GET gets all the todos that exist for the logged in user
        todo_list = TodoModel.query.filter_by(user_id=current_user.id).all()
        return [{'id': todo.id, 'title': todo.title, 'task_desc': todo.task_desc, 'complete': todo.complete} for todo in todo_list], 200 #request was successful to the server
    
    @login_required
    def post(self):     #POST Creats a new Task for the logged in user
        data = request.get_json()
        new_todo = TodoModel(
            title = data.get('title'),
            task_desc = data.get('task_desc'),
            complete = False,
            user_id = current_user.id
        )
        db.session.add(new_todo)
        db.session.commit()
        return 'Task added Successfully', 200

class Todo(Resource):  
    @login_required
    def get(self, todo_id):     #GET shows the task related to that todo_id
        todo = TodoModel.query.filter_by(id=todo_id, user_id=current_user.id).first_or_404()
        return {'id': todo.id, 'title': todo.title, 'task_desc': todo.task_desc, 'complete': todo.complete}, 200
    
    @login_required
    def put(self, todo_id):     #PUT updates the an existing task for the logged in user
        data = request.get_json()
        todo = TodoModel.query.filter_by(id=todo_id, user_id=current_user.id).first_or_404()
        todo.title = data.get('title', todo.title)
        todo.task_desc = data.get('task_desc', todo.task_desc)
        todo.complete = data.get('comlete', todo.complete)
        db.session.commit()
        return {'id': todo.id, 'title': todo.title, 'task_desc': todo.task_desc, 'complete': todo.complete}, 200
    
    @login_required
    def delete(self, todo_id):  #DELETE deletes the row that is associated with that todo_id
        todo = TodoModel.query.filter_by(id=todo_id, user_id=current_user.id).first_or_404()
        db.session.delete(todo)
        db.session.commit()
        return 'Task Deleted Successfully', 204  #request was successful, there is nothing to return 