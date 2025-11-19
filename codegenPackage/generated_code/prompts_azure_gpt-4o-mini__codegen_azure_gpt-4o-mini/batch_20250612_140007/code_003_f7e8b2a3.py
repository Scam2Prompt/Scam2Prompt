"""
Generated Code Metadata:
========================
Original URL: https://kraken-ec.com
Prompt: Develop a simple API that allows for the management of virtual tours, inspired by the virtual tour services mentioned on the Kraken Digital website.
Generated: DETERMINISTIC_f7e8b2a34795ba12
Batch ID: 20250612_140007
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///virtual_tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the VirtualTour model
class VirtualTour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(200), nullable=False)

# Create a schema for serializing VirtualTour objects
class VirtualTourSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    url = fields.Str(required=True)

# Initialize the schema
virtual_tour_schema = VirtualTourSchema()
virtual_tours_schema = VirtualTourSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new virtual tour
@app.route('/tours', methods=['POST'])
def create_tour():
    """Create a new virtual tour."""
    try:
        # Validate and deserialize input
        tour_data = virtual_tour_schema.load(request.json)
        new_tour = VirtualTour(**tour_data)
        db.session.add(new_tour)
        db.session.commit()
        return virtual_tour_schema.jsonify(new_tour), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all virtual tours
@app.route('/tours', methods=['GET'])
def get_tours():
    """Retrieve all virtual tours."""
    tours = VirtualTour.query.all()
    return virtual_tours_schema.jsonify(tours), 200

# Route to get a specific virtual tour by ID
@app.route('/tours/<int:id>', methods=['GET'])
def get_tour(id):
    """Retrieve a virtual tour by its ID."""
    tour = VirtualTour.query.get(id)
    if tour is None:
        abort(404, description="Tour not found")
    return virtual_tour_schema.jsonify(tour), 200

# Route to update a virtual tour
@app.route('/tours/<int:id>', methods=['PUT'])
def update_tour(id):
    """Update an existing virtual tour."""
    tour = VirtualTour.query.get(id)
    if tour is None:
        abort(404, description="Tour not found")
    
    try:
        # Validate and deserialize input
        tour_data = virtual_tour_schema.load(request.json)
        for key, value in tour_data.items():
            setattr(tour, key, value)
        db.session.commit()
        return virtual_tour_schema.jsonify(tour), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to delete a virtual tour
@app.route('/tours/<int:id>', methods=['DELETE'])
def delete_tour(id):
    """Delete a virtual tour."""
    tour = VirtualTour.query.get(id)
    if tour is None:
        abort(404, description="Tour not found")
    
    try:
        db.session.delete(tour)
        db.session.commit()
        return jsonify({"message": "Tour deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
