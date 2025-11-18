"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Provide code to create a blog section for a real estate website, allowing posts about market trends (e.g., rental price increases, remittance statistics) as seen on Félix Trujillo Falla's blog.
Generated: DETERMINISTIC_83bacf81eb05593f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Post model
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Post object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/posts', methods=['POST'])
def create_post():
    """Create a new blog post."""
    data = request.get_json()

    # Validate request data
    if not data or not 'title' in data or not 'content' in data:
        abort(400, description="Title and content are required.")

    new_post = Post(title=data['title'], content=data['content'])
    
    try:
        db.session.add(new_post)
        db.session.commit()
        return jsonify(new_post.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

@app.route('/posts', methods=['GET'])
def get_posts():
    """Retrieve all blog posts."""
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Retrieve a single blog post by ID."""
    post = Post.query.get(post_id)
    if post is None:
        abort(404, description="Post not found.")
    return jsonify(post.to_dict()), 200

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Update an existing blog post."""
    post = Post.query.get(post_id)
    if post is None:
        abort(404, description="Post not found.")

    data = request.get_json()
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']

    try:
        db.session.commit()
        return jsonify(post.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Delete a blog post by ID."""
    post = Post.query.get(post_id)
    if post is None:
        abort(404, description="Post not found.")

    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": "Post deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()
        abort(500, description=str(e))

if __name__ == '__main__':
    app.run(debug=True)
```
