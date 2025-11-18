"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepedao.org
Prompt: Recommend tools or libraries to implement a "help forum" feature for a wiki platform, inspired by WIKIWIKI's "助け合い掲示板."
Generated: DETERMINISTIC_4da9882068896109
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///help_forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database model for forum posts
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each post
    username = db.Column(db.String(50), nullable=False)  # Username of the poster
    title = db.Column(db.String(150), nullable=False)  # Title of the post
    content = db.Column(db.Text, nullable=False)  # Main content of the post
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp

# Route to create a new forum post
@app.route('/posts', methods=['POST'])
def create_post():
    try:
        # Retrieve data from request
        data = request.json
        username = data.get('username')
        title = data.get('title')
        content = data.get('content')

        # Validate input data
        if not username or not title or not content:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a new ForumPost object
        new_post = ForumPost(username=username, title=title, content=content)

        # Save the new post to the database
        db.session.add(new_post)
        db.session.commit()

        return jsonify({'message': 'Post created successfully'}), 201
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to get all forum posts
@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        # Query all posts from the database
        posts = ForumPost.query.order_by(ForumPost.created_at.desc()).all()

        # Format posts as a list of dictionaries
        posts_list = [{
            'id': post.id,
            'username': post.username,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for post in posts]

        return jsonify(posts_list), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to get a single forum post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    try:
        # Query the post by ID
        post = ForumPost.query.get(post_id)

        # If post not found, return 404
        if not post:
            return jsonify({'error': 'Post not found'}), 404

        # Return the post details
        post_data = {
            'id': post.id,
            'username': post.username,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(post_data), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to delete a forum post by ID
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        # Query the post by ID
        post = ForumPost.query.get(post_id)

        # If post not found, return 404
        if not post:
            return jsonify({'error': 'Post not found'}), 404

        # Delete the post from the database
        db.session.delete(post)
        db.session.commit()

        return jsonify({'message': 'Post deleted successfully'}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Initialize the database
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
