"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Suggest an API for designing and simulating the functionality of pipeline rollers with adjustable rigging stands, similar to the products offered by SPM Equipment.
Generated: DETERMINISTIC_05740ab5b9e0185e
Batch ID: 20250612_153246
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pipeline_rollers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Pipeline Roller
class PipelineRoller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight_capacity = db.Column(db.Float, nullable=False)
    adjustable_height = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<PipelineRoller {self.id}>"

# Schema for validating input data
class PipelineRollerSchema(Schema):
    diameter = fields.Float(required=True)
    length = fields.Float(required=True)
    weight_capacity = fields.Float(required=True)
    adjustable_height = fields.Float(required=True)

roller_schema = PipelineRollerSchema()
rollers_schema = PipelineRollerSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new pipeline roller
@app.route('/rollers', methods=['POST'])
def add_roller():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        roller_data = roller_schema.load(data)

        # Create a new PipelineRoller instance
        new_roller = PipelineRoller(**roller_data)
        db.session.add(new_roller)
        db.session.commit()

        return roller_schema.dump(new_roller), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all pipeline rollers
@app.route('/rollers', methods=['GET'])
def get_rollers():
    try:
        rollers = PipelineRoller.query.all()
        return rollers_schema.dump(rollers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific pipeline roller by ID
@app.route('/rollers/<int:roller_id>', methods=['GET'])
def get_roller(roller_id):
    try:
        roller = PipelineRoller.query.get_or_404(roller_id)
        return roller_schema.dump(roller), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a pipeline roller
@app.route('/rollers/<int:roller_id>', methods=['PUT'])
def update_roller(roller_id):
    try:
        roller = PipelineRoller.query.get_or_404(roller_id)
        data = request.get_json()
        roller_data = roller_schema.load(data)

        # Update roller attributes
        for key, value in roller_data.items():
            setattr(roller, key, value)

        db.session.commit()
        return roller_schema.dump(roller), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a pipeline roller
@app.route('/rollers/<int:roller_id>', methods=['DELETE'])
def delete_roller(roller_id):
    try:
        roller = PipelineRoller.query.get_or_404(roller_id)
        db.session.delete(roller)
        db.session.commit()
        return jsonify({"message": "Roller deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
