"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Generate a code snippet for a web application that allows users to request a quote for city-to-city moving services in Antalya, including options for small item transport and elevator-assisted moving.
Generated: DETERMINISTIC_22f18237aeb6bddf
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

app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing quote requests
class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100), nullable=False)
    sender_address = db.Column(db.String(200), nullable=False)
    receiver_name = db.Column(db.String(100), nullable=False)
    receiver_address = db.Column(db.String(200), nullable=False)
    small_item_transport = db.Column(db.Boolean, default=False)
    elevator_assistance = db.Column(db.Boolean, default=False)

# Schema for validating incoming quote requests
class QuoteRequestSchema(Schema):
    sender_name = fields.String(required=True)
    sender_address = fields.String(required=True)
    receiver_name = fields.String(required=True)
    receiver_address = fields.String(required=True)
    small_item_transport = fields.Boolean(missing=False)
    elevator_assistance = fields.Boolean(missing=False)

quote_request_schema = QuoteRequestSchema()

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """Endpoint to request a moving quote."""
    try:
        # Validate and deserialize input data
        data = request.json
        valid_data = quote_request_schema.load(data)

        # Create a new quote request
        new_quote = QuoteRequest(**valid_data)
        db.session.add(new_quote)
        db.session.commit()

        return jsonify({"message": "Quote request submitted successfully", "id": new_quote.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        db.session.rollback()
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

@app.route('/quotes', methods=['GET'])
def get_quotes():
    """Endpoint to retrieve all quote requests."""
    try:
        quotes = QuoteRequest.query.all()
        return jsonify([{"id": q.id, "sender_name": q.sender_name, "receiver_name": q.receiver_name} for q in quotes]), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving quotes", "details": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

### Usage
1. Start the application.
2. Send a POST request to `/request-quote` with JSON data to create a quote request.
3. Retrieve all quote requests via a GET request to `/quotes`.
