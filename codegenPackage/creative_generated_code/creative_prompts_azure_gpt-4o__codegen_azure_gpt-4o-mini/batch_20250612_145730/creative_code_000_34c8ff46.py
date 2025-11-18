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
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database (for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeopathic_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a model for Product Categories
class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        """Convert the ProductCategory instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/categories', methods=['GET'])
def get_categories():
    """Retrieve all product categories."""
    categories = ProductCategory.query.all()
    return jsonify([category.to_dict() for category in categories]), 200

@app.route('/categories', methods=['POST'])
def create_category():
    """Create a new product category."""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Category name is required'}), 400

    new_category = ProductCategory(name=data['name'])
    
    try:
        db.session.add(new_category)
        db.session.commit()
        return jsonify(new_category.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Category already exists'}), 400

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Retrieve a specific product category by ID."""
    category = ProductCategory.query.get_or_404(category_id)
    return jsonify(category.to_dict()), 200

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Update an existing product category."""
    category = ProductCategory.query.get_or_404(category_id)
    data = request.get_json()
    
    if data and 'name' in data:
        category.name = data['name']
        
        try:
            db.session.commit()
            return jsonify(category.to_dict()), 200
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Category already exists'}), 400
    
    return jsonify({'error': 'Invalid input'}), 400

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Delete a product category."""
    category = ProductCategory.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
