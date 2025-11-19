"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Generate code for a community-driven platform for hacktivism, inspired by the ETHBerlin event and its mission to push decentralized ecosystems forward.
Generated: DETERMINISTIC_395bc81da6b8163e
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community-Driven Hacktivism Platform
Inspired by ETHBerlin's mission to push decentralized ecosystems forward.

This code provides a basic implementation of a platform where users can:
1. Register and log in.
2. Create and join hacktivism projects.
3. Collaborate and share ideas.

Framework: Flask (Python)
Database: SQLite (for simplicity)
"""

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hacktivism.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

# Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Association table for users and projects
user_project_association = db.Table('user_project_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

# Route: Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        data = request.json
        name = data.get('name')
        description = data.get('description')

        if not name or not description:
            return jsonify({'error': 'Name and description are required'}), 400

        if Project.query.filter_by(name=name).first():
            return jsonify({'error': 'Project name already exists'}), 400

        new_project = Project(name=name, description=description, creator_id=session['user_id'])
        db.session.add(new_project)
        db.session.commit()

        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Join a project
@app.route('/projects/<int:project_id>/join', methods=['POST'])
def join_project(project_id):
    try:
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        project = Project.query.get(project_id)
        if not project:
            return jsonify({'error': 'Project not found'}), 404

        user = User.query.get(session['user_id'])
        if user in project.users:
            return jsonify({'error': 'Already a member of this project'}), 400

        project.users.append(user)
        db.session.commit()

        return jsonify({'message': 'Joined project successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: List all projects
@app.route('/projects', methods=['GET'])
def list_projects():
    try:
        projects = Project.query.all()
        project_list = [{'id': p.id, 'name': p.name, 'description': p.description} for p in projects]
        return jsonify(project_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Logout
@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.pop('user_id', None)
        return jsonify({'message': 'Logged out successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize database and run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
```
