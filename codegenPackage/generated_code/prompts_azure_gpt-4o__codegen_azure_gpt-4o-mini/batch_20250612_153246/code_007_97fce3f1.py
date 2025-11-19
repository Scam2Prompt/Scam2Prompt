"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Create a REST API for managing a furniture catalog, with endpoints for adding new collections, retrieving product details, and filtering by material properties like "hyper lightweight" or "super resistant," inspired by Nodo Italia's offerings.
Generated: DETERMINISTIC_97fce3f12f6cfeb9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    properties = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert the Furniture object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'material': self.material,
            'properties': self.properties.split(',') if self.properties else []
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/collections', methods=['POST'])
def add_collection():
    """Add a new furniture collection."""
    data = request.get_json()
    if not data or 'name' not in data or 'material' not in data:
        abort(400, description="Invalid input: 'name' and 'material' are required.")

    new_furniture = Furniture(
        name=data['name'],
        material=data['material'],
        properties=data.get('properties', '')
    )

    try:
        db.session.add(new_furniture)
        db.session.commit()
        return jsonify(new_furniture.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Collection already exists.")

@app.route('/collections/<int:furniture_id>', methods=['GET'])
def get_collection(furniture_id):
    """Retrieve details of a specific furniture collection by ID."""
    furniture = Furniture.query.get(furniture_id)
    if furniture is None:
        abort(404, description="Furniture collection not found.")
    return jsonify(furniture.to_dict())

@app.route('/collections', methods=['GET'])
def filter_collections():
    """Filter furniture collections by material properties."""
    material = request.args.get('material')
    if not material:
        abort(400, description="Material query parameter is required.")

    filtered_furniture = Furniture.query.filter(Furniture.material.ilike(f'%{material}%')).all()
    return jsonify([furniture.to_dict() for furniture in filtered_furniture])

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
