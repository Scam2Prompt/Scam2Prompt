"""
Generated Code Metadata:
========================
Original URL: https://828768840-96b.pages.dev
Prompt: Generate a code example for building a social interaction system for a cryptocurrency trading community, inspired by Blum's features.
Generated: DETERMINISTIC_4ebaddf56e2e23f0
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

# Define the Post model for user interactions
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return f'<Post {self.id} by User {self.user_id}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        raise BadRequest("Username is required.")

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "username": new_user.username}), 201

# Route to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    user_id = data.get('user_id')
    content = data.get('content')

    if not user_id or not content:
        raise BadRequest("User ID and content are required.")

    new_post = Post(user_id=user_id, content=content)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"id": new_post.id, "content": new_post.content}), 201

# Route to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": post.id, "user_id": post.user_id, "content": post.content, "created_at": post.created_at} for post in posts]), 200

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found."}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
