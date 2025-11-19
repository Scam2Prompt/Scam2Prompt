"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Develop a RESTful API endpoint that allows users to submit their moving requirements and receive a tailored quote for Antalya's city moving services.
Generated: DETERMINISTIC_032919fa0da93407
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
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///moving_services.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for moving requests
class MovingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    moving_date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD format
    details = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<MovingRequest {self.name}>'

# Schema for input validation
class MovingRequestSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    moving_date = fields.Str(required=True)  # YYYY-MM-DD format
    details = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/moving-quote', methods=['POST'])
def get_moving_quote():
    """
    Endpoint to submit moving requirements and receive a tailored quote.
    Expects JSON payload with user details.
    """
    schema = MovingRequestSchema()
    
    # Validate input data
    try:
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new moving request
    new_request = MovingRequest(
        name=request_data['name'],
        address=request_data['address'],
        moving_date=request_data['moving_date'],
        details=request_data.get('details')
    )

    try:
        db.session.add(new_request)
        db.session.commit()
        # Simulated quote calculation logic
        quote = calculate_quote(request_data)
        return jsonify({"message": "Quote generated successfully", "quote": quote}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def calculate_quote(data):
    """
    Simulated quote calculation logic.
    This can be replaced with actual business logic based on moving requirements.
    """
    base_quote = 100  # Base quote in currency
    if "details" in data and data["details"]:
        additional_cost = len(data["details"].split()) * 10  # Example: $10 per additional detail word
        return base_quote + additional_cost
    return base_quote

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
