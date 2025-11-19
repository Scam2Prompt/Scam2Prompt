"""
Generated Code Metadata:
========================
Original URL: https://npors.net
Prompt: How can architects collaborate and showcase their projects using the Études Architect App, and what features does it offer for professional development?
Generated: DETERMINISTIC_52ae4c1e8d0bf4ea
Batch ID: 20250622_210655
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'etudes_architect.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    """Represents an architect user."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    projects = db.relationship('Project', backref='author', lazy=True)

    def set_password(self, password):
        """Sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the user's password."""
        return check_password_hash(self.password_hash, password)

# Define the Project model
class Project(db.Model):
    """Represents an architect's project."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400
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
            return jsonify({'error': 'No data provided'}), 400
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Missing required fields'}), 400
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401
        return jsonify({'message': 'User logged in successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        title = data.get('title')
        description = data.get('description')
        user_id = data.get('user_id')
        if not title or not description or not user_id:
            return jsonify({'error': 'Missing required fields'}), 400
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        new_project = Project(title=title, description=description, author=user)
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all projects for a user
@app.route('/projects/<int:user_id>', methods=['GET'])
def get_projects(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        projects = user.projects
        output = []
        for project in projects:
            project_data = {'id': project.id, 'title': project.title, 'description': project.description}
            output.append(project_data)
        return jsonify({'projects': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
