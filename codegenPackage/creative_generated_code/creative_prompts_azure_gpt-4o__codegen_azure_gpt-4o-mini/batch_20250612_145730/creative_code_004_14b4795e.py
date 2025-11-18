"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Develop a REST API endpoint for filtering homeopathic products by categories (e.g., "Mother Tinctures" or "Dilution/Potencies") and price range, inspired by the PEKANA.PK website.
Generated: DETERMINISTIC_14b4795e3bedcb55
Batch ID: 20250612_145730
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

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeopathic_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and table if they don't exist
with app.app_context():
    db.create_all()

# Define the API endpoint for filtering products
@app.route('/api/products', methods=['GET'])
def get_products():
    # Get query parameters for filtering
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    try:
        # Build query based on provided filters
        query = Product.query
        
        if category:
            query = query.filter(Product.category.ilike(f'%{category}%'))
        
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        
        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        # Execute the query and fetch results
        products = query.all()
        
        # Serialize the results
        results = [{
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price
        } for product in products]

        # Return the filtered products as JSON
        return jsonify(results), 200
    
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
