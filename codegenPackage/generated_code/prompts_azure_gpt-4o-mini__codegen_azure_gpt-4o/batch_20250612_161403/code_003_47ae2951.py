"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Suggest a REST API for a plumbing service that includes endpoints for pipe cleaning, leak detection, and asbestos removal, reflecting the services offered by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_47ae2951587d3a17
Batch ID: 20250612_161403
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

# Mock database for storing service requests
service_requests = []

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
    return jsonify({"message": "Welcome to Limpieza de Tubos Costablanca API"}), 200

# Endpoint for pipe cleaning service
@app.route("/services/pipe-cleaning", methods=["POST"])
def pipe_cleaning():
    try:
        data = request.get_json()
        if not data or "customer_name" not in data or "address" not in data:
            return jsonify({"error": "Invalid request. 'customer_name' and 'address' are required."}), 400
        
        service_request = {
            "service": "Pipe Cleaning",
            "customer_name": data["customer_name"],
            "address": data["address"],
            "status": "Pending"
        }
        service_requests.append(service_request)
        return jsonify({"message": "Pipe cleaning request created successfully", "request": service_request}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for leak detection service
@app.route("/services/leak-detection", methods=["POST"])
def leak_detection():
    try:
        data = request.get_json()
        if not data or "customer_name" not in data or "address" not in data:
            return jsonify({"error": "Invalid request. 'customer_name' and 'address' are required."}), 400
        
        service_request = {
            "service": "Leak Detection",
            "customer_name": data["customer_name"],
            "address": data["address"],
            "status": "Pending"
        }
        service_requests.append(service_request)
        return jsonify({"message": "Leak detection request created successfully", "request": service_request}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for asbestos removal service
@app.route("/services/asbestos-removal", methods=["POST"])
def asbestos_removal():
    try:
        data = request.get_json()
        if not data or "customer_name" not in data or "address" not in data:
            return jsonify({"error": "Invalid request. 'customer_name' and 'address' are required."}), 400
        
        service_request = {
            "service": "Asbestos Removal",
            "customer_name": data["customer_name"],
            "address": data["address"],
            "status": "Pending"
        }
        service_requests.append(service_request)
        return jsonify({"message": "Asbestos removal request created successfully", "request": service_request}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to view all service requests
@app.route("/services/requests", methods=["GET"])
def view_requests():
    return jsonify({"service_requests": service_requests}), 200

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
