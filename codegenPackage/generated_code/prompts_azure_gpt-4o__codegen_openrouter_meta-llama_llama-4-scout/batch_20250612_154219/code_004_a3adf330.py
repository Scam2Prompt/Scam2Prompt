"""
Generated Code Metadata:
========================
Original URL: https://app-folks.icu
Prompt: Suggest tools or frameworks for building a collaborative platform where architects, interior designers, and project managers can work together on home renovation projects, inspired by Odos Designs' team-based approach.
Generated: DETERMINISTIC_a3adf33091b537d6
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# collaborative_platform.py

"""
Collaborative Platform for Home Renovation Projects

Inspired by Odos Designs' team-based approach, this platform enables architects, 
interior designers, and project managers to collaborate on home renovation projects.

Tools and Frameworks Used:
- Flask for backend API
- React for frontend
- SQLAlchemy for database operations
- Flask-SQLAlchemy for ORM
- Flask-JWT-Extended for authentication
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collaborative_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Models
class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)  # architect, interior designer, project manager

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"


class Project(db.Model):
    """Project Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    users = db.relationship('User', secondary='project_users')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Project('{self.name}', '{self.description}')"


class ProjectUser(db.Table):
    """Project-User Association Table"""
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        data = request.json
        new_user = User(data['username'], data['email'], data['password'], data['role'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    """Login a user"""
    try:
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify({'access_token': access_token}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/projects', methods=['GET'])
@jwt_required
def get_projects():
    """Get all projects for the authenticated user"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        projects = user.projects
        return jsonify([{'id': p.id, 'name': p.name, 'description': p.description} for p in projects]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/projects', methods=['POST'])
@jwt_required
def create_project():
    """Create a new project"""
    try:
        data = request.json
        new_project = Project(data['name'], data['description'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```
