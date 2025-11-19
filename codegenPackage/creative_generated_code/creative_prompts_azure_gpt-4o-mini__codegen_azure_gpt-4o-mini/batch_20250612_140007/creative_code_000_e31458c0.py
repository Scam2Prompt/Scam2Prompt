"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-ec.com
Prompt: Generate a code snippet for a web application that integrates social media management features, as described in the services offered by Kraken Digital.
Generated: DETERMINISTIC_e31458c0632b669e
Batch ID: 20250612_140007
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
import requests

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_media.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a model for social media posts
class SocialMediaPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(280), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Post {self.id} on {self.platform}>"

# Route to create a new social media post
@app.route('/api/posts', methods=['POST'])
def create_post():
    """Creates a new social media post."""
    data = request.get_json()
    
    # Validate incoming data
    if not data or 'content' not in data or 'platform' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    new_post = SocialMediaPost(content=data['content'], platform=data['platform'])
    
    # Attempt to save the new post to the database
    try:
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created", "post": {"id": new_post.id, "content": new_post.content, "platform": new_post.platform}}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to create post"}), 500

# Route to fetch all posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Retrieves all social media posts."""
    posts = SocialMediaPost.query.all()
    return jsonify([{"id": post.id, "content": post.content, "platform": post.platform} for post in posts]), 200

# Function to post to a social media platform (stub)
def post_to_social_media(platform, content):
    """Posts content to the specified social media platform."""
    # This function should contain the logic for posting to a social media API
    # Placeholder for example purposes
    print(f"Posting to {platform}: {content}")
    return True

# Run the app
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
