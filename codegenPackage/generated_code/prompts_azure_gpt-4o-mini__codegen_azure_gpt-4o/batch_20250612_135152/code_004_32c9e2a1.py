"""
Generated Code Metadata:
========================
Original URL: https://ullivis.blogspot.com
Prompt: Suggest a library for managing blog posts and user profiles in a web application, similar to features found in Blogger.
Generated: DETERMINISTIC_32c9e2a19ec4366d
Batch ID: 20250612_135152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation using the Flask framework and SQLAlchemy for managing blog posts and user profiles. This code is production-ready, well-documented, and follows best practices.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert User object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

# Define the BlogPost model
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to User model
    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def to_dict(self):
        """Convert BlogPost object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author_id': self.author_id,
            'author_username': self.author.username,
            'created_at': self.created_at.isoformat()
        }

# Create database tables
with app.app_context():
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return jsonify({'error': 'Username and email are required'}), 400

        # Check for duplicate username or email
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'error': 'Username or email already exists'}), 400

        # Create and save the user
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User created successfully', 'user': user.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to create a new blog post
@app.route('/posts', methods=['POST'])
def create_post():
    try:
        data = request.json
        title = data.get('title')
        content = data.get('content')
        author_id = data.get('author_id')

        if not title or not content or not author_id:
            return jsonify({'error': 'Title, content, and author_id are required'}), 400

        # Check if the author exists
        author = User.query.get(author_id)
        if not author:
            return jsonify({'error': 'Author not found'}), 404

        # Create and save the blog post
        post = BlogPost(title=title, content=content, author_id=author_id)
        db.session.add(post)
        db.session.commit()

        return jsonify({'message': 'Post created successfully', 'post': post.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to fetch all blog posts
@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        posts = BlogPost.query.all()
        return jsonify({'posts': [post.to_dict() for post in posts]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify({'users': [user.to_dict() for user in users]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to fetch a specific user's blog posts
@app.route('/users/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'posts': [post.to_dict() for post in user.posts]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic library for managing users and blog posts in a web application. It includes routes for creating users and posts, fetching all users and posts, and fetching posts by a specific user. It uses Flask for the web framework and SQLAlchemy for database management.
