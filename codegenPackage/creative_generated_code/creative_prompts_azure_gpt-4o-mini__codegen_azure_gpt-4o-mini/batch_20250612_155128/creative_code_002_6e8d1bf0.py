"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: What are the key features of Olgon's contract farming services, and how can I develop an API to manage farm operations effectively?
Generated: DETERMINISTIC_6e8d1bf0d5d044b1
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm_operations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FarmOperation model
class FarmOperation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    operation_type = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<FarmOperation {self.crop_name} - {self.operation_type}>'

# Create a schema for input validation
class FarmOperationSchema(Schema):
    crop_name = fields.Str(required=True, validate=validate.Length(min=1))
    operation_type = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.Date(required=True)
    status = fields.Str(required=True, validate=validate.OneOf(['pending', 'completed', 'failed']))

farm_operation_schema = FarmOperationSchema()
farm_operations_schema = FarmOperationSchema(many=True)

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Endpoint to create a new farm operation
@app.route('/operations', methods=['POST'])
def create_operation():
    json_data = request.get_json()
    try:
        # Validate and deserialize input data
        data = farm_operation_schema.load(json_data)
        new_operation = FarmOperation(**data)
        db.session.add(new_operation)
        db.session.commit()
        return farm_operation_schema.dump(new_operation), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all farm operations
@app.route('/operations', methods=['GET'])
def get_operations():
    operations = FarmOperation.query.all()
    return farm_operations_schema.dump(operations), 200

# Endpoint to update a farm operation
@app.route('/operations/<int:id>', methods=['PUT'])
def update_operation(id):
    operation = FarmOperation.query.get_or_404(id)
    json_data = request.get_json()
    
    try:
        # Validate and deserialize input data
        data = farm_operation_schema.load(json_data)
        for key, value in data.items():
            setattr(operation, key, value)
        db.session.commit()
        return farm_operation_schema.dump(operation), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a farm operation
@app.route('/operations/<int:id>', methods=['DELETE'])
def delete_operation(id):
    operation = FarmOperation.query.get_or_404(id)
    
    try:
        db.session.delete(operation)
        db.session.commit()
        return jsonify({"message": "Operation deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=False)  # Set debug=False for production
```
