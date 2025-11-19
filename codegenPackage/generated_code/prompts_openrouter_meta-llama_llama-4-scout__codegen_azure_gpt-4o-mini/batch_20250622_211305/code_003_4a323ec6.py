"""
Generated Code Metadata:
========================
Original URL: https://the-immediatex.com
Prompt: Design a system architecture for an investment education platform that provides online trading tutorials, workshops, and connects learners with seasoned experts, using immediate x as a reference.
Generated: DETERMINISTIC_4a323ec6b4cdcf7a
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_education_platform.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_education.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'learner' or 'expert'

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

# Schema for User
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Model for Tutorial
class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, created_by):
        self.title = title
        self.content = content
        self.created_by = created_by

# Schema for Tutorial
class TutorialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tutorial

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def add_user():
    try:
        name = request.json['name']
        email = request.json['email']
        role = request.json['role']
        new_user = User(name, email, role)
        db.session.add(new_user)
        db.session.commit()
        return UserSchema().jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return UserSchema(many=True).jsonify(users)

# Route to create a new tutorial
@app.route('/tutorials', methods=['POST'])
def add_tutorial():
    try:
        title = request.json['title']
        content = request.json['content']
        created_by = request.json['created_by']
        new_tutorial = Tutorial(title, content, created_by)
        db.session.add(new_tutorial)
        db.session.commit()
        return TutorialSchema().jsonify(new_tutorial), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all tutorials
@app.route('/tutorials', methods=['GET'])
def get_tutorials():
    tutorials = Tutorial.query.all()
    return TutorialSchema(many=True).jsonify(tutorials)

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic structure for an investment education platform using Flask, SQLAlchemy, and Marshmallow. It includes user and tutorial models, routes for creating and retrieving users and tutorials, and error handling for common issues.
