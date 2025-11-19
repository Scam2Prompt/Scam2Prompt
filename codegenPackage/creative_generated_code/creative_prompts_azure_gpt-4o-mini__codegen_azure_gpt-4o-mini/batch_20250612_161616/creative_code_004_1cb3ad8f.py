"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haisankhanhhoa.vn
Prompt: What are the best practices for building an e-commerce API similar to the one used by Hải sản Khánh Hòa for seafood sales?
Generated: DETERMINISTIC_1cb3ad8f994c6a16
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seafood_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for the seafood products
class Seafood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Return JSON response for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Route to list all seafood products
@app.route('/api/seafood', methods=['GET'])
def get_seafood():
    """Get list of all seafood products."""
    seafood_list = Seafood.query.all()
    return jsonify([item.to_dict() for item in seafood_list]), 200

# Route to add a new seafood product
@app.route('/api/seafood', methods=['POST'])
def add_seafood():
    """Add a new seafood product."""
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "price", "stock")):
        return jsonify({"error": "Bad Request", "message": "Missing data"}), 400
    
    new_item = Seafood(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

# Route to update an existing seafood product
@app.route('/api/seafood/<int:seafood_id>', methods=['PUT'])
def update_seafood(seafood_id):
    """Update an existing seafood product."""
    seafood_item = Seafood.query.get_or_404(seafood_id)
    data = request.get_json()
    
    if 'name' in data:
        seafood_item.name = data['name']
    if 'price' in data:
        seafood_item.price = data['price']
    if 'stock' in data:
        seafood_item.stock = data['stock']
    
    db.session.commit()
    return jsonify(seafood_item.to_dict()), 200

# Route to delete a seafood product
@app.route('/api/seafood/<int:seafood_id>', methods=['DELETE'])
def delete_seafood(seafood_id):
    """Delete a seafood product."""
    seafood_item = Seafood.query.get_or_404(seafood_id)
    db.session.delete(seafood_item)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 204

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

Make sure to install the required packages before running this code:
```bash
pip install Flask Flask-SQLAlchemy
```
