"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Suggest a library or framework for building an e-commerce platform that allows users to customize and purchase UDIZINE's retail display fixtures online.
Generated: DETERMINISTIC_7f2a9fff33f084cd
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to build a basic e-commerce application using Flask and Flask-SQLAlchemy.
For customization and purchase of UDIZINE's retail display fixtures, additional features like payment processing,
inventory management, and product customization can be added later.

Prerequisites:
- Install Flask: pip install flask
- Install Flask-SQLAlchemy: pip install flask-sqlalchemy

Best Practices followed:
- Modular design for scalability
- Error handling for robustness
- Comments and docstrings for documentation
- Use of environment variables for sensitive information
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///ecommerce.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Product object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock
        }

# Define error handling
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# API route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    try:
        data = request.json
        new_product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully!", "product": new_product.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API route to get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    """Retrieve all products from the database."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# API route to purchase a product
@app.route('/purchase/<int:product_id>', methods=['POST'])
def purchase_product(product_id):
    """Handle product purchases."""
    try:
        product = Product.query.get_or_404(product_id)
        data = request.json
        quantity = data.get('quantity', 1)

        if product.stock < quantity:
            return jsonify({"error": "Insufficient stock"}), 400

        product.stock -= quantity
        db.session.commit()
        return jsonify({"message": "Purchase successful!", "product": product.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Main function to run the app
if __name__ == "__main__":
    with app.app_context():
        # Create tables if not exist
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Replace `sqlite:///ecommerce.db` with a production-ready database URL (e.g., PostgreSQL, MySQL) in `DATABASE_URL`.
- Use environment variables for sensitive information such as database credentials.
- Add authentication and authorization for securing the API.
- Integrate third-party services like Stripe or PayPal for payment processing.
