"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epicpinterestfail.com
Prompt: Suggest an API for retrieving metadata from blog posts about oral surgery, such as "Dr David Webb’s Journey in Oral Surgery," and demonstrate its implementation.
Generated: DETERMINISTIC_fcfc5b4ab49c8a24
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_metadata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for BlogPost metadata
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert BlogPost instance to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/posts', methods=['GET'])
def get_blog_posts():
    """Retrieve all blog posts."""
    try:
        posts = BlogPost.query.all()
        return jsonify([post.to_dict() for post in posts]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_blog_post(post_id):
    """Retrieve a specific blog post by ID."""
    try:
        post = BlogPost.query.get_or_404(post_id)
        return jsonify(post.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/posts', methods=['POST'])
def create_blog_post():
    """Create a new blog post."""
    data = request.get_json()
    try:
        # Validate incoming data
        if not all(key in data for key in ('title', 'author', 'content')):
            return jsonify({'error': 'Missing fields in request'}), 400

        new_post = BlogPost(
            title=data['title'],
            author=data['author'],
            content=data['content'],
            created_at=datetime.utcnow()
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify(new_post.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
