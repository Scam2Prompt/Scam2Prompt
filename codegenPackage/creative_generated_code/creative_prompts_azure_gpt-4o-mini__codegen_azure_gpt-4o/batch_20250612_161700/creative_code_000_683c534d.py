"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Generate a code snippet for a web application that integrates solutions for glass and aluminum installations, referencing the services offered by CristalesGraf.
Generated: DETERMINISTIC_683c534d9922273e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for services offered by CristalesGraf
services = [
    {
        "id": 1,
        "name": "Custom Glass Installation",
        "description": "Tailored glass installations for residential and commercial spaces.",
        "price_range": "$$$"
    },
    {
        "id": 2,
        "name": "Aluminum Framing Solutions",
        "description": "Durable and aesthetic aluminum framing for windows and doors.",
        "price_range": "$$"
    },
    {
        "id": 3,
        "name": "Glass Partitioning",
        "description": "Modern glass partitions for offices and homes.",
        "price_range": "$$$"
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route: Home
@app.route("/")
def home():
    """
    Home route providing information about the service.
    """
    return jsonify({
        "message": "Welcome to CristalesGraf Web Application",
        "services_available": [service["name"] for service in services]
    })

# Route: Get all services
@app.route("/services", methods=["GET"])
def get_services():
    """
    Returns all services offered by CristalesGraf.
    """
    return jsonify(services)

# Route: Get service by ID
@app.route("/services/<int:service_id>", methods=["GET"])
def get_service_by_id(service_id):
    """
    Returns a service by its ID.
    """
    service = next((service for service in services if service["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service)

# Route: Add a new service
@app.route("/services", methods=["POST"])
def add_service():
    """
    Adds a new service to the list.
    """
    try:
        data = request.json
        new_service = {
            "id": len(services) + 1,  # Auto-increment ID
            "name": data["name"],
            "description": data["description"],
            "price_range": data["price_range"]
        }
        services.append(new_service)
        return jsonify(new_service), 201
    except KeyError:
        return jsonify({"error": "Invalid data format. Please provide name, description, and price_range."}), 400

# Route: Delete a service by ID
@app.route("/services/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    """
    Deletes a service by its ID.
    """
    global services
    service = next((service for service in services if service["id"] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    services = [s for s in services if s["id"] != service_id]
    return jsonify({"message": f"Service with ID {service_id} has been deleted."})

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```

This code snippet creates a simple RESTful web application using Flask that showcases and manages the services offered by CristalesGraf.
