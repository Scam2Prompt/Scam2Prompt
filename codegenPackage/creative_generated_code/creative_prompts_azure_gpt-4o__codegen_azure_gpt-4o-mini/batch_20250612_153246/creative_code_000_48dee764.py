"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Write code for an e-commerce website that allows users to select multiple variants of products, similar to the functionality described for Samsung S25 Ultra on TaniPhone.com.
Generated: DETERMINISTIC_48dee764e2478fce
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    variants = db.relationship('Variant', backref='product', lazy=True)

# Database model for Product Variants
class Variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    storage = db.Column(db.String(50), nullable=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to retrieve products and their variants
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        products_data = [
            {
                'id': product.id,
                'name': product.name,
                'variants': [
                    {'id': variant.id, 'color': variant.color, 'storage': variant.storage}
                    for variant in product.variants
                ]
            } for product in products
        ]
        return jsonify(products_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to add a new product with variants
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    try:
        new_product = Product(name=data['name'])
        db.session.add(new_product)
        db.session.commit()

        for variant in data['variants']:
            new_variant = Variant(product_id=new_product.id, color=variant['color'], storage=variant['storage'])
            db.session.add(new_variant)

        db.session.commit()
        return jsonify({'message': 'Product added successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product with this name already exists.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Ensure you have Flask and Flask-SQLAlchemy installed. You can install these using:
```bash
pip install Flask Flask-SQLAlchemy
```

### Database Initialization
- The database will be initialized automatically on the first request due to the `create_tables` function. Make sure to run this application in an environment where you have permissions to create the SQLite database file.
