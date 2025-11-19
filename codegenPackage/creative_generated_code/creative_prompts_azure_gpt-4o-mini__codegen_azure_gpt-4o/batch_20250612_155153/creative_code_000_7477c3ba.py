"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gegetastycakes-353.pages.dev
Prompt: Generate a code snippet for an online ordering system that allows users to select cake flavors and specify local or shipped delivery options, similar to the offerings on gegetastycakes-353.pages.dev.
Generated: DETERMINISTIC_7477c3ba25dbb15b
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample list of available cake flavors
CAKE_FLAVORS = ["Vanilla", "Chocolate", "Red Velvet", "Carrot", "Lemon"]

# Sample delivery options
DELIVERY_OPTIONS = ["Local Pickup", "Shipped"]

@app.route('/cakes', methods=['GET'])
def get_cake_flavors():
    """
    Endpoint to retrieve available cake flavors.
    Returns:
        JSON response with the list of cake flavors.
    """
    return jsonify({"cake_flavors": CAKE_FLAVORS}), 200

@app.route('/delivery-options', methods=['GET'])
def get_delivery_options():
    """
    Endpoint to retrieve delivery options.
    Returns:
        JSON response with the available delivery options.
    """
    return jsonify({"delivery_options": DELIVERY_OPTIONS}), 200

@app.route('/order', methods=['POST'])
def place_order():
    """
    Endpoint to place an order.
    Request body should include:
        flavor: The selected cake flavor (string).
        delivery: Delivery option (Local Pickup or Shipped) (string).
        customer_name: Name of the customer (string).
    Returns:
        JSON response with the order summary or error message.
    """
    try:
        # Parse JSON request body
        data = request.get_json()

        # Validate request data
        flavor = data.get("flavor")
        delivery = data.get("delivery")
        customer_name = data.get("customer_name")

        if flavor not in CAKE_FLAVORS:
            return jsonify({"error": "Invalid cake flavor selected."}), 400
        if delivery not in DELIVERY_OPTIONS:
            return jsonify({"error": "Invalid delivery option selected."}), 400
        if not customer_name or not isinstance(customer_name, str):
            return jsonify({"error": "Customer name is required and must be a string."}), 400

        # Generate order summary
        order_summary = {
            "message": "Order placed successfully!",
            "order_details": {
                "customer_name": customer_name,
                "cake_flavor": flavor,
                "delivery_option": delivery
            }
        }

        return jsonify(order_summary), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
