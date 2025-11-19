"""
Generated Code Metadata:
========================
Original URL: https://pilotmassiveai.pages.dev
Prompt: Suggest tools or libraries to build a simple task management system where users can earn rewards, similar to the concept of MASSIVE Pilot.
Generated: DETERMINISTIC_748996a2ea4ffacb
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Task Management System with Rewards**
======================================

**System Requirements**
-----------------------

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Marshmallow 0.14+

**Code**
------
```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///task_management.db")
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tasks = db.relationship("Task", backref="user", lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    rewards = db.relationship("Reward", backref="task", lazy=True)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)

    def __init__(self, name, description, points, task_id):
        self.name = name
        self.description = description
        self.points = points
        self.task_id = task_id


# Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task


class RewardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reward


# API Endpoints
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user_schema = UserSchema()
        user_data = request.get_json()
        user = User(user_data["username"], user_data["password"])
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/tasks", methods=["POST"])
def create_task():
    try:
        task_schema = TaskSchema()
        task_data = request.get_json()
        task = Task(task_data["title"], task_data["description"], task_data["user_id"])
        db.session.add(task)
        db.session.commit()
        return task_schema.dump(task)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/rewards", methods=["POST"])
def create_reward():
    try:
        reward_schema = RewardSchema()
        reward_data = request.get_json()
        reward = Reward(reward_data["name"], reward_data["description"], reward_data["points"], reward_data["task_id"])
        db.session.add(reward)
        db.session.commit()
        return reward_schema.dump(reward)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    try:
        task = Task.query.get(task_id)
        if task:
            task.completed = True
            db.session.commit()
            return jsonify({"message": "Task completed successfully"})
        else:
            return jsonify({"error": "Task not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/users/<int:user_id>/rewards", methods=["GET"])
def get_user_rewards(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            tasks = Task.query.filter_by(user_id=user_id).all()
            rewards = []
            for task in tasks:
                if task.completed:
                    task_rewards = Reward.query.filter_by(task_id=task.id).all()
                    rewards.extend(task_rewards)
            return jsonify([{"name": reward.name, "description": reward.description, "points": reward.points} for reward in rewards])
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-Marshmallow==0.14.0
```

```bash
# Run the application
python app.py
```

```bash
# Install dependencies
pip install -r requirements.txt
```
