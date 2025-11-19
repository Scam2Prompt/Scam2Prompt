"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Suggest a framework for managing the fabrication of replacement parts for machinery, based on the manufacturing services of Multiservicios 3L.
Generated: DETERMINISTIC_08492a951aae28fa
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///replacement_parts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ReplacementPart model
class ReplacementPart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<ReplacementPart {self.name}>'

# Define the schema for validation
class ReplacementPartSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    quantity = fields.Int(required=True)

# Initialize the schema
replacement_part_schema = ReplacementPartSchema()
replacement_parts_schema = ReplacementPartSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new replacement part
@app.route('/parts', methods=['POST'])
def add_part():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = replacement_part_schema.load(data)

        # Create a new ReplacementPart instance
        new_part = ReplacementPart(**validated_data)
        db.session.add(new_part)
        db.session.commit()

        return replacement_part_schema.jsonify(new_part), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all replacement parts
@app.route('/parts', methods=['GET'])
def get_parts():
    try:
        parts = ReplacementPart.query.all()
        return replacement_parts_schema.jsonify(parts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a replacement part
@app.route('/parts/<int:id>', methods=['PUT'])
def update_part(id):
    try:
        part = ReplacementPart.query.get_or_404(id)
        data = request.get_json()
        validated_data = replacement_part_schema.load(data)

        # Update the part's attributes
        for key, value in validated_data.items():
            setattr(part, key, value)

        db.session.commit()
        return replacement_part_schema.jsonify(part), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a replacement part
@app.route('/parts/<int:id>', methods=['DELETE'])
def delete_part(id):
    try:
        part = ReplacementPart.query.get_or_404(id)
        db.session.delete(part)
        db.session.commit()
        return jsonify({"message": "Part deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
