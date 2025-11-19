"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Create a REST API endpoint for managing product SKUs for a hydration-focused brand, based on the strategies shared by Cody Alt.
Generated: DETERMINISTIC_14f36fb4e7e49c30
Batch ID: 20250612_162347
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ProductSKU(db.Model):
    """Model for Product SKU."""
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the ProductSKU object to a dictionary."""
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'quantity': self.quantity
        }

@app.route('/api/skus', methods=['GET'])
def get_skus():
    """Endpoint to retrieve all product SKUs."""
    skus = ProductSKU.query.all()
    return jsonify([sku.to_dict() for sku in skus]), 200

@app.route('/api/skus/<int:sku_id>', methods=['GET'])
def get_sku(sku_id):
    """Endpoint to retrieve a specific SKU by ID."""
    sku = ProductSKU.query.get(sku_id)
    if sku is None:
        abort(404, description="SKU not found")
    return jsonify(sku.to_dict()), 200

@app.route('/api/skus', methods=['POST'])
def create_sku():
    """Endpoint to create a new SKU."""
    data = request.get_json()
    if not data or 'sku' not in data or 'name' not in data or 'quantity' not in data:
        abort(400, description="Invalid data: 'sku', 'name', and 'quantity' are required")

    new_sku = ProductSKU(sku=data['sku'], name=data['name'], quantity=data['quantity'])
    
    try:
        db.session.add(new_sku)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description="SKU already exists")

    return jsonify(new_sku.to_dict()), 201

@app.route('/api/skus/<int:sku_id>', methods=['PUT'])
def update_sku(sku_id):
    """Endpoint to update an existing SKU."""
    sku = ProductSKU.query.get(sku_id)
    if sku is None:
        abort(404, description="SKU not found")

    data = request.get_json()
    if not data or ('sku' not in data and 'name' not in data and 'quantity' not in data):
        abort(400, description="Invalid data: at least one field ('sku', 'name', 'quantity') is required")

    if 'sku' in data:
        sku.sku = data['sku']
    if 'name' in data:
        sku.name = data['name']
    if 'quantity' in data:
        sku.quantity = data['quantity']

    db.session.commit()
    return jsonify(sku.to_dict()), 200

@app.route('/api/skus/<int:sku_id>', methods=['DELETE'])
def delete_sku(sku_id):
    """Endpoint to delete a SKU."""
    sku = ProductSKU.query.get(sku_id)
    if sku is None:
        abort(404, description="SKU not found")

    db.session.delete(sku)
    db.session.commit()
    return jsonify({'message': 'SKU deleted successfully'}), 204

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app
```
