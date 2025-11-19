"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Generate a REST API specification for a service that provides information on equine massage techniques and saddle fitting, referencing the services provided by Martin Godwin Equine Services.
Generated: DETERMINISTIC_2b9296ebaf4349a9
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for equine massage techniques and saddle fitting services
services_data = {
    "equine_massage_techniques": [
        {
            "id": 1,
            "name": "Swedish Massage",
            "description": "A technique that uses long strokes to improve circulation and relax muscles."
        },
        {
            "id": 2,
            "name": "Deep Tissue Massage",
            "description": "Focuses on deeper layers of muscle tissue to relieve tension and pain."
        }
    ],
    "saddle_fitting": [
        {
            "id": 1,
            "name": "Basic Saddle Fitting",
            "description": "Ensures the saddle fits the horse properly to prevent discomfort or injury."
        },
        {
            "id": 2,
            "name": "Advanced Saddle Fitting",
            "description": "Includes detailed analysis of saddle fit and rider posture."
        }
    ]
}

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint providing basic information about the API.
    """
    return jsonify({
        "message": "Welcome to Martin Godwin Equine Services API",
        "endpoints": {
            "/massage-techniques": "Get information on equine massage techniques",
            "/saddle-fitting": "Get information on saddle fitting services"
        }
    })

# Endpoint to get all equine massage techniques
@app.route("/massage-techniques", methods=["GET"])
def get_massage_techniques():
    """
    Returns a list of equine massage techniques.
    """
    return jsonify(services_data["equine_massage_techniques"])

# Endpoint to get a specific equine massage technique by ID
@app.route("/massage-techniques/<int:technique_id>", methods=["GET"])
def get_massage_technique_by_id(technique_id):
    """
    Returns details of a specific equine massage technique by ID.
    """
    technique = next((t for t in services_data["equine_massage_techniques"] if t["id"] == technique_id), None)
    if technique:
        return jsonify(technique)
    else:
        return jsonify({"error": "Massage technique not found"}), 404

# Endpoint to get all saddle fitting services
@app.route("/saddle-fitting", methods=["GET"])
def get_saddle_fitting_services():
    """
    Returns a list of saddle fitting services.
    """
    return jsonify(services_data["saddle_fitting"])

# Endpoint to get a specific saddle fitting service by ID
@app.route("/saddle-fitting/<int:service_id>", methods=["GET"])
def get_saddle_fitting_service_by_id(service_id):
    """
    Returns details of a specific saddle fitting service by ID.
    """
    service = next((s for s in services_data["saddle_fitting"] if s["id"] == service_id), None)
    if service:
        return jsonify(service)
    else:
        return jsonify({"error": "Saddle fitting service not found"}), 404

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
