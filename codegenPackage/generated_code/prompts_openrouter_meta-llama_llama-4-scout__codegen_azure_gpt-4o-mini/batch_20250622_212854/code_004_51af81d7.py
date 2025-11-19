"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Create a RESTful API endpoint to request a quote for a brick restoration project, including parameters for project location, building type, and required services like scaffolding and water repellent application."
Generated: DETERMINISTIC_51af81d7639ef9ab
Batch ID: 20250622_212854
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for quotes
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    building_type = db.Column(db.String(50), nullable=False)
    services = db.Column(db.String(200), nullable=False)

# Schema for validating incoming data
class QuoteSchema(Schema):
    location = fields.Str(required=True)
    building_type = fields.Str(required=True)
    services = fields.List(fields.Str(), required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/quotes', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for a brick restoration project.
    Expects JSON payload with location, building type, and services.
    """
    # Parse and validate incoming JSON data
    schema = QuoteSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new quote entry
    new_quote = Quote(
        location=data['location'],
        building_type=data['building_type'],
        services=', '.join(data['services'])
    )

    # Add the new quote to the database
    try:
        db.session.add(new_quote)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create quote", "details": str(e)}), 500

    # Return the created quote as a response
    return jsonify({
        "id": new_quote.id,
        "location": new_quote.location,
        "building_type": new_quote.building_type,
        "services": new_quote.services
    }), 201

if __name__ == '__main__':
    app.run(debug=False)
```
