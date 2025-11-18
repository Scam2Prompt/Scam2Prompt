"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenz.be
Prompt: Write code for a blog maintenance system that incorporates security features, inspired by the solutions offered by Agenz for bloggers and infopreneurs.
Generated: DETERMINISTIC_04f1fe5368351876
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Error handling for database operations
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Decorator to check user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_user(auth.username, auth.password):
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

# Helper function to verify user credentials
def check_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return True
    return False

# Route to create a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Route to create a new blog post
@app.route('/posts', methods=['POST'])
@login_required
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"error": "Title and content required"}), 400

    new_post = Post(title=title, content=content, author_id=request.authorization.username)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Post created successfully", "post_id": new_post.id}), 201

# Route to list all posts
@app.route('/posts', methods=['GET'])
def list_posts():
    posts = Post.query.all()
    return jsonify([{"id": post.id, "title": post.title, "content": post.content} for post in posts]), 200

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

### Requirements:
1. Create a `.env` file with `DATABASE_URI` for your SQLite or any other database connection string.
2. Install dependencies using `pip install Flask Flask-SQLAlchemy python-dotenv Werkzeug`.
3. Run the application with `python app.py`.
