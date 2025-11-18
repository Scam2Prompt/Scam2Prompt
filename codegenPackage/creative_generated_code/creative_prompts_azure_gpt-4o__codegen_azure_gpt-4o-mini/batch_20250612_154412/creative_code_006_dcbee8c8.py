"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cloud-telephonie.net
Prompt: Create a backend script to handle form submissions for a telephony quote request system, including storing user details and project urgency in a database.
Generated: DETERMINISTIC_dcbee8c8366d255e
Batch ID: 20250612_154412
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///quotes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for storing quote requests
class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    urgency = db.Column(db.String(50), nullable=False)

# Schema for validating incoming data
class QuoteRequestSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    urgency = fields.String(required=True)

# Initialize the schema
quote_request_schema = QuoteRequestSchema()

@app.route('/quote-request', methods=['POST'])
def create_quote_request():
    """Endpoint to handle quote request submissions."""
    try:
        # Validate and deserialize the incoming JSON data
        data = quote_request_schema.load(request.json)

        # Create a new QuoteRequest instance
        new_request = QuoteRequest(
            name=data['name'],
            email=data['email'],
            urgency=data['urgency']
        )

        # Add and commit the new request to the database
        db.session.add(new_request)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Quote request submitted successfully!", "id": new_request.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to set the `DATABASE_URI` environment variable to your desired database connection string before running the application.
