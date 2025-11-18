"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Provide a solution using Flask or Django to build a backend system for managing product inventory and promotions for a site like "Jurunense Home Center."
Generated: DETERMINISTIC_3af4678fc919a95f
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready solution using Flask to manage product inventory and promotions:

### Flask Application: Backend for Product Inventory and Promotions

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity, replace with production-ready DB if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Models

class Product(db.Model):
    """Model for storing product details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Promotion(db.Model):
    """Model for storing promotion details."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    discount = db.Column(db.Float, nullable=False)  # Discount in percentage
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

# Routes

@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products."""
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    } for product in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Fetch a single product by ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    })

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product."""
    try:
        data = request.json
        new_product = Product(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully', 'product_id': new_product.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    try:
        data = request.json
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

@app.route('/promotions', methods=['GET'])
def get_promotions():
    """Fetch all promotions."""
    promotions = Promotion.query.all()
    return jsonify([{
        'id': promotion.id,
        'product_id': promotion.product_id,
        'discount': promotion.discount,
        'start_date': promotion.start_date.strftime('%Y-%m-%d %H:%M:%S'),
        'end_date': promotion.end_date.strftime('%Y-%m-%d %H:%M:%S')
    } for promotion in promotions])

@app.route('/promotions', methods=['POST'])
def add_promotion():
    """Add a new promotion."""
    try:
        data = request.json
        product = Product.query.get(data['product_id'])
        if not product:
            return jsonify({'error': 'Invalid product ID'}), 404

        new_promotion = Promotion(
            product_id=data['product_id'],
            discount=data['discount'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d %H:%M:%S'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d %H:%M:%S')
        )
        db.session.add(new_promotion)
        db.session.commit()
        return jsonify({'message': 'Promotion added successfully', 'promotion_id': new_promotion.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/promotions/<int:promotion_id>', methods=['DELETE'])
def delete_promotion(promotion_id):
    """Delete a promotion."""
    promotion = Promotion.query.get(promotion_id)
    if not promotion:
        return jsonify({'error': 'Promotion not found'}), 404

    db.session.delete(promotion)
    db.session.commit()
    return jsonify({'message': 'Promotion deleted successfully'})

# Run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()

    app.run(debug=True)  # Use debug=False in production
```

### Steps to Run:
1. Save the code in a file, e.g., `app.py`.
2. Install dependencies: `pip install flask flask-sqlalchemy`.
3. Run the app: `python app.py`.
4. Use a tool like Postman or curl to interact with the API.

You can expand this application further by adding authentication, pagination for fetching products/promotions, and other advanced features as needed.
