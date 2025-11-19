"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.legal
Prompt: How can I develop an API that connects businesses with arbitration services, referencing the features highlighted by Legal Arbitrium?
Generated: DETERMINISTIC_d30fcd185756fa3b
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Simulated database for arbitration services and businesses
arbitration_services = [
    {"id": 1, "name": "Legal Arbitrium Services", "specialty": "Contract Disputes"},
    {"id": 2, "name": "Mediation Experts", "specialty": "Small Business Disputes"},
]

businesses = []

# Custom error handler for production readiness
@app.errorhandler(Exception)
def handle_exception(e):
    # Handle HTTP exceptions
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    # Handle non-HTTP exceptions
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/arbitration-services', methods=['GET'])
def get_arbitration_services():
    """
    Endpoint to retrieve the list of available arbitration services.
    Returns:
        JSON response with the list of services.
    """
    return jsonify({"services": arbitration_services}), 200

@app.route('/businesses', methods=['POST'])
def register_business():
    """
    Endpoint to register a business seeking arbitration services.
    Request Data:
        JSON payload with `name` and `industry`.
    Returns:
        JSON response confirming business registration.
    """
    try:
        data = request.json
        name = data.get("name")
        industry = data.get("industry")

        # Validate input
        if not name or not industry:
            return jsonify({"error": "Both 'name' and 'industry' fields are required"}), 400

        # Add business to simulated database
        business = {"id": len(businesses) + 1, "name": name, "industry": industry}
        businesses.append(business)

        return jsonify({"message": "Business registered successfully", "business": business}), 201

    except Exception as e:
        return jsonify({"error": "Invalid request"}), 400

@app.route('/match-arbitration-service', methods=['POST'])
def match_service():
    """
    Endpoint to match a business with an arbitration service based on specialty.
    Request Data:
        JSON payload with `business_id` and `specialty`.
    Returns:
        JSON response with matched arbitration services.
    """
    try:
        data = request.json
        business_id = data.get("business_id")
        specialty = data.get("specialty")

        # Validate input
        if not business_id or not specialty:
            return jsonify({"error": "Both 'business_id' and 'specialty' fields are required"}), 400

        # Find matching services
        matching_services = [
            service for service in arbitration_services if service["specialty"].lower() == specialty.lower()
        ]

        if not matching_services:
            return jsonify({"message": "No matching arbitration services found"}), 404

        return jsonify({"business_id": business_id, "matching_services": matching_services}), 200

    except Exception as e:
        return jsonify({"error": "Invalid request"}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
