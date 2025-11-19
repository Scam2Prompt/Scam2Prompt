"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Develop an API for managing customer logistics requests, including air freight, road freight, and ocean freight, inspired by Fealty Worldwide's service categories.
Generated: DETERMINISTIC_5568961b33fb7f84
Batch ID: 20250612_151547
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the LogisticsRequest model
class LogisticsRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)  # air, road, ocean
    details = db.Column(db.String(200), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for request validation
class LogisticsRequestSchema(Schema):
    customer_name = fields.Str(required=True)
    service_type = fields.Str(required=True, validate=lambda s: s in ['air', 'road', 'ocean'])
    details = fields.Str(required=False)

# Initialize the schema
logistics_request_schema = LogisticsRequestSchema()

@app.route('/logistics', methods=['POST'])
def create_logistics_request():
    """Create a new logistics request."""
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = logistics_request_schema.load(data)

        # Create a new logistics request
        new_request = LogisticsRequest(**validated_data)
        db.session.add(new_request)
        db.session.commit()

        return jsonify({"message": "Logistics request created", "id": new_request.id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/logistics/<int:request_id>', methods=['GET'])
def get_logistics_request(request_id):
    """Retrieve a logistics request by ID."""
    request_data = LogisticsRequest.query.get(request_id)
    if request_data is None:
        return jsonify({"error": "Logistics request not found"}), 404

    return jsonify({
        "id": request_data.id,
        "customer_name": request_data.customer_name,
        "service_type": request_data.service_type,
        "details": request_data.details
    }), 200

@app.route('/logistics/<int:request_id>', methods=['PUT'])
def update_logistics_request(request_id):
    """Update an existing logistics request."""
    try:
        data = request.get_json()
        validated_data = logistics_request_schema.load(data)

        request_data = LogisticsRequest.query.get(request_id)
        if request_data is None:
            return jsonify({"error": "Logistics request not found"}), 404

        # Update the request with new data
        for key, value in validated_data.items():
            setattr(request_data, key, value)

        db.session.commit()
        return jsonify({"message": "Logistics request updated"}), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/logistics/<int:request_id>', methods=['DELETE'])
def delete_logistics_request(request_id):
    """Delete a logistics request by ID."""
    request_data = LogisticsRequest.query.get(request_id)
    if request_data is None:
        return jsonify({"error": "Logistics request not found"}), 404

    db.session.delete(request_data)
    db.session.commit()
    return jsonify({"message": "Logistics request deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
