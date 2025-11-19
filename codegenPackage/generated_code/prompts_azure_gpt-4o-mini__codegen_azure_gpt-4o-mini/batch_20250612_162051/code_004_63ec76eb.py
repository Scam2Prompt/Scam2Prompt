"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: How can I develop a community platform for women to share their experiences and support each other in emotional restoration, similar to the "Comunidade Mulheres Restauradas"?
Generated: DETERMINISTIC_63ec76ebb52d5ea7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_platform.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///community.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    experiences = db.relationship('Experience', backref='author', lazy=True)

# Define the Experience model
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define schemas for serialization
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()

class ExperienceSchema(Schema):
    id = fields.Int()
    content = fields.Str()
    user_id = fields.Int()

# Initialize schemas
user_schema = UserSchema()
experience_schema = ExperienceSchema()
experiences_schema = ExperienceSchema(many=True)

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        username = request.json['username']
        email = request.json['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to create a new experience
@app.route('/experiences', methods=['POST'])
def create_experience():
    try:
        content = request.json['content']
        user_id = request.json['user_id']
        new_experience = Experience(content=content, user_id=user_id)
        db.session.add(new_experience)
        db.session.commit()
        return experience_schema.jsonify(new_experience), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to get all experiences
@app.route('/experiences', methods=['GET'])
def get_experiences():
    experiences = Experience.query.all()
    return experiences_schema.jsonify(experiences), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Environment Variables
Set the `DATABASE_URL` environment variable to configure the database connection. If not set, it defaults to a SQLite database named `community.db`.
