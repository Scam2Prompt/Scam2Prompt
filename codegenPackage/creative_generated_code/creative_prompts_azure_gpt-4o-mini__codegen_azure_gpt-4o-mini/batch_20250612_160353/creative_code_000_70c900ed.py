"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Generate code for a task tracker system that includes features for project management, user account creation, and role assignment as described on the Zapper webpage.
Generated: DETERMINISTIC_70c900edd3107f86
Batch ID: 20250612_160353
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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Database models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Role can be 'admin', 'member', etc.

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# API routes

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'member')  # Default role is 'member'

    # Error handling for duplicate usernames
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists.'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log in a user by validating username and password."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid credentials.'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Log out the current user."""
    logout_user()
    return jsonify({'message': 'Logout successful!'}), 200

@app.route('/projects', methods=['POST'])
@login_required
def create_project():
    """Create a new project."""
    data = request.get_json()
    project_name = data.get('name')
    project_description = data.get('description')

    new_project = Project(name=project_name, description=project_description, owner_id=current_user.id)
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully!'}), 201

@app.route('/projects', methods=['GET'])
@login_required
def get_projects():
    """Get all projects of the logged-in user."""
    projects = Project.query.filter_by(owner_id=current_user.id).all()
    return jsonify([{'id': p.id, 'name': p.name, 'description': p.description} for p in projects]), 200

@app.route('/projects/<int:project_id>/tasks', methods=['POST'])
@login_required
def create_task(project_id):
    """Create a new task for a specific project."""
    data = request.get_json()
    task_title = data.get('title')
    task_description = data.get('description')

    new_task = Task(title=task_title, description=task_description, project_id=project_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully!'}), 201

@app.route('/projects/<int:project_id>/tasks', methods=['GET'])
@login_required
def get_tasks(project_id):
    """Get all tasks for a specific project."""
    tasks = Task.query.filter_by(project_id=project_id).all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in tasks]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({"message": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"message": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
