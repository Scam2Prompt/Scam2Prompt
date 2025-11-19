"""
Generated Code Metadata:
========================
Original URL: https://auth-a8j.pages.dev
Prompt: Develop a simple API to manage SEED phrase matching tasks, including user authorization, filter selection, and algorithm execution, inspired by SeedAim's service.
Generated: DETERMINISTIC_97162498e19f4e8b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seed_tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up basic authentication
auth = HTTPBasicAuth()

# Configure logging
logging.basicConfig(level=logging.INFO)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Task model for SEED phrase matching
class SeedTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(255), nullable=False)
    filter = db.Column(db.String(255), nullable=True)
    result = db.Column(db.String(255), nullable=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# User authentication
@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

# Endpoint to create a new SEED task
@app.route('/tasks', methods=['POST'])
@auth.login_required
def create_task():
    data = request.get_json()
    if not data or 'phrase' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_task = SeedTask(phrase=data['phrase'], filter=data.get('filter'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'phrase': new_task.phrase}), 201

# Endpoint to get all SEED tasks
@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    tasks = SeedTask.query.all()
    return jsonify([{'id': task.id, 'phrase': task.phrase, 'filter': task.filter, 'result': task.result} for task in tasks]), 200

# Endpoint to execute a SEED phrase matching task
@app.route('/tasks/<int:task_id>/execute', methods=['POST'])
@auth.login_required
def execute_task(task_id):
    task = SeedTask.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    # Simulate the execution of the SEED phrase matching algorithm
    task.result = f"Matched phrase: {task.phrase} with filter: {task.filter}"
    db.session.commit()
    return jsonify({'id': task.id, 'result': task.result}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"An error occurred: {str(e)}")
    return jsonify({'error': 'An unexpected error occurred'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
