"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Create a RESTful API for managing a community support platform where women can share their experiences, receive encouragement, and participate in discussions, inspired by the "Comunidade Mulheres Restauradas" on WhatsApp.
Generated: DETERMINISTIC_e90aaf3ff559edcb
Batch ID: 20250622_210655
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

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return jsonify({"error": "Username and email are required"}), 400

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username or email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users]), 200

# Route to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    try:
        data = request.json
        user_id = data.get('user_id')
        content = data.get('content')

        if not user_id or not content:
            return jsonify({"error": "User ID and content are required"}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_post = Post(user_id=user_id, content=content)
        db.session.add(new_post)
        db.session.commit()

        return jsonify({"message": "Post created successfully", "post": {"id": new_post.id, "user_id": new_post.user_id, "content": new_post.content}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": post.id, "user_id": post.user_id, "content": post.content} for post in posts]), 200

# Route to get posts by a specific user
@app.route('/users/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify([{"id": post.id, "content": post.content} for post in user.posts]), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
