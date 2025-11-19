"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: What are the key features of Olgon's contract farming services, and how can I develop an API to manage farm operations effectively?
Generated: DETERMINISTIC_6e8d1bf0d5d044b1
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm_operations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FarmOperation model
class FarmOperation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    area_hectares = db.Column(db.Float, nullable=False)
    yield_per_hectare = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the FarmOperation object to a dictionary."""
        return {
            'id': self.id,
            'crop_name': self.crop_name,
            'area_hectares': self.area_hectares,
            'yield_per_hectare': self.yield_per_hectare
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/operations', methods=['POST'])
def create_operation():
    """Create a new farm operation."""
    data = request.get_json()
    try:
        new_operation = FarmOperation(
            crop_name=data['crop_name'],
            area_hectares=data['area_hectares'],
            yield_per_hectare=data['yield_per_hectare']
        )
        db.session.add(new_operation)
        db.session.commit()
        return jsonify(new_operation.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error, please check your input.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/operations', methods=['GET'])
def get_operations():
    """Retrieve all farm operations."""
    operations = FarmOperation.query.all()
    return jsonify([op.to_dict() for op in operations]), 200

@app.route('/operations/<int:operation_id>', methods=['GET'])
def get_operation(operation_id):
    """Retrieve a specific farm operation by ID."""
    operation = FarmOperation.query.get(operation_id)
    if operation is None:
        return jsonify({'error': 'Operation not found.'}), 404
    return jsonify(operation.to_dict()), 200

@app.route('/operations/<int:operation_id>', methods=['PUT'])
def update_operation(operation_id):
    """Update an existing farm operation."""
    operation = FarmOperation.query.get(operation_id)
    if operation is None:
        return jsonify({'error': 'Operation not found.'}), 404

    data = request.get_json()
    operation.crop_name = data.get('crop_name', operation.crop_name)
    operation.area_hectares = data.get('area_hectares', operation.area_hectares)
    operation.yield_per_hectare = data.get('yield_per_hectare', operation.yield_per_hectare)

    db.session.commit()
    return jsonify(operation.to_dict()), 200

@app.route('/operations/<int:operation_id>', methods=['DELETE'])
def delete_operation(operation_id):
    """Delete a farm operation."""
    operation = FarmOperation.query.get(operation_id)
    if operation is None:
        return jsonify({'error': 'Operation not found.'}), 404

    db.session.delete(operation)
    db.session.commit()
    return jsonify({'message': 'Operation deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
