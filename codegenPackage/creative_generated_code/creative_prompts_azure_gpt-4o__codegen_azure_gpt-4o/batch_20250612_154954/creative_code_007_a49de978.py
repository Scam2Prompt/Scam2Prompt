"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbase.com
Prompt: Write code to implement a feature for registering and tracking product deliveries in a mobile app, inspired by the SVG Mobil App functionality on inbase.com.
Generated: DETERMINISTIC_a49de97865916fc6
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for deliveries (for demonstration purposes only, replace with a database in production)
deliveries = {}

# Helper function to generate unique delivery IDs
def generate_delivery_id():
    return str(uuid.uuid4())

# Route to handle product delivery registration
@app.route('/register_delivery', methods=['POST'])
def register_delivery():
    """
    Endpoint to register a new product delivery.
    Expects a JSON payload with 'product_name', 'delivery_address', and 'delivery_date'.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        product_name = data.get('product_name')
        delivery_address = data.get('delivery_address')
        delivery_date = data.get('delivery_date')  # Expected in "YYYY-MM-DD" format

        # Validate required fields
        if not product_name or not delivery_address or not delivery_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate delivery_date format
        try:
            delivery_date_obj = datetime.strptime(delivery_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD'"}), 400

        # Generate a unique delivery ID
        delivery_id = generate_delivery_id()

        # Save the delivery to the in-memory storage
        deliveries[delivery_id] = {
            "product_name": product_name,
            "delivery_address": delivery_address,
            "delivery_date": delivery_date_obj.strftime("%Y-%m-%d"),
            "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Return success response
        return jsonify({
            "message": "Delivery registered successfully",
            "delivery_id": delivery_id
        }), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to retrieve all deliveries
@app.route('/get_deliveries', methods=['GET'])
def get_deliveries():
    """
    Endpoint to retrieve all registered deliveries.
    Returns a list of all deliveries in JSON format.
    """
    try:
        return jsonify({
            "deliveries": deliveries
        }), 200
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to retrieve a specific delivery by ID
@app.route('/get_delivery/<delivery_id>', methods=['GET'])
def get_delivery(delivery_id):
    """
    Endpoint to retrieve a specific delivery by its ID.
    Returns the delivery details if found.
    """
    try:
        # Check if the delivery exists
        delivery = deliveries.get(delivery_id)
        if not delivery:
            return jsonify({"error": "Delivery not found"}), 404

        return jsonify(delivery), 200
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to delete a specific delivery by ID
@app.route('/delete_delivery/<delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id):
    """
    Endpoint to delete a specific delivery by its ID.
    """
    try:
        # Check if the delivery exists
        if delivery_id not in deliveries:
            return jsonify({"error": "Delivery not found"}), 404

        # Delete the delivery
        del deliveries[delivery_id]

        return jsonify({"message": "Delivery deleted successfully"}), 200
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
