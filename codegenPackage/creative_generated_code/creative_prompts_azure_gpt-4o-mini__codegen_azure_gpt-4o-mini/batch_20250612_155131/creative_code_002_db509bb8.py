"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Create an API endpoint that enables users to request legal and financial advice for debt management, reflecting the services described on the Arbitum Consulting website.
Generated: DETERMINISTIC_db509bb8f1487408
Batch ID: 20250612_155131
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advice_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database model for advice requests
class AdviceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    request_type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Schema for validating incoming requests
class AdviceRequestSchema(Schema):
    user_name = fields.Str(required=True)
    email = fields.Email(required=True)
    request_type = fields.Str(required=True, validate=lambda s: s in ["legal", "financial"])
    message = fields.Str(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/advice-request', methods=['POST'])
def request_advice():
    """
    API endpoint to request legal or financial advice for debt management.
    """
    try:
        # Validate and parse incoming JSON data
        schema = AdviceRequestSchema()
        data = schema.load(request.json)

        # Create a new advice request
        advice_request = AdviceRequest(
            user_name=data['user_name'],
            email=data['email'],
            request_type=data['request_type'],
            message=data['message']
        )

        # Save the request to the database
        db.session.add(advice_request)
        db.session.commit()

        # Log the successful request
        logger.info(f"Advice request submitted: {advice_request.id}")

        return jsonify({"message": "Advice request submitted successfully.", "id": advice_request.id}), 201

    except ValidationError as err:
        logger.error(f"Validation error: {err.messages}")
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        logger.exception("An error occurred while processing the request")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
