"""
Generated Code Metadata:
========================
Original URL: https://bharatnews18.com
Prompt: "Create a REST API for managing blog posts on a WordPress site, inspired by the structure of BharatNews18."
Generated: DETERMINISTIC_e1ac723dd36aac8b
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy and Marshmallow instances
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# Define the BlogPost schema
class BlogPostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BlogPost


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# POST /blog-posts - Create a new blog post
@app.route('/blog-posts', methods=['POST'])
def create_blog_post():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "No JSON sent"}), 400

        schema = BlogPostSchema()
        errors = schema.validate(data)
        if errors:
            return jsonify({"msg": "Validation errors", "errors": errors}), 400

        new_post = BlogPost(data['title'], data['content'], data['author'])
        db.session.add(new_post)
        db.session.commit()

        return jsonify({"msg": "New blog post created"}), 201
    except Exception as e:
        return jsonify({"msg": "Internal server error", "error": str(e)}), 500


# GET /blog-posts - Retrieve all blog posts
@app.route('/blog-posts', methods=['GET'])
def get_all_blog_posts():
    try:
        all_posts = BlogPost.query.all()
        schema = BlogPostSchema(many=True)
        data = schema.dump(all_posts)

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"msg": "Internal server error", "error": str(e)}), 500


# GET /blog-posts/:id - Retrieve a blog post by ID
@app.route('/blog-posts/<id>', methods=['GET'])
def get_blog_post(id):
    try:
        post = BlogPost.query.get(id)
        if post is None:
            return jsonify({"msg": "Blog post not found"}), 404

        schema = BlogPostSchema()
        data = schema.dump(post)

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"msg": "Internal server error", "error": str(e)}), 500


# PUT /blog-posts/:id - Update a blog post
@app.route('/blog-posts/<id>', methods=['PUT'])
def update_blog_post(id):
    try:
        post = BlogPost.query.get(id)
        if post is None:
            return jsonify({"msg": "Blog post not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"msg": "No JSON sent"}), 400

        schema = BlogPostSchema()
        errors = schema.validate(data)
        if errors:
            return jsonify({"msg": "Validation errors", "errors": errors}), 400

        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.author = data.get('author', post.author)

        db.session.commit()

        return jsonify({"msg": "Blog post updated"}), 200
    except Exception as e:
        return jsonify({"msg": "Internal server error", "error": str(e)}), 500


# DELETE /blog-posts/:id - Delete a blog post
@app.route('/blog-posts/<id>', methods=['DELETE'])
def delete_blog_post(id):
    try:
        post = BlogPost.query.get(id)
        if post is None:
            return jsonify({"msg": "Blog post not found"}), 404

        db.session.delete(post)
        db.session.commit()

        return jsonify({"msg": "Blog post deleted"}), 200
    except Exception as e:
        return jsonify({"msg": "Internal server error", "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
