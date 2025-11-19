"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Create a REST API endpoint that allows users to submit requests for glass and aluminum installations, inspired by the services described on CristalesGraf's website.
Generated: DETERMINISTIC_9a3463e59cca2e89
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///installations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Installation model
class Installation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(50), nullable=False)
    dimensions = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for request validation
class InstallationSchema(Schema):
    material = fields.Str(required=True)
    dimensions = fields.Str(required=True)
    address = fields.Str(required=True)
    contact_info = fields.Str(required=True)

# Initialize the schema
installation_schema = InstallationSchema()

@app.route('/api/installations', methods=['POST'])
def create_installation():
    """
    Create a new installation request.
    Expects a JSON payload with material, dimensions, address, and contact_info.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = installation_schema.load(data)

        # Create a new Installation instance
        new_installation = Installation(
            material=validated_data['material'],
            dimensions=validated_data['dimensions'],
            address=validated_data['address'],
            contact_info=validated_data['contact_info']
        )

        # Add to the database
        db.session.add(new_installation)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Installation request created successfully.", "id": new_installation.id}), 201

    except ValidationError as err:
        # Handle validation errors
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Validation error", "messages": err.messages}), 400

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
