"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: How can I implement a collaborative feature in a pool maintenance app similar to Pooltyme, allowing multiple users to log tasks?
Generated: DETERMINISTIC_1cdb6b155597edf3
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pool_maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database models
class User(db.Model):
    """
    Represents a user in the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model):
    """
    Represents a pool maintenance task logged by a user.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f'<Task {self.description} by User {self.user_id}>'


# Create database tables
@app.before_first_request
def create_tables():
    """
    Ensures database tables are created before the first request.
    """
    db.create_all()


# Routes
@app.route('/register', methods=['POST'])
def register_user():
    """
    Registers a new user in the application.
    """
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return jsonify({'error': 'Username and email are required'}), 400

        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully', 'user': {'id': user.id, 'username': user.username, 'email': user.email}}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500


@app.route('/log-task', methods=['POST'])
def log_task():
    """
    Logs a pool maintenance task for a specific user.
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        description = data.get('description')

        if not user_id or not description:
            return jsonify({'error': 'User ID and task description are required'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        task = Task(user_id=user_id, description=description)
        db.session.add(task)
        db.session.commit()

        return jsonify({'message': 'Task logged successfully', 'task': {'id': task.id, 'description': task.description, 'timestamp': task.timestamp}}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500


@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    """
    Retrieves all tasks for a specific user.
    """
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        tasks = Task.query.filter_by(user_id=user_id).all()
        tasks_data = [{'id': task.id, 'description': task.description, 'timestamp': task.timestamp} for task in tasks]

        return jsonify({'user': {'id': user.id, 'username': user.username}, 'tasks': tasks_data}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
