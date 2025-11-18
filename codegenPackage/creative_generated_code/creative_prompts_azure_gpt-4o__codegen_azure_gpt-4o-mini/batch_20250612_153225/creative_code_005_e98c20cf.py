"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medpointye.com
Prompt: Develop a REST API endpoint to list products like "Inmunofluor Chlamydia T" and "Inmunofluor Toxoplasmosis" with sorting options, based on the MedPointYE catalog structure.
Generated: DETERMINISTIC_e98c20cf74c741f6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Change to your database config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model to represent the product structure in the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Product model to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to list products with optional sorting."""
    
    sort_by = request.args.get('sort_by', 'name')  # Default sort by name
    sort_order = request.args.get('sort_order', 'asc')  # Default sort order is ascending

    # Validate sort order
    if sort_order not in ['asc', 'desc']:
        abort(400, description="Invalid sort_order. Use 'asc' or 'desc'.")

    # Validate sort_by field
    if sort_by not in ['name', 'category', 'price']:
        abort(400, description="Invalid sort_by field. Use 'name', 'category', or 'price'.")

    # Build the query with sorting
    try:
        products_query = Product.query.order_by(
            getattr(Product, sort_by).asc() if sort_order == 'asc' else getattr(Product, sort_by).desc()
        )
        products = products_query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Log the error in a real application
        return jsonify({"error": "Database error occurred."}), 500

if __name__ == '__main__':
    # Create the database and tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
