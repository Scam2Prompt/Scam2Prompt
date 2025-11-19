"""
Generated Code Metadata:
========================
Original URL: https://ccjourney.co
Prompt: Illustrate how to implement a pre-order system in a web application for fashion collections, inspired by the Capsule Cosmic Journey's pre-order offerings.
Generated: DETERMINISTIC_aa2de9f840b37e4f
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///preorders.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    preorders = db.relationship('PreOrder', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Collection(db.Model):
    __tablename__ = 'collections'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    launch_date = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    items = db.relationship('CollectionItem', backref='collection', lazy=True)

class CollectionItem(db.Model):
    __tablename__ = 'collection_items'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    collection_id = db.Column(db.String(36), db.ForeignKey('collections.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))
    stock = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PreOrder(db.Model):
    __tablename__ = 'preorders'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.String(36), db.ForeignKey('collection_items.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, shipped, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    item = db.relationship('CollectionItem', backref='preorders')

# Helper functions
def validate_pre_order_data(data):
    required_fields = ['item_id', 'quantity']
    for field in required_fields:
        if field not in data:
            return False
    return True

# API Routes
@app.route('/api/collections', methods=['GET'])
def get_collections():
    """Get all active collections"""
    collections = Collection.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': collection.id,
        'name': collection.name,
        'description': collection.description,
        'launch_date': collection.launch_date.isoformat(),
        'items_count': len(collection.items)
    } for collection in collections])

@app.route('/api/collections/<collection_id>/items', methods=['GET'])
def get_collection_items(collection_id):
    """Get all items in a specific collection"""
    collection = Collection.query.get_or_404(collection_id)
    items = CollectionItem.query.filter_by(collection_id=collection_id).all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
        'image_url': item.image_url,
        'stock': item.stock
    } for item in items])

@app.route('/api/preorders', methods=['POST'])
def create_pre_order():
    """Create a new pre-order"""
    # In a real application, you would authenticate the user first
    data = request.get_json()
    
    if not validate_pre_order_data(data):
        abort(400, description="Invalid pre-order data")
    
    item = CollectionItem.query.get(data['item_id'])
    if not item:
        abort(404, description="Item not found")
    
    if item.stock < data['quantity']:
        abort(400, description="Not enough stock available")
    
    # In a real app, you'd get user_id from the authenticated session
    user_id = "demo-user-id"  # Placeholder for demo
    
    pre_order = PreOrder(
        user_id=user_id,
        item_id=item.id,
        quantity=data['quantity']
    )
    
    try:
        db.session.add(pre_order)
        db.session.commit()
        
        # Update stock (in a real app, you might want to reserve stock instead)
        item.stock -= data['quantity']
        db.session.commit()
        
        return jsonify({
            'id': pre_order.id,
            'item_id': pre_order.item_id,
            'quantity': pre_order.quantity,
            'status': pre_order.status,
            'created_at': pre_order.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        abort(500, description="Failed to create pre-order")

@app.route('/api/preorders/<preorder_id>', methods=['GET'])
def get_pre_order(preorder_id):
    """Get details of a specific pre-order"""
    pre_order = PreOrder.query.get_or_404(preorder_id)
    return jsonify({
        'id': pre_order.id,
        'item': {
            'id': pre_order.item.id,
            'name': pre_order.item.name,
            'price': pre_order.item.price
        },
        'quantity': pre_order.quantity,
        'status': pre_order.status,
        'created_at': pre_order.created_at.isoformat(),
        'updated_at': pre_order.updated_at.isoformat()
    })

@app.route('/api/preorders/<preorder_id>', methods=['PUT'])
def update_pre_order(preorder_id):
    """Update a pre-order (e.g., change quantity or cancel)"""
    pre_order = PreOrder.query.get_or_404(preorder_id)
    data = request.get_json()
    
    if 'quantity' in data:
        # Handle quantity changes
        delta = data['quantity'] - pre_order.quantity
        if pre_order.item.stock < delta:
            abort(400, description="Not enough stock available")
        
        pre_order.item.stock -= delta
        pre_order.quantity = data['quantity']
    
    if 'status' in data and data['status'] == 'cancelled':
        # Handle cancellation
        pre_order.item.stock += pre_order.quantity
        pre_order.status = 'cancelled'
    
    try:
        db.session.commit()
        return jsonify({
            'id': pre_order.id,
            'status': pre_order.status,
            'quantity': pre_order.quantity,
            'updated_at': pre_order.updated_at.isoformat()
        })
    except Exception as e:
        db.session.rollback()
        abort(500, description="Failed to update pre-order")

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
