"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Develop a REST API endpoint to retrieve "Wall Memes" product categories and their associated products, including sale items, for use in a mobile app.
Generated: DETERMINISTIC_a04769a693e5e532
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules and frameworks
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wall_memes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Category model
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    # Relationship with Product
    products = db.relationship('Product', backref='category', lazy=True)

# Define the Product model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_on_sale = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

# Error handler for database errors
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    response = {
        "error": "Database error occurred",
        "message": str(error)
    }
    return jsonify(response), 500

# API endpoint to retrieve product categories and associated products
@app.route('/api/categories', methods=['GET'])
def get_categories():
    try:
        # Fetch all categories and their associated products
        categories = Category.query.all()
        result = []
        for category in categories:
            category_data = {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "products": [
                    {
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                        "is_on_sale": product.is_on_sale
                    }
                    for product in category.products
                ]
            }
            result.append(category_data)
        # Return the response as JSON
        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors
        response = {
            "error": "An error occurred while processing the request",
            "message": str(e)
        }
        return jsonify(response), 500

# Run the Flask app
if __name__ == '__main__':
    # Create tables if they do not exist
    with app.app_context():
        db.create_all()
    # Start the development server
    app.run(debug=True)
```
