"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Build a REST API that provides information on Medicare Supplement Insurance, including worldwide coverage and maximum out-of-pocket costs.
Generated: DETERMINISTIC_e6459f47590ef6d6
Batch ID: 20250612_154942
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
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)

# Configuration for the SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicare_supplement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Medicare Supplement Insurance
class MedicareSupplement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    worldwide_coverage = db.Column(db.Boolean, nullable=False)
    max_out_of_pocket = db.Column(db.Float, nullable=False)

# Schema for serializing Medicare Supplement data
class MedicareSupplementSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    worldwide_coverage = fields.Bool(required=True)
    max_out_of_pocket = fields.Float(required=True)

medicare_schema = MedicareSupplementSchema()
medicare_list_schema = MedicareSupplementSchema(many=True)

@app.route('/api/medicare_supplements', methods=['POST'])
def add_medicare_supplement():
    """Add a new Medicare Supplement Insurance entry."""
    try:
        # Validate and deserialize input
        new_supplement = medicare_schema.load(request.json)
        supplement = MedicareSupplement(**new_supplement)
        db.session.add(supplement)
        db.session.commit()
        return medicare_schema.jsonify(supplement), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/medicare_supplements', methods=['GET'])
def get_medicare_supplements():
    """Retrieve all Medicare Supplement Insurance entries."""
    supplements = MedicareSupplement.query.all()
    return medicare_list_schema.jsonify(supplements), 200

@app.route('/api/medicare_supplements/<int:id>', methods=['GET'])
def get_medicare_supplement(id):
    """Retrieve a specific Medicare Supplement Insurance entry by ID."""
    supplement = MedicareSupplement.query.get_or_404(id)
    return medicare_schema.jsonify(supplement), 200

@app.route('/api/medicare_supplements/<int:id>', methods=['PUT'])
def update_medicare_supplement(id):
    """Update a specific Medicare Supplement Insurance entry."""
    supplement = MedicareSupplement.query.get_or_404(id)
    try:
        updated_data = medicare_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(supplement, key, value)
        db.session.commit()
        return medicare_schema.jsonify(supplement), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/medicare_supplements/<int:id>', methods=['DELETE'])
def delete_medicare_supplement(id):
    """Delete a specific Medicare Supplement Insurance entry."""
    supplement = MedicareSupplement.query.get_or_404(id)
    db.session.delete(supplement)
    db.session.commit()
    return jsonify({"message": "Supplement deleted successfully."}), 204

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

This Flask application provides a REST API with endpoints to create, retrieve, update, and delete Medicare Supplement Insurance entries, along with proper error handling and data validation.
