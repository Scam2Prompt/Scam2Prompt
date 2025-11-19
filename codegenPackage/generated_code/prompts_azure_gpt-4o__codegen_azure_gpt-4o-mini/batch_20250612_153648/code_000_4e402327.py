"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: Write code to prototype a web publishing platform that incorporates SEO optimization and e-commerce functionality, as described in the services offered by metamass.de.
Generated: DETERMINISTIC_4e40232703ed2ce7
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the database model for a Blog Post
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    seo_title = db.Column(db.String(100), nullable=False)
    seo_description = db.Column(db.String(160), nullable=False)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Define the database model for a Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Route to create a new blog post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = BlogPost(
        title=data['title'],
        content=data['content'],
        seo_title=data['seo_title'],
        seo_description=data['seo_description']
    )
    try:
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Post creation failed!'}), 400

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description']
    )
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product creation failed!'}), 400

# Route to display all blog posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = BlogPost.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]), 200

# Route to display all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price} for product in products]), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Set the `DATABASE_URL` environment variable to configure the database connection.
- This code provides basic CRUD functionality for blog posts and products, with SEO fields included for blog posts.
- Error handling is implemented for common scenarios.
