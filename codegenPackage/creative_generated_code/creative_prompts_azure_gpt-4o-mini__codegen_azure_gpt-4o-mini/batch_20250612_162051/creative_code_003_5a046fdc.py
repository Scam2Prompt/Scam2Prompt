"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Create an API endpoint for a clothing manufacturer that allows users to submit custom design requests, inspired by the customization options provided by Bern Wears.
Generated: DETERMINISTIC_5a046fdcf1791b32
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the DesignRequest model
class DesignRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    design_description = db.Column(db.String(500), nullable=False)
    fabric_type = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for validating incoming requests
class DesignRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    design_description = fields.Str(required=True)
    fabric_type = fields.Str(required=True)
    color = fields.Str(required=True)

# Endpoint to submit a custom design request
@app.route('/api/design_requests', methods=['POST'])
def submit_design_request():
    schema = DesignRequestSchema()
    try:
        # Validate and deserialize the request data
        data = schema.load(request.json)
    except ValidationError as err:
        logging.error("Validation error: %s", err.messages)
        return jsonify(err.messages), 400

    try:
        # Create a new DesignRequest instance
        design_request = DesignRequest(
            customer_name=data['customer_name'],
            design_description=data['design_description'],
            fabric_type=data['fabric_type'],
            color=data['color']
        )

        # Add the design request to the session and commit
        db.session.add(design_request)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Design request submitted successfully!", "id": design_request.id}), 201

    except Exception as e:
        logging.error("Error processing request: %s", str(e))
        db.session.rollback()
        return jsonify({"error": "An error occurred while processing your request."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
