"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Design a RESTful API that connects users with medical care services offered by Shiv Vedika Trust for individuals in their final days.
Generated: DETERMINISTIC_580839ccd4a84954
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation
services = [
    {
        "id": 1,
        "name": "Palliative Care",
        "description": "Specialized care for individuals in their final days.",
        "availability": True
    },
    {
        "id": 2,
        "name": "Spiritual Support",
        "description": "Providing emotional and spiritual support to patients.",
        "availability": True
    },
    {
        "id": 3,
        "name": "Home Visit",
        "description": "Medical professionals providing care at home.",
        "availability": False
    }
]

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Root endpoint
@app.route("/")
def index():
    return jsonify({"message": "Welcome to Shiv Vedika Trust Medical Services API"}), 200

# Endpoint to retrieve all services
@app.route("/services", methods=["GET"])
def get_services():
    return jsonify({"services": services}), 200

# Endpoint to retrieve a specific service by ID
@app.route("/services/<int:service_id>", methods=["GET"])
def get_service(service_id):
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service), 200

# Endpoint to create a new medical service
@app.route("/services", methods=["POST"])
def create_service():
    try:
        data = request.get_json()
        if not data or "name" not in data or "description" not in data or "availability" not in data:
            return jsonify({"error": "Invalid input"}), 400

        # Generate a new ID based on the last service ID
        new_id = max(s["id"] for s in services) + 1 if services else 1
        new_service = {
            "id": new_id,
            "name": data["name"],
            "description": data["description"],
            "availability": data["availability"]
        }
        services.append(new_service)
        return jsonify(new_service), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to update an existing service
@app.route("/services/<int:service_id>", methods=["PUT"])
def update_service(service_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        service = next((s for s in services if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Update fields if available in input
        service["name"] = data.get("name", service["name"])
        service["description"] = data.get("description", service["description"])
        service["availability"] = data.get("availability", service["availability"])
        return jsonify(service), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to delete a service by ID
@app.route("/services/<int:service_id>", methods=["DELETE"])
def delete_service(service_id):
    try:
        service = next((s for s in services if s["id"] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        services.remove(service)
        return jsonify({"message": "Service deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main application entry point
if __name__ == "__main__":
    app.run(debug=True)
```
