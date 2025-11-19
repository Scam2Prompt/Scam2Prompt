"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Generate a code snippet for a web application that allows users to request transportation services for bulk cargo, referencing the types of cargo offered by OPC, such as liquid and dry cargo.
Generated: DETERMINISTIC_471a2a5e10df39e0
Batch ID: 20250612_161700
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transportation_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for transportation requests
class TransportationRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    client_name = db.Column(db.String(100), nullable=False)

# Schema for validating incoming requests
class TransportationRequestSchema(Schema):
    cargo_type = fields.String(required=True)
    quantity = fields.Float(required=True)
    client_name = fields.String(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/request-transportation', methods=['POST'])
def request_transportation():
    """Handle transportation requests for bulk cargo."""
    schema = TransportationRequestSchema()
    try:
        # Validate and deserialize the incoming request data
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create a new transportation request
    new_request = TransportationRequest(
        cargo_type=request_data['cargo_type'],
        quantity=request_data['quantity'],
        client_name=request_data['client_name']
    )

    # Add to the session and commit
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Transportation request submitted successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
