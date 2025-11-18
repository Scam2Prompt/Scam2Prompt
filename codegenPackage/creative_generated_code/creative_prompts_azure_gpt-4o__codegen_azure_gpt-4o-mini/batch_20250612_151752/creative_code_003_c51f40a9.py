"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Create a RESTful API design for an e-commerce platform that supports filtering products by categories such as "زیبایی و سلامت" and "کنسول بازی و لوازم جانبی."
Generated: DETERMINISTIC_c51f40a9f37f3792
Batch ID: 20250612_151752
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

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def serialize(self):
        """Return a serialized representation of the Product."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

# Initialize the database (for demonstration purposes; in production, this should be managed separately)
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieve all products or filter products by category.
    ---
    responses:
      200:
        description: A list of products filtered by category
      400:
        description: Bad request if filters are invalid
    """
    category = request.args.get('category')

    try:
        # Query all products or filter by category
        if category:
            products = Product.query.filter_by(category=category).all()
        else:
            products = Product.query.all()

        # Serialize the products to JSON
        return jsonify([product.serialize() for product in products]), 200

    except SQLAlchemyError as e:
        # Handle any SQL errors
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['POST'])
def create_product():
    """
    Create a new product.
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
              category:
                type: string
    responses:
      201:
        description: Product created successfully
      400:
        description: Bad request if the payload is invalid
    """
    data = request.json

    if 'name' not in data or 'category' not in data:
        return jsonify({"error": "Name and category are required."}), 400

    new_product = Product(name=data['name'], category=data['category'])

    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.serialize()), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
