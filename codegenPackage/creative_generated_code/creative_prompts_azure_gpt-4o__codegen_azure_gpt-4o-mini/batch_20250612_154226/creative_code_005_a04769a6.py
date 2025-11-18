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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memes.db'  # Use SQLite for simplicity; in production, switch to a robust DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    sale_price = db.Column(db.Float, nullable=True)
    is_on_sale = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sale_price': self.sale_price,
            'is_on_sale': self.is_on_sale
        }

# Define the Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'products': [product.to_dict() for product in self.products]
        }

# Create the database tables (Run this once)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve Wall Memes product categories and associated products
@app.route('/api/wall_memes/categories', methods=['GET'])
def get_categories():
    try:
        categories = Category.query.all()  # Fetch all categories
        return jsonify([category.to_dict() for category in categories]), 200
    except SQLAlchemyError as e:
        # Log the error, return a generic error message
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({"error": "Could not retrieve categories."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=True for development; set to False in production
```
