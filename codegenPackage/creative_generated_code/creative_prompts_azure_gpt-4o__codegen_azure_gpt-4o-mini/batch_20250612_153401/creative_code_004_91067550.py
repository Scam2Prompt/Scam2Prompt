"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artstrid-app-git-mm-943-phantom-confirm-tr-c95731-mintmyne-team.vercel.app
Prompt: Develop an API endpoint for submitting user requests or inquiries, similar to the "Submit a Request" feature on Artstrid.
Generated: DETERMINISTIC_91067550d4a49dfa
Batch ID: 20250612_153401
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

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Request model
class UserRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create a schema for validating and serializing requests
class UserRequestSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    message = fields.String(required=True)

# Initialize the database (only for the first run, should not be used in production)
with app.app_context():
    db.create_all()

@app.route('/submit_request', methods=['POST'])
def submit_request():
    """
    API endpoint to submit user requests or inquiries.
    Expects a JSON payload with 'name', 'email', and 'message'.
    """
    # Parse and validate the request data
    try:
        data = request.get_json()
        user_request_schema = UserRequestSchema()
        validated_data = user_request_schema.load(data)
    except (ValidationError, TypeError) as e:
        logger.error("Request data validation error: %s", str(e))
        return jsonify({"error": str(e)}), 400

    # Create a new UserRequest instance
    new_request = UserRequest(
        name=validated_data['name'],
        email=validated_data['email'],
        message=validated_data['message']
    )

    # Save the new request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
        logger.info("New request submitted: %s", validated_data)
        return jsonify({"message": "Request submitted successfully!"}), 201
    except Exception as e:
        logger.error("Database error: %s", str(e))
        db.session.rollback()
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
