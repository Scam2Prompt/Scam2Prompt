"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write Python code to create an e-commerce API for managing sports equipment categories like "Beach Vôlei," "Basquete," and "Rugby," including features for adding, updating, and deleting items.
Generated: DETERMINISTIC_4564c5f68ec57bb4
Batch ID: 20250612_151414
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_equipment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class EquipmentCategory(db.Model):
    """Model representing a sports equipment category."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def serialize(self):
        """Serialize the category object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/categories', methods=['GET'])
def get_categories():
    """Retrieve all equipment categories."""
    categories = EquipmentCategory.query.all()
    return jsonify([category.serialize() for category in categories])

@app.route('/categories', methods=['POST'])
def add_category():
    """Add a new equipment category."""
    if not request.json or 'name' not in request.json:
        abort(400, 'Category name is required')
    
    new_category = EquipmentCategory(name=request.json['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.serialize()), 201

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Update an existing equipment category by ID."""
    category = EquipmentCategory.query.get_or_404(category_id)

    if not request.json or 'name' not in request.json:
        abort(400, 'Category name is required')
    
    category.name = request.json['name']
    db.session.commit()
    return jsonify(category.serialize())

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Delete an equipment category by ID."""
    category = EquipmentCategory.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
```
