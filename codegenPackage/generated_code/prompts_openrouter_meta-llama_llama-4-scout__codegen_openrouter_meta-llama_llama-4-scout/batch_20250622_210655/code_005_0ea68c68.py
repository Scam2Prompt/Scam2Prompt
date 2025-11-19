"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Suggest a set of Python libraries for building a web application similar to Portal de Saltinho, allowing teachers to create and manage interactive educational content for various subjects."
Generated: DETERMINISTIC_0ea68c68d73b5b80
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
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Create a Flask application instance
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"User('{self.username}')"

# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Define the Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, subject, user_id):
        self.title = title
        self.description = description
        self.subject = subject
        self.user_id = user_id

    def __repr__(self):
        return f"Content('{self.title}', '{self.subject}')"

# Define the Content schema
class ContentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Content

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'Username already exists'}), 400
        
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logger.error(e)
        return jsonify({'message': 'Failed to create user'}), 500

# Login a user
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400
        
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials'}), 401
        
        return jsonify({'message': 'Logged in successfully'}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'message': 'Failed to login'}), 500

# Create new content
@app.route('/content', methods=['POST'])
def create_content():
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        subject = data.get('subject')
        user_id = data.get('user_id')
        
        if not title or not description or not subject or not user_id:
            return jsonify({'message': 'All fields are required'}), 400
        
        new_content = Content(title, description, subject, user_id)
        db.session.add(new_content)
        db.session.commit()
        
        return jsonify({'message': 'Content created successfully'}), 201
    except Exception as e:
        logger.error(e)
        return jsonify({'message': 'Failed to create content'}), 500

# Get all content
@app.route('/content', methods=['GET'])
def get_content():
    try:
        content = Content.query.all()
        content_schema = ContentSchema(many=True)
        return jsonify(content_schema.dump(content)), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'message': 'Failed to get content'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
