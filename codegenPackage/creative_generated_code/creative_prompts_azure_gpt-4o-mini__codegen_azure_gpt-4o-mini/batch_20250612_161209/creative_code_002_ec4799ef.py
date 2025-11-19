"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deva.cl
Prompt: Create a RESTful API endpoint that allows users to query for specific hardware products, such as door stoppers and ventilation grills, based on the catalog provided by DEVA.
Generated: DETERMINISTIC_ec4799ef2aa54ae8
Batch ID: 20250612_161209
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
from sqlalchemy.exc import IntegrityError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hardware_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Hardware Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Convert the Product model to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve hardware products based on query parameters.
    Query parameters:
        - category (optional): Filter products by category
        - name (optional): Search products by name
    Returns:
        JSON list of products matching the query
    """
    try:
        category = request.args.get('category')
        name = request.args.get('name')

        # Build the query
        query = Product.query
        if category:
            query = query.filter(Product.category.ilike(f'%{category}%'))
        if name:
            query = query.filter(Product.name.ilike(f'%{name}%'))

        # Execute the query and convert results to a list of dictionaries
        products = query.all()
        result = [product.to_dict() for product in products]

        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error retrieving products: {e}")
        return jsonify({"error": "An error occurred while retrieving products."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
