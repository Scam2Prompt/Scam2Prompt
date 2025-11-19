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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_support.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

# Define the Post schema for serialization
class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)

# Initialize the schema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Route to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    """Create a new post."""
    try:
        # Validate and deserialize input
        post_data = post_schema.load(request.json)
        new_post = Post(**post_data)
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post), 201
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Route to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    """Retrieve all posts."""
    posts = Post.query.all()
    return posts_schema.dump(posts), 200

# Route to get a specific post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Retrieve a specific post by ID."""
    post = Post.query.get_or_404(post_id)
    return post_schema.dump(post), 200

# Route to update a post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Update a specific post by ID."""
    post = Post.query.get_or_404(post_id)
    try:
        post_data = post_schema.load(request.json)
        post.title = post_data['title']
        post.content = post_data['content']
        db.session.commit()
        return post_schema.dump(post), 200
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

# Route to delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Delete a specific post by ID."""
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
