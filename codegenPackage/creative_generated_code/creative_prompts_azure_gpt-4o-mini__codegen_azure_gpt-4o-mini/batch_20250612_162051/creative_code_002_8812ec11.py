"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Create an API endpoint for a logistics application that allows users to request clearing and forwarding services, similar to those provided by Olgadorks Shipping Company.
Generated: DETERMINISTIC_8812ec118ac59574
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Database model for Clearing and Forwarding requests
class ClearingForwardingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f"<Request {self.id} - {self.customer_name}>"

# Marshmallow schema for request validation
class ClearingForwardingRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    service_type = fields.Str(required=True)
    details = fields.Str()

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint for creating a clearing and forwarding request
@app.route('/api/requests', methods=['POST'])
def create_request():
    # Load and validate incoming JSON data
    schema = ClearingForwardingRequestSchema()
    try:
        request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Create new request instance
    new_request = ClearingForwardingRequest(
        customer_name=request_data['customer_name'],
        service_type=request_data['service_type'],
        details=request_data.get('details')
    )

    # Add the request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback on error
        return jsonify({"error": "Could not create request", "details": str(e)}), 500

    return jsonify({"message": "Request created successfully", "id": new_request.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
