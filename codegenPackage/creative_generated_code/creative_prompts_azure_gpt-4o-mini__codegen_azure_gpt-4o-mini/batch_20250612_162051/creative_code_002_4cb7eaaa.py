"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Create a REST API endpoint that enables users to submit property details for title insurance inquiries at Superior Title Montana.
Generated: DETERMINISTIC_4cb7eaaa85b42266
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100), nullable=False)
    property_address = db.Column(db.String(255), nullable=False)
    property_value = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Define schema for validation
class PropertySchema(Schema):
    owner_name = fields.Str(required=True)
    property_address = fields.Str(required=True)
    property_value = fields.Float(required=True)

property_schema = PropertySchema()

# API endpoint to submit property details
@app.route('/api/properties', methods=['POST'])
def submit_property():
    try:
        # Validate and deserialize incoming JSON data
        data = request.get_json()
        logger.info(f"Received data: {data}")
        validated_data = property_schema.load(data)

        # Create a new Property instance
        new_property = Property(
            owner_name=validated_data['owner_name'],
            property_address=validated_data['property_address'],
            property_value=validated_data['property_value']
        )

        # Add to the database
        db.session.add(new_property)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Property submitted successfully!", "id": new_property.id}), 201

    except ValidationError as err:
        logger.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400
    except Exception as e:
        logger.exception("An error occurred while submitting property details.")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
