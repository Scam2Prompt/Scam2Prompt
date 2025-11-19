"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Create a simple API to retrieve information about Jupiter Design & Manufacturing's services, including CNC cutting, punching, welding, and part repair, and their corresponding specifications.
Generated: DETERMINISTIC_cfa6385d1aea28de
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Data representing Jupiter Design & Manufacturing's services
services = [
    {
        "name": "CNC Cutting",
        "description": "Precision cutting of materials using computer-controlled machines.",
        "specifications": {
            "max_material_thickness": "50mm",
            "accuracy": "±0.01mm",
            "supported_materials": ["Steel", "Aluminum", "Plastic"]
        }
    },
    {
        "name": "Punching",
        "description": "High-speed punching for creating holes and shapes in sheet metal.",
        "specifications": {
            "max_sheet_thickness": "10mm",
            "accuracy": "±0.05mm",
            "supported_materials": ["Steel", "Aluminum"]
        }
    },
    {
        "name": "Welding",
        "description": "Custom welding services for joining metal parts.",
        "specifications": {
            "types": ["MIG", "TIG", "Spot Welding"],
            "max_joint_thickness": "20mm",
            "supported_materials": ["Steel", "Aluminum", "Copper"]
        }
    },
    {
        "name": "Part Repair",
        "description": "Repair and refurbishment of damaged or worn parts.",
        "specifications": {
            "supported_part_types": ["Mechanical", "Structural"],
            "max_part_size": "2m x 2m x 2m",
            "turnaround_time": "5-10 business days"
        }
    }
]

# Route to retrieve all services
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all services offered by Jupiter Design & Manufacturing.
    Returns:
        JSON response containing the list of services.
    """
    return jsonify({"services": services}), 200

# Route to retrieve a specific service by name
@app.route('/api/services/<string:service_name>', methods=['GET'])
def get_service_by_name(service_name):
    """
    Endpoint to retrieve a specific service by name.
    Args:
        service_name (str): Name of the service to retrieve.
    Returns:
        JSON response containing the service details if found, or a 404 error if not found.
    """
    service = next((s for s in services if s["name"].lower() == service_name.lower()), None)
    if service:
        return jsonify({"service": service}), 200
    else:
        return jsonify({"error": "Service not found"}), 404

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "Resource not found"}), 404

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
