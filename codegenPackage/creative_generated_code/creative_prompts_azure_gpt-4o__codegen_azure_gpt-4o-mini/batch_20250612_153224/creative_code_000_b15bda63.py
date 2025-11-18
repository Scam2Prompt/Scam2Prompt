"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: Write code to implement a wishlist feature for an e-commerce platform, allowing users to create, find, manage, and view lists, similar to the functionality described on Alwan's website.
Generated: DETERMINISTIC_b15bda63fb7fad9b
Batch ID: 20250612_153224
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

# Database model for Wishlist
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'name': self.name}

# Database model for Wishlist items
class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)  # Assuming product_id is an integer
    quantity = db.Column(db.Integer, default=1)

    def to_dict(self):
        return {'id': self.id, 'wishlist_id': self.wishlist_id, 'product_id': self.product_id, 'quantity': self.quantity}

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/wishlists', methods=['POST'])
def create_wishlist():
    """Create a new wishlist for a user."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'name' not in data:
        abort(400, 'Invalid data: user_id and name are required.')

    wishlist = Wishlist(user_id=data['user_id'], name=data['name'])
    db.session.add(wishlist)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, 'Error creating wishlist. Please try again.')

    return jsonify(wishlist.to_dict()), 201

@app.route('/wishlists/<int:user_id>', methods=['GET'])
def get_wishlists(user_id):
    """Get all wishlists for a user."""
    wishlists = Wishlist.query.filter_by(user_id=user_id).all()
    return jsonify([wishlist.to_dict() for wishlist in wishlists]), 200

@app.route('/wishlists/<int:wishlist_id>', methods=['GET'])
def get_wishlist(wishlist_id):
    """Get a specific wishlist by ID."""
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        abort(404, 'Wishlist not found.')
    return jsonify(wishlist.to_dict()), 200

@app.route('/wishlists/<int:wishlist_id>', methods=['DELETE'])
def delete_wishlist(wishlist_id):
    """Delete a specific wishlist by ID."""
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        abort(404, 'Wishlist not found.')

    db.session.delete(wishlist)
    db.session.commit()
    return jsonify({'message': 'Wishlist deleted successfully.'}), 200

@app.route('/wishlists/<int:wishlist_id>/items', methods=['POST'])
def add_item_to_wishlist(wishlist_id):
    """Add an item to a specific wishlist."""
    data = request.get_json()
    if not data or 'product_id' not in data:
        abort(400, 'Invalid data: product_id is required.')

    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        abort(404, 'Wishlist not found.')

    wishlist_item = WishlistItem(wishlist_id=wishlist_id, product_id=data['product_id'], quantity=data.get('quantity', 1))
    db.session.add(wishlist_item)
    db.session.commit()
    return jsonify(wishlist_item.to_dict()), 201

@app.route('/wishlists/<int:wishlist_id>/items', methods=['GET'])
def get_wishlist_items(wishlist_id):
    """Get all items from a specific wishlist."""
    wishlist_items = WishlistItem.query.filter_by(wishlist_id=wishlist_id).all()
    return jsonify([item.to_dict() for item in wishlist_items]), 200

@app.route('/wishlists/items/<int:item_id>', methods=['DELETE'])
def delete_wishlist_item(item_id):
    """Delete a specific item from a wishlist."""
    item = WishlistItem.query.get(item_id)
    if not item:
        abort(404, 'Item not found.')

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)  # In production, set debug to False and configure proper logging
```
