"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Suggest a REST API structure for managing furniture inventory for a store like Navkar Furniture, including endpoints for categories like almirahs and dining tables.
Generated: DETERMINISTIC_eec17f533cf2184d
Batch ID: 20250612_162051
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    """Model representing a furniture category."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class FurnitureItem(db.Model):
    """Model representing a furniture item."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

    category = db.relationship('Category', backref=db.backref('furniture_items', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category_id": self.category_id,
            "price": self.price
        }


@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()


@app.route('/categories', methods=['GET'])
def get_categories():
    """Retrieve all furniture categories."""
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])


@app.route('/categories', methods=['POST'])
def create_category():
    """Create a new furniture category."""
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Invalid input: 'name' is required.")
    
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.to_dict()), 201


@app.route('/furniture', methods=['GET'])
def get_furniture_items():
    """Retrieve all furniture items."""
    furniture_items = FurnitureItem.query.all()
    return jsonify([item.to_dict() for item in furniture_items])


@app.route('/furniture', methods=['POST'])
def create_furniture_item():
    """Create a new furniture item."""
    data = request.get_json()
    if not data or 'name' not in data or 'category_id' not in data or 'price' not in data:
        abort(400, description="Invalid input: 'name', 'category_id', and 'price' are required.")
    
    new_item = FurnitureItem(name=data['name'], category_id=data['category_id'], price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201


@app.route('/furniture/<int:item_id>', methods=['GET'])
def get_furniture_item(item_id):
    """Retrieve a specific furniture item by ID."""
    item = FurnitureItem.query.get_or_404(item_id)
    return jsonify(item.to_dict())


@app.route('/furniture/<int:item_id>', methods=['PUT'])
def update_furniture_item(item_id):
    """Update a specific furniture item."""
    item = FurnitureItem.query.get_or_404(item_id)
    data = request.get_json()
    
    if 'name' in data:
        item.name = data['name']
    if 'category_id' in data:
        item.category_id = data['category_id']
    if 'price' in data:
        item.price = data['price']

    db.session.commit()
    return jsonify(item.to_dict())


@app.route('/furniture/<int:item_id>', methods=['DELETE'])
def delete_furniture_item(item_id):
    """Delete a specific furniture item."""
    item = FurnitureItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully."}), 204


if __name__ == '__main__':
    app.run(debug=True)
```
