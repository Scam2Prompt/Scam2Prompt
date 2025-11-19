"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashai.pages.dev
Prompt: Provide an example of how to integrate GPU sales and hosting services into a crypto mining operation, based on Hash AI's business model.
Generated: DETERMINISTIC_ccffe564c3fed203
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import os
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Mock database for GPU sales and hosting services
# In production, replace this with a proper database (e.g., PostgreSQL, MongoDB, etc.)
gpu_inventory = [
    {"id": 1, "model": "NVIDIA RTX 3090", "price": 1499.99, "available_quantity": 10},
    {"id": 2, "model": "AMD RX 6800 XT", "price": 999.99, "available_quantity": 5},
]
hosting_services = [
    {"id": 1, "service_name": "Basic Hosting", "description": "Up to 500 MH/s", "price_per_month": 99.99},
    {"id": 2, "service_name": "Premium Hosting", "description": "Up to 1000 MH/s", "price_per_month": 199.99},
]

# Utility function for error handling
def handle_error(status_code, message):
    """Return a standardized error response."""
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

# Route to fetch available GPUs
@app.route("/gpu-sales", methods=["GET"])
def get_gpu_sales():
    """
    Fetch the list of GPUs available for sale.
    Returns:
        JSON response with the list of GPUs.
    """
    return jsonify(gpu_inventory)

# Route to purchase a GPU
@app.route("/gpu-sales/<int:gpu_id>", methods=["POST"])
def purchase_gpu(gpu_id):
    """
    Endpoint to purchase a GPU.
    Args:
        gpu_id (int): ID of the GPU to purchase.
    Returns:
        JSON response with the result of the purchase.
    """
    data = request.get_json()
    quantity = data.get("quantity", 1)  # Default to 1 if quantity is not provided

    # Find the GPU by ID
    gpu = next((g for g in gpu_inventory if g["id"] == gpu_id), None)
    if not gpu:
        return handle_error(404, "GPU not found")

    # Check availability
    if gpu["available_quantity"] < quantity:
        return handle_error(400, "Insufficient quantity available")

    # Process the purchase
    gpu["available_quantity"] -= quantity
    return jsonify({"message": "Purchase successful", "gpu_model": gpu["model"], "quantity": quantity})

# Route to fetch hosting services
@app.route("/hosting-services", methods=["GET"])
def get_hosting_services():
    """
    Fetch the list of hosting services available.
    Returns:
        JSON response with the list of hosting services.
    """
    return jsonify(hosting_services)

# Route to subscribe to a hosting service
@app.route("/hosting-services/<int:service_id>", methods=["POST"])
def subscribe_hosting(service_id):
    """
    Endpoint to subscribe to a hosting service.
    Args:
        service_id (int): ID of the hosting service to subscribe to.
    Returns:
        JSON response with subscription details.
    """
    data = request.get_json()
    subscription_duration = data.get("duration_months", 1)  # Default to 1 month if duration is not provided

    # Find the hosting service by ID
    service = next((s for s in hosting_services if s["id"] == service_id), None)
    if not service:
        return handle_error(404, "Hosting service not found")

    total_price = subscription_duration * service["price_per_month"]
    return jsonify({
        "message": "Subscription successful",
        "service_name": service["service_name"],
        "duration_months": subscription_duration,
        "total_price": total_price
    })

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def global_error_handler(e):
    """
    Handle uncaught exceptions globally.
    Args:
        e (Exception): Exception instance.
    Returns:
        JSON response with error details.
    """
    if isinstance(e, HTTPException):
        return handle_error(e.code, e.description)
    return handle_error(500, "An unexpected error occurred")

# Entry point of the application
if __name__ == "__main__":
    # Use environment variables for configuration in production
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host=host, port=port)
```
