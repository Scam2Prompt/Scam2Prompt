"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Create an API endpoint to handle customer orders for a meat business, inspired by Conficarnes del Valle's services.
Generated: DETERMINISTIC_f8111c0185c324bd
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setup logging for debugging and production
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Example database simulation
orders_db = []  # Simulate a database with a list

# Error handling middleware
@app.errorhandler(404)
def handle_404_error(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def handle_500_error(error):
    logging.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

# Define API endpoint for customer orders
@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a new customer order.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "contact": "+123456789",
        "order_details": [
            {"product": "Beef", "quantity": 2, "price_per_unit": 20.0},
            {"product": "Chicken", "quantity": 1, "price_per_unit": 10.0}
        ]
    }
    """
    try:
        # Parse incoming request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400
        
        # Validate required fields
        required_fields = ["customer_name", "contact", "order_details"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Validate order details
        if not isinstance(data["order_details"], list) or len(data["order_details"]) == 0:
            return jsonify({"error": "Invalid order details"}), 400
        
        # Calculate total amount
        total_amount = sum(
            item["quantity"] * item["price_per_unit"]
            for item in data["order_details"]
            if "quantity" in item and "price_per_unit" in item
        )

        # Create order object
        new_order = {
            "id": len(orders_db) + 1,  # Simple ID generation
            "customer_name": data["customer_name"],
            "contact": data["contact"],
            "order_details": data["order_details"],
            "total_amount": total_amount
        }

        # Save to database (simulated)
        orders_db.append(new_order)

        # Return success response
        logging.info(f"Order created: {new_order}")
        return jsonify({"message": "Order created successfully", "order_id": new_order["id"]}), 201

    except Exception as e:
        logging.error(f"Error creating order: {str(e)}")
        return jsonify({"error": "Failed to create order"}), 500


@app.route('/api/orders', methods=['GET'])
def list_orders():
    """
    Endpoint to fetch all customer orders.
    """
    return jsonify(orders_db), 200


# Application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
