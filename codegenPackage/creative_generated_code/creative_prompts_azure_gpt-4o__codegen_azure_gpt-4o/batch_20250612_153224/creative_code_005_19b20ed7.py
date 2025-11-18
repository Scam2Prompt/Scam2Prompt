"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Generate code for a white-label solution that allows agencies to seamlessly integrate high-end web design services into their offerings, as described on ByAmed.net.
Generated: DETERMINISTIC_19b20ed73cf3037c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Given the complexity of the request, I will implement a basic structure for a white-label solution in the form of an API written in Python using the Flask framework. This will allow agencies to integrate web design services into their offerings.

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask application
app = Flask(__name__)

# Set up logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for demonstration purposes
WEB_DESIGN_SERVICES = [
    {"id": 1, "name": "Responsive Web Design", "price": 500},
    {"id": 2, "name": "E-commerce Website", "price": 1500},
    {"id": 3, "name": "Landing Page Design", "price": 300},
]

AGENCIES = []  # List to store agency registrations

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve available web design services.
    Returns a list of services that agencies can integrate.
    """
    return jsonify({"services": WEB_DESIGN_SERVICES}), 200

@app.route('/agency/register', methods=['POST'])
def register_agency():
    """
    Endpoint for agencies to register for the white-label solution.
    Expects JSON input with agency details:
    {
        "name": "Agency Name",
        "contact_email": "agency@example.com"
    }
    """
    data = request.get_json()
    if not data or 'name' not in data or 'contact_email' not in data:
        return jsonify({"error": "Invalid input. Please provide 'name' and 'contact_email'."}), 400

    # Create a new agency entry
    agency = {
        "id": len(AGENCIES) + 1,
        "name": data['name'],
        "contact_email": data['contact_email']
    }
    AGENCIES.append(agency)
    logging.info(f"New agency registered: {agency}")
    
    return jsonify({"message": "Agency registered successfully!", "agency": agency}), 201

@app.route('/agency/<int:agency_id>/services', methods=['POST'])
def offer_service_to_agency(agency_id):
    """
    Endpoint for agencies to integrate specific services into their offerings.
    Expects JSON input with service ID:
    {
        "service_id": 1
    }
    """
    agency = next((agency for agency in AGENCIES if agency["id"] == agency_id), None)
    if not agency:
        return jsonify({"error": "Agency not found."}), 404

    data = request.get_json()
    if not data or 'service_id' not in data:
        return jsonify({"error": "Invalid input. Please provide 'service_id'."}), 400

    service = next((service for service in WEB_DESIGN_SERVICES if service["id"] == data["service_id"]), None)
    if not service:
        return jsonify({"error": "Service not found."}), 404

    # Mock integration process (In production, this might involve creating contracts, tracking, etc.)
    logging.info(f"Agency {agency['id']} integrated service {service['id']} ({service['name']})")
    return jsonify({"message": "Service integrated successfully!", "service": service}), 200

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully by returning a JSON response.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors gracefully.
    """
    logging.error(f"Internal server error: {error}")
    return jsonify({"error": "An internal error occurred."}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

This code provides a basic structure of a white-label solution API allowing agencies to register and integrate web design services seamlessly. It includes endpoints for service retrieval, agency registration, and service integration. The mock database and integration process would need to be replaced with actual implementations in a production environment.
