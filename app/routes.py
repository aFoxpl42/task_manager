from flask import Blueprint, request, jsonify
from . import db
from .models import Task
from datetime import datetime

main = Blueprint('main', __name__)

@main.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "description": t.description,
        "priority": t.priority,
        "status": t.status,
        "due_date": t.due_date.isoformat() if t.due_date else None,
        "created_at": t.created_at.isoformat()
    } for t in tasks])

@main.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        priority=data.get("priority", "Medium"),
        due_date=datetime.fromisoformat(data["due_date"]) if data.get("due_date") else None
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created", "id": task.id}), 201
