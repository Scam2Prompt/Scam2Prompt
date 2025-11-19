"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pranaisland.com
Prompt: Create an API endpoint that retrieves the latest products from a jewelry shop, including details on pricing and availability for items like gold-plated copper and crystal beads.
Generated: DETERMINISTIC_ba2810074eb51ccd
Batch ID: 20250612_160804
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

# Configure the database (SQLite for simplicity; use environment variables for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Convert the Product instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'material': self.material,
            'price': self.price,
            'availability': self.availability
        }

# Create the database tables (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve the latest products
@app.route('/api/products/latest', methods=['GET'])
def get_latest_products():
    try:
        # Query for the latest products (assuming 'latest' means all available products)
        latest_products = Product.query.filter_by(availability=True).all()
        
        # Convert products to a list of dictionaries
        products_list = [product.to_dict() for product in latest_products]
        
        return jsonify({
            'success': True,
            'data': products_list
        }), 200
        
    except SQLAlchemyError as e:
        # Log the error (placeholder for actual logging)
        print(f"Database error occurred: {e}")
        
        return jsonify({
            'success': False,
            'message': 'An error occurred while retrieving products.',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
