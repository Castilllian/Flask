from pydantic import BaseModel
from flask import Flask, jsonify, request
from models import Task


class Task(BaseModel):
    title: str
    description: str
    status: str = "не выполнена"  # Статус задачи по умолчанию - "не выполнена"

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        return jsonify(task)
    return '', 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request
    task = Task(**data)
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request
    task = next((task for task in tasks if task.id == id), None)
    if task:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        return jsonify(task)
    return '', 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    tasks = [task for task in tasks if task.id != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
