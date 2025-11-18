"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Write Python code to create an e-commerce API for managing homeopathic product categories like "Pekana Drops," "Pekana Syrups," and "Pekana Granules," as described on the PEKANA.PK website.
Generated: DETERMINISTIC_34c8ff467e0d3c4a
Batch ID: 20250612_145730
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

# Initialize Flask app
app = Flask(__name__)

# Configure database (Using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeopathic_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the ProductCategory model
class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

# Create the database
with app.app_context():
    db.create_all()

# Routes for the ProductCategory API
@app.route('/api/categories', methods=['GET'])
def get_categories():
    """
    Retrieve all product categories.
    """
    categories = ProductCategory.query.all()
    return jsonify([category.to_dict() for category in categories])

@app.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """
    Retrieve a single product category by ID.
    """
    category = ProductCategory.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category.to_dict())

@app.route('/api/categories', methods=['POST'])
def create_category():
    """
    Create a new product category.
    """
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid input"}), 400
    if ProductCategory.query.filter_by(name=data['name']).first():
        return jsonify({"error": "Category with this name already exists"}), 400
    category = ProductCategory(name=data['name'], description=data.get('description'))
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict()), 201

@app.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """
    Update an existing product category.
    """
    category = ProductCategory.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    if 'name' in data:
        existing_category = ProductCategory.query.filter_by(name=data['name']).first()
        if existing_category and existing_category.id != category.id:
            return jsonify({"error": "Category with this name already exists"}), 400
        category.name = data['name']
    if 'description' in data:
        category.description = data['description']
    db.session.commit()
    return jsonify(category.to_dict())

@app.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """
    Delete a product category.
    """
    category = ProductCategory.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
