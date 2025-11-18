"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ircmhealth.com
Prompt: Create a REST API endpoint for submitting claims and tracking their status in a medical billing system, incorporating features similar to ircmhealth.com's RCM services.
Generated: DETERMINISTIC_6b77d1008fec6dd4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for claims (for demonstration purposes; use a database in production)
claims = {}

# Error handling utility
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response

# Endpoint to submit a new claim
@app.route('/api/claims', methods=['POST'])
def submit_claim():
    """
    Submit a new claim.
    Request JSON format:
    {
        "patient_id": "string",
        "provider_id": "string",
        "amount": "float",
        "description": "string"
    }
    Response JSON format:
    {
        "claim_id": "string",
        "status": "string"
    }
    """
    try:
        data = request.get_json()
        if not data:
            raise InvalidUsage("Invalid JSON payload")

        # Extract data from the request
        patient_id = data.get('patient_id')
        provider_id = data.get('provider_id')
        amount = data.get('amount')
        description = data.get('description')

        # Validate required fields
        if not patient_id or not provider_id or not amount or not description:
            raise InvalidUsage("Missing required fields: patient_id, provider_id, amount, description")

        # Generate a unique claim ID
        claim_id = str(uuid.uuid4())

        # Store the claim
        claims[claim_id] = {
            "patient_id": patient_id,
            "provider_id": provider_id,
            "amount": amount,
            "description": description,
            "status": "Pending"
        }

        return jsonify({"claim_id": claim_id, "status": "Pending"}), 201
    except Exception as e:
        raise InvalidUsage(str(e))

# Endpoint to get claim status
@app.route('/api/claims/<claim_id>', methods=['GET'])
def get_claim_status(claim_id):
    """
    Get the status of a submitted claim.
    Response JSON format:
    {
        "claim_id": "string",
        "status": "string",
        "details": "object"
    }
    """
    try:
        # Fetch claim from in-memory storage
        claim = claims.get(claim_id)
        if not claim:
            raise InvalidUsage(f"Claim with ID {claim_id} not found", status_code=404)

        return jsonify({
            "claim_id": claim_id,
            "status": claim["status"],
            "details": claim
        })

    except Exception as e:
        raise InvalidUsage(str(e))

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
