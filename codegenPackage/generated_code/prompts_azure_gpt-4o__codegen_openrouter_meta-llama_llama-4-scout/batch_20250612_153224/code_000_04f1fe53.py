"""
Generated Code Metadata:
========================
Original URL: https://agenz.be
Prompt: Write code for a blog maintenance system that incorporates security features, inspired by the solutions offered by Agenz for bloggers and infopreneurs.
Generated: DETERMINISTIC_04f1fe5368351876
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blog_maintenance_system.py

import os
import logging
import hashlib
import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(16)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Set up logging
logging.basicConfig(filename='blog.log', level=logging.INFO)

class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return check_password_hash(self.password, password)

class Post(db.Model):
    """Represents a blog post in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

@app.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/login', methods=['POST'])
def login():
    """Logs in a user and returns an access token."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401

        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/posts', methods=['POST'])
@jwt_required
def create_post():
    """Creates a new blog post."""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request'}), 400

        title = data.get('title')
        content = data.get('content')

        if not title or not content:
            return jsonify({'error': 'Title and content are required'}), 400

        author_id = User.query.filter_by(username=get_jwt_identity()).first().id
        new_post = Post(title, content, author_id)
        db.session.add(new_post)
        db.session.commit()

        return jsonify({'message': 'Post created successfully'}), 201
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/posts', methods=['GET'])
@jwt_required
def get_posts():
    """Retrieves all blog posts."""
    try:
        posts = Post.query.all()
        output = []
        for post in posts:
            post_data = {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'author': User.query.filter_by(id=post.author_id).first().username
            }
            output.append(post_data)
        return jsonify({'posts': output}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
