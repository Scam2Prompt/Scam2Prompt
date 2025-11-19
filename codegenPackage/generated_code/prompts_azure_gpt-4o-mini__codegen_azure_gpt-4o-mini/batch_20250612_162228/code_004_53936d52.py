"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: Design an API endpoint for an online store that allows users to submit custom costume design requests, inspired by the services offered by IceStyle.pl.
Generated: DETERMINISTIC_53936d5246b2789b
Batch ID: 20250612_162228
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///costume_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for costume design requests
class CostumeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Schema for validating input data
class CostumeRequestSchema(Schema):
    user_name = fields.Str(required=True)
    email = fields.Email(required=True)
    description = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit a custom costume design request
@app.route('/api/costume-requests', methods=['POST'])
def submit_costume_request():
    schema = CostumeRequestSchema()
    
    # Validate and deserialize input data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new costume request
    new_request = CostumeRequest(
        user_name=data['user_name'],
        email=data['email'],
        description=data['description']
    )

    # Add to the database and commit
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        logging.error(f"Error saving request: {e}")
        return jsonify({"error": "Failed to save request"}), 500

    # Return success response
    return jsonify({"message": "Costume request submitted successfully", "id": new_request.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
