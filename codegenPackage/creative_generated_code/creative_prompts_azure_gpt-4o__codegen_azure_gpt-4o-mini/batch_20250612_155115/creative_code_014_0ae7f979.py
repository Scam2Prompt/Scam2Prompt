"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Create a Flask API to manage product filtering based on user-selected attributes like material, style, and fit, and return JSON responses for front-end integration.
Generated: DETERMINISTIC_0ae7f9797287060c
Batch ID: 20250612_155115
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Example database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model definition
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50), nullable=False)
    fit = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert product instance to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'material': self.material,
            'style': self.style,
            'fit': self.fit
        }

# Endpoint to filter products by attributes
@app.route('/api/products', methods=['GET'])
def get_filtered_products():
    """Retrieve products filtered by selected attributes."""
    material = request.args.get('material')
    style = request.args.get('style')
    fit = request.args.get('fit')

    # Build query dynamically based on provided filters
    query = Product.query

    if material:
        query = query.filter(Product.material == material)
    if style:
        query = query.filter(Product.style == style)
    if fit:
        query = query.filter(Product.fit == fit)

    try:
        products = query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask app in debug mode
```
