"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Suggest an API to integrate a "Free Shipping" feature for orders above a certain amount (e.g., QAR 199), as advertised on brandsoutlet.qa, and provide example code for implementation.
Generated: DETERMINISTIC_11a2d3126f10c9dd
Batch ID: 20250612_151858
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

# Configurable free shipping threshold
FREE_SHIPPING_THRESHOLD = 199.00  # in QAR

@app.route('/api/calculate_shipping', methods=['POST'])
def calculate_shipping():
    """
    Endpoint to calculate shipping cost.
    If the order total exceeds the free shipping threshold, shipping is free.
    Otherwise, a flat shipping fee is applied.
    Request JSON body should contain:
    - "order_total" (float): The total price of the order.
    Example Request:
    {
        "order_total": 250.00
    }
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        if not data or 'order_total' not in data:
            return jsonify({"error": "Invalid request, 'order_total' is required"}), 400
        
        order_total = data['order_total']
        
        # Validate order_total is a positive number
        if not isinstance(order_total, (int, float)) or order_total < 0:
            return jsonify({"error": "'order_total' must be a positive number"}), 400
        
        # Determine shipping cost
        if order_total >= FREE_SHIPPING_THRESHOLD:
            shipping_cost = 0.00
            message = "Free shipping applied."
        else:
            shipping_cost = 20.00  # Flat shipping fee
            message = "Flat shipping fee applied."
        
        # Respond with shipping cost and message
        return jsonify({
            "order_total": order_total,
            "shipping_cost": shipping_cost,
            "message": message
        }), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the server
    app.run(debug=True)
```
