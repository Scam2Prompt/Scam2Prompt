"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epicpinterestfail.com
Prompt: Generate code to filter blog posts by tags such as "Dental," "Surgery," and "Health" and display them in a user-friendly interface.
Generated: DETERMINISTIC_5481b3a3e7ee2ba2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200), nullable=False)  # Comma-separated tags

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Route to display blog posts filtered by tag
@app.route('/posts', methods=['GET'])
def get_posts():
    # Get the tag from query parameters
    tag = request.args.get('tag', '').strip()
    
    # Validate the tag input
    if tag and tag not in ["Dental", "Surgery", "Health"]:
        return jsonify({"error": "Invalid tag"}), 400  # Return error for invalid tags
    
    # Query the blog posts based on the tag
    if tag:
        posts = BlogPost.query.filter(BlogPost.tags.like(f'%{tag}%')).all()
    else:
        posts = BlogPost.query.all()  # Return all posts if no tag is provided
    
    # Render the posts in the user-friendly interface
    return render_template('posts.html', posts=posts, selected_tag=tag)

# Error handling for database-related errors
@app.errorhandler(Exception)
def handle_exception(e):
    # Handle all exceptions and return a JSON response
    return jsonify({"error": str(e)}), 500

# Create the database tables (only for the first run)
@app.before_first_request
def create_tables():
    db.create_all()

# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (posts.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .post { margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; }
        .tag-filter { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>
    <div class="tag-filter">
        <h3>Filter by Tag:</h3>
        <a href="/posts?tag=Dental">Dental</a>
        <a href="/posts?tag=Surgery">Surgery</a>
        <a href="/posts?tag=Health">Health</a>
        <a href="/posts">All</a>
    </div>
    <div>
        {% if posts %}
            {% for post in posts %}
                <div class="post">
                    <h2>{{ post.title }}</h2>
                    <p>{{ post.content }}</p>
                    <p><strong>Tags:</strong> {{ post.tags }}</p>
                </div>
            {% endfor %}
        {% else %}
            <p>No posts found.</p>
        {% endif %}
    </div>
</body>
</html>
```
