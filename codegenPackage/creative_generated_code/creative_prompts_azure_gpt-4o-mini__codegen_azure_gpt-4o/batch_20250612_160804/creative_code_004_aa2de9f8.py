"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccjourney.co
Prompt: Illustrate how to implement a pre-order system in a web application for fashion collections, inspired by the Capsule Cosmic Journey's pre-order offerings.
Generated: DETERMINISTIC_aa2de9f840b37e4f
Batch ID: 20250612_160804
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

# Initialize Flask application
app = Flask(__name__)

# In-memory database (for illustration, should use a proper database like PostgreSQL in production)
fashion_collections = [
    {"id": "1", "name": "Cosmic Jacket", "price": 120.0, "stock": 100, "pre_order_available": True},
    {"id": "2", "name": "Galaxy Boots", "price": 80.0, "stock": 50, "pre_order_available": True},
    {"id": "3", "name": "Stellar Bag", "price": 50.0, "stock": 0, "pre_order_available": True},
]
pre_orders = []  # Store pre-orders

# Helper function to find a collection by ID
def find_collection_by_id(collection_id):
    for collection in fashion_collections:
        if collection["id"] == collection_id:
            return collection
    return None

@app.route('/collections', methods=['GET'])
def get_collections():
    """
    Endpoint to return all fashion collections with pre-order availability.
    """
    return jsonify({"collections": fashion_collections}), 200

@app.route('/pre-order', methods=['POST'])
def create_pre_order():
    """
    Endpoint to create a pre-order for a fashion collection.
    Expected JSON payload format:
    {
        "collection_id": "1",
        "customer_name": "John Doe",
        "customer_email": "john.doe@example.com"
    }
    """
    data = request.get_json()
    
    # Validate request payload
    if not data or "collection_id" not in data or "customer_name" not in data or "customer_email" not in data:
        return jsonify({"error": "Invalid payload. Please provide collection_id, customer_name, and customer_email."}), 400
    
    collection_id = data["collection_id"]
    customer_name = data["customer_name"]
    customer_email = data["customer_email"]

    # Find the collection
    collection = find_collection_by_id(collection_id)
    if not collection:
        return jsonify({"error": "Collection not found."}), 404

    # Check if pre-order is available for the collection
    if not collection["pre_order_available"]:
        return jsonify({"error": "Pre-order not available for this collection."}), 400

    # Create the pre-order
    pre_order = {
        "id": str(uuid.uuid4()),  # Generate a unique ID for the pre-order
        "collection_id": collection_id,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "status": "pending"  # Initial status of the pre-order
    }
    pre_orders.append(pre_order)
    
    return jsonify({"message": "Pre-order created successfully.", "pre_order": pre_order}), 201

@app.route('/pre-orders', methods=['GET'])
def get_pre_orders():
    """
    Endpoint to retrieve all pre-orders. 
    This would typically be restricted to admin access.
    """
    return jsonify({"pre_orders": pre_orders}), 200

@app.errorhandler(404)
def handle_404_error(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def handle_500_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

# Run the application (for production, use a WSGI server like Gunicorn or uWSGI)
if __name__ == '__main__':
    app.run(debug=True)
```
