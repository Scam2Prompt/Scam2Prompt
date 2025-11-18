"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Write code to generate a customer wishlist feature for an e-commerce platform, inspired by the wishlist functionality on Frigoterm.ro.
Generated: DETERMINISTIC_a2a0ae70327d5866
Batch ID: 20250612_154601
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Customer
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    wishlists = db.relationship('Wishlist', backref='customer', lazy=True)

# Database model for Wishlist
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/customers', methods=['POST'])
def create_customer():
    """Create a new customer."""
    data = request.get_json()
    if not data or not 'name' in data or not 'email' in data:
        abort(400, 'Must include name and email.')

    new_customer = Customer(name=data['name'], email=data['email'])
    try:
        db.session.add(new_customer)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, 'Email already exists.')

    return jsonify({'id': new_customer.id, 'name': new_customer.name}), 201

@app.route('/customers/<int:customer_id>/wishlists', methods=['POST'])
def add_to_wishlist(customer_id):
    """Add a product to a customer's wishlist."""
    data = request.get_json()
    if not data or not 'product_name' in data:
        abort(400, 'Must include product_name.')

    new_wishlist_item = Wishlist(product_name=data['product_name'], customer_id=customer_id)
    db.session.add(new_wishlist_item)
    db.session.commit()

    return jsonify({'id': new_wishlist_item.id, 'product_name': new_wishlist_item.product_name}), 201

@app.route('/customers/<int:customer_id>/wishlists', methods=['GET'])
def get_wishlist(customer_id):
    """Get all wishlist items for a customer."""
    wishlists = Wishlist.query.filter_by(customer_id=customer_id).all()
    return jsonify([{'id': item.id, 'product_name': item.product_name} for item in wishlists]), 200

@app.route('/customers/<int:customer_id>/wishlists/<int:item_id>', methods=['DELETE'])
def remove_from_wishlist(customer_id, item_id):
    """Remove a product from a customer's wishlist."""
    wishlist_item = Wishlist.query.filter_by(id=item_id, customer_id=customer_id).first()
    if not wishlist_item:
        abort(404, 'Wishlist item not found.')

    db.session.delete(wishlist_item)
    db.session.commit()
    return jsonify({'result': True}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
