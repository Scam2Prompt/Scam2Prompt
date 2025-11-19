"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Create an API endpoint for retrieving the latest products from an online store, specifically for categories like dohányzóasztalok and fotelek.
Generated: DETERMINISTIC_c4423c3d635644d7
Batch ID: 20250612_155153
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # Database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert Product to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'created_at': self.created_at.isoformat()
        }

@app.route('/api/products/latest', methods=['GET'])
def get_latest_products():
    """
    Get the latest products from specific categories: dohányzóasztalok and fotelek.
    
    Returns:
        JSON response with the latest products in the specified categories.
    """
    try:
        # Retrieve query parameters for pagination (optional)
        limit = request.args.get('limit', default=10, type=int)
        offset = request.args.get('offset', default=0, type=int)

        # Filter for specific categories
        categories = ['dohányzóasztalok', 'fotelek']
        latest_products = Product.query.filter(Product.category.in_(categories)) \
            .order_by(Product.created_at.desc()) \
            .limit(limit) \
            .offset(offset) \
            .all()

        # Serialize the products to JSON
        products_list = [product.to_dict() for product in latest_products]

        return jsonify(products=products_list), 200

    except Exception as e:
        # Log the exception (could be replaced with a proper logging mechanism)
        print(f"Error retrieving latest products: {e}")
        return jsonify({'error': 'An error occurred while retrieving products.'}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application
```
