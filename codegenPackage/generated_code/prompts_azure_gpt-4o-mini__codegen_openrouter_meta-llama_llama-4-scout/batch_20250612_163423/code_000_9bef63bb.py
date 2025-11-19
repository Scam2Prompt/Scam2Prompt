"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Generate a code snippet for a web application that facilitates online learning experiences similar to those offered by Virtual5, focusing on habit creation and personal development.
Generated: DETERMINISTIC_9bef63bb863e0d07
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    habits = db.relationship('Habit', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define the Habit model
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='habit', lazy=True)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username or not email or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Login a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Please provide all required fields'}), 400
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new habit
@app.route('/habits', methods=['POST'])
def create_habit():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        title = data.get('title')
        description = data.get('description')
        if not title or not description:
            return jsonify({'error': 'Please provide all required fields'}), 400
        user_id = request.args.get('user_id', type=int)
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        new_habit = Habit(title=title, description=description, user=user)
        db.session.add(new_habit)
        db.session.commit()
        return jsonify({'message': 'Habit created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all habits for a user
@app.route('/habits', methods=['GET'])
def get_habits():
    try:
        user_id = request.args.get('user_id', type=int)
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        habits = user.habits
        output = []
        for habit in habits:
            output.append({'id': habit.id, 'title': habit.title, 'description': habit.description})
        return jsonify(output), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
