"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Develop a RESTful API endpoint for managing a wishlist of medical products, similar to the functionality provided by Curaheridas for their users.
Generated: DETERMINISTIC_be2ff863e1ccad16
Batch ID: 20250612_155432
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Wishlist model
class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)

# Initialize the database and create tables
with app.app_context():
    db.create_all()

@app.route('/wishlist', methods=['GET'])
def get_wishlist():
    """
    Retrieve all items in the wishlist.
    """
    items = WishlistItem.query.all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price
    } for item in items]), 200

@app.route('/wishlist/<int:item_id>', methods=['GET'])
def get_wishlist_item(item_id):
    """
    Retrieve a single wishlist item by ID.
    """
    item = WishlistItem.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    return jsonify({
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price
    }), 200

@app.route('/wishlist', methods=['POST'])
def add_wishlist_item():
    """
    Add a new item to the wishlist.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        new_item = WishlistItem(name=name, description=description, price=price)
        db.session.add(new_item)
        db.session.commit()

        return jsonify({
            'id': new_item.id,
            'name': new_item.name,
            'description': new_item.description,
            'price': new_item.price
        }), 201
    except Exception as e:
        return jsonify({'error': 'Failed to add item', 'details': str(e)}), 500

@app.route('/wishlist/<int:item_id>', methods=['PUT'])
def update_wishlist_item(item_id):
    """
    Update an existing wishlist item by ID.
    """
    try:
        item = WishlistItem.query.get(item_id)
        if not item:
            return jsonify({'error': 'Item not found'}), 404

        data = request.get_json()
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)

        db.session.commit()

        return jsonify({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price
        }), 200
    except Exception as e:
        return jsonify({'error': 'Failed to update item', 'details': str(e)}), 500

@app.route('/wishlist/<int:item_id>', methods=['DELETE'])
def delete_wishlist_item(item_id):
    """
    Delete a wishlist item by ID.
    """
    try:
        item = WishlistItem.query.get(item_id)
        if not item:
            return jsonify({'error': 'Item not found'}), 404

        db.session.delete(item)
        db.session.commit()

        return jsonify({'message': 'Item deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to delete item', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
