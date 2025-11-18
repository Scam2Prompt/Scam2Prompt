"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Create a REST API endpoint to fetch product details from an e-commerce database structured similarly to "Poly-Market.hu," including filtering by category and price range.
Generated: DETERMINISTIC_2b46d11635b06b92
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the product instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

@app.route('/api/products', methods=['GET'])
def get_products():
    """Fetch product details filtered by category and price range."""
    try:
        category = request.args.get('category')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        query = Product.query
        
        # Filter by category if provided
        if category:
            query = query.filter(Product.category == category)
        
        # Filter by price range if provided
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        # Fetch filtered products
        products = query.all()

        # Convert products to a list of dictionaries
        return jsonify([product.to_dict() for product in products]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred.", "message": str(e)}), 500
    except Exception as e:
        # Handle all other errors
        return jsonify({"error": "An unexpected error occurred.", "message": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Start the Flask application
    app.run(debug=True)
```

Make sure to replace the database URI with one that corresponds to your database configuration when deploying this code to production.
