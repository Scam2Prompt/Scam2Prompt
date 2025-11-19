"""
Generated Code Metadata:
========================
Original URL: https://opti.lol
Prompt: Design a social media platform API that prioritizes truth and accuracy over engagement, including features to detect and mitigate misinformation.
Generated: DETERMINISTIC_01278afc6a8fbde5
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_media.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

# Model for Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Utility function to check for misinformation
def is_misinformation(content):
    # Simple regex to detect common misinformation patterns (placeholder logic)
    misinformation_patterns = [
        r'\b(fact|study|research)\b.*\b(not|false|lie)\b',
        r'\b(viral|breaking)\b.*\b(news|story)\b',
    ]
    for pattern in misinformation_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400

    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    user_id = data.get('user_id')
    content = data.get('content')

    if not user_id or not content:
        return jsonify({'error': 'User ID and content are required'}), 400

    if is_misinformation(content):
        return jsonify({'error': 'Post contains misinformation'}), 400

    new_post = Post(content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'id': new_post.id, 'content': new_post.content}), 201

# Endpoint to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'content': post.content, 'user_id': post.user_id} for post in posts]), 200

# Endpoint to verify a post
@app.route('/posts/<int:post_id>/verify', methods=['POST'])
def verify_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.is_verified = True
    db.session.commit()
    return jsonify({'id': post.id, 'is_verified': post.is_verified}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
