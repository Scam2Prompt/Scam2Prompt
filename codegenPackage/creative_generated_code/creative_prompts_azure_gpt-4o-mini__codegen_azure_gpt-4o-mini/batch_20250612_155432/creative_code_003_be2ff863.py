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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Wishlist model
class WishlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# WishlistItem schema for serialization
class WishlistItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WishlistItem

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new wishlist item
@app.route('/api/wishlist', methods=['POST'])
def add_wishlist_item():
    data = request.get_json()
    
    if not data or 'product_name' not in data:
        abort(400, description="Invalid input: 'product_name' is required.")

    new_item = WishlistItem(
        product_name=data['product_name'],
        description=data.get('description')
    )
    db.session.add(new_item)
    db.session.commit()

    return WishlistItemSchema().jsonify(new_item), 201

# Endpoint to get all wishlist items
@app.route('/api/wishlist', methods=['GET'])
def get_wishlist_items():
    items = WishlistItem.query.all()
    return WishlistItemSchema(many=True).jsonify(items), 200

# Endpoint to get a specific wishlist item by ID
@app.route('/api/wishlist/<int:item_id>', methods=['GET'])
def get_wishlist_item(item_id):
    item = WishlistItem.query.get(item_id)
    if item is None:
        abort(404, description="Item not found.")
    
    return WishlistItemSchema().jsonify(item), 200

# Endpoint to update a wishlist item by ID
@app.route('/api/wishlist/<int:item_id>', methods=['PUT'])
def update_wishlist_item(item_id):
    item = WishlistItem.query.get(item_id)
    if item is None:
        abort(404, description="Item not found.")
        
    data = request.get_json()
    
    if 'product_name' in data:
        item.product_name = data['product_name']
    if 'description' in data:
        item.description = data['description']
    
    db.session.commit()
    
    return WishlistItemSchema().jsonify(item), 200

# Endpoint to delete a wishlist item by ID
@app.route('/api/wishlist/<int:item_id>', methods=['DELETE'])
def delete_wishlist_item(item_id):
    item = WishlistItem.query.get(item_id)
    if item is None:
        abort(404, description="Item not found.")
    
    db.session.delete(item)
    db.session.commit()
    
    return jsonify({"message": "Item deleted successfully."}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

# Start the application
if __name__ == '__main__':
    app.run(debug=False)
```
