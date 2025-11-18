"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Recommend libraries or APIs for building a blog section on an e-commerce site, similar to the "Herramientas destacadas para marketing digital" blog on "Mass Compras."
Generated: DETERMINISTIC_6a7fe011555c4dba
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    """Model for blog posts."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Route to create a new blog post
@app.route('/blog', methods=['POST'])
def create_blog_post():
    """Create a new blog post."""
    data = request.json
    try:
        new_post = BlogPost(title=data['title'], content=data['content'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Blog post created!', 'id': new_post.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create blog post. Ensure title is unique.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all blog posts
@app.route('/blog', methods=['GET'])
def get_blog_posts():
    """Retrieve all blog posts."""
    posts = BlogPost.query.all()
    return jsonify([{ 'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at } for post in posts]), 200

# Route to get a specific blog post by ID
@app.route('/blog/<int:post_id>', methods=['GET'])
def get_blog_post(post_id):
    """Retrieve a specific blog post by ID."""
    post = BlogPost.query.get_or_404(post_id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at}), 200

# Route to update a blog post
@app.route('/blog/<int:post_id>', methods=['PUT'])
def update_blog_post(post_id):
    """Update an existing blog post."""
    post = BlogPost.query.get_or_404(post_id)
    data = request.json
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify({'message': 'Blog post updated!'}), 200

# Route to delete a blog post
@app.route('/blog/<int:post_id>', methods=['DELETE'])
def delete_blog_post(post_id):
    """Delete a specific blog post by ID."""
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Blog post deleted!'}), 200

# Create the database and tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
