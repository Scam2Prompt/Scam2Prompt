"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpl-liner.com
Prompt: Develop a REST API endpoint for managing custom brokerage requests, incorporating features mentioned on the MPL website.
Generated: DETERMINISTIC_19d0e76f210ed4f6
Batch ID: 20250612_161616
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Database configuration (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brokerage_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Brokerage Request Model
class BrokerageRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    request_description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='Pending')

# Schema for serializing responses
class BrokerageRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BrokerageRequest

# Create the database
with app.app_context():
    db.create_all()

# Endpoint to create a new brokerage request
@app.route('/api/brokerage-requests', methods=['POST'])
def create_brokerage_request():
    try:
        # Get data from the request
        data = request.get_json()
        if not data or 'client_name' not in data or 'request_description' not in data:
            raise BadRequest("Missing required fields: 'client_name' and 'request_description'.")

        # Create a new request
        new_request = BrokerageRequest(
            client_name=data['client_name'],
            request_description=data['request_description']
        )
        db.session.add(new_request)
        db.session.commit()

        # Return the created request as JSON
        return BrokerageRequestSchema().jsonify(new_request), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all brokerage requests
@app.route('/api/brokerage-requests', methods=['GET'])
def get_brokerage_requests():
    try:
        requests = BrokerageRequest.query.all()
        return BrokerageRequestSchema(many=True).jsonify(requests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get a specific brokerage request by ID
@app.route('/api/brokerage-requests/<int:id>', methods=['GET'])
def get_brokerage_request(id):
    try:
        request = BrokerageRequest.query.get_or_404(id)
        return BrokerageRequestSchema().jsonify(request), 200
    except NotFound:
        return jsonify({"error": "Brokerage request not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a brokerage request
@app.route('/api/brokerage-requests/<int:id>', methods=['PUT'])
def update_brokerage_request(id):
    try:
        request_data = request.get_json()
        request_to_update = BrokerageRequest.query.get_or_404(id)

        # Update fields if provided
        if 'client_name' in request_data:
            request_to_update.client_name = request_data['client_name']
        if 'request_description' in request_data:
            request_to_update.request_description = request_data['request_description']
        if 'status' in request_data:
            request_to_update.status = request_data['status']

        db.session.commit()
        return BrokerageRequestSchema().jsonify(request_to_update), 200

    except NotFound:
        return jsonify({"error": "Brokerage request not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a brokerage request
@app.route('/api/brokerage-requests/<int:id>', methods=['DELETE'])
def delete_brokerage_request(id):
    try:
        request_to_delete = BrokerageRequest.query.get_or_404(id)
        db.session.delete(request_to_delete)
        db.session.commit()
        return jsonify({"message": "Brokerage request deleted successfully."}), 204
    except NotFound:
        return jsonify({"error": "Brokerage request not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
