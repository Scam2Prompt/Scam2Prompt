"""
Generated Code Metadata:
========================
Original URL: https://delourier.com
Prompt: Generate code to implement a secure payment system for a luxury fashion e-commerce website like Delourier, ensuring compatibility with worldwide shipping and free shipping options.
Generated: DETERMINISTIC_cdcda964ad6e41de
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from payment_gateway import PaymentGateway  # Hypothetical payment gateway library

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configuration for payment gateway
PAYMENT_GATEWAY_API_KEY = 'your_api_key_here'
payment_gateway = PaymentGateway(api_key=PAYMENT_GATEWAY_API_KEY)

# Sample product data
products = {
    "luxury_bag": {"price": 1200, "currency": "USD"},
    "designer_shoes": {"price": 800, "currency": "USD"},
}

# Free shipping threshold
FREE_SHIPPING_THRESHOLD = 1000

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Process the checkout for a luxury fashion e-commerce website.
    Expects a JSON payload with product IDs and payment information.
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data:
            raise BadRequest("Request must be JSON")

        product_ids = data.get('product_ids', [])
        payment_info = data.get('payment_info', {})

        # Validate product IDs
        total_amount = 0
        for product_id in product_ids:
            if product_id not in products:
                raise BadRequest(f"Product ID '{product_id}' is not valid")
            total_amount += products[product_id]['price']

        # Determine shipping cost
        shipping_cost = 0 if total_amount >= FREE_SHIPPING_THRESHOLD else 50  # Flat shipping fee

        # Process payment
        payment_response = payment_gateway.process_payment(total_amount + shipping_cost, payment_info)
        if not payment_response['success']:
            raise Exception("Payment processing failed: " + payment_response['message'])

        # Return success response
        return jsonify({
            "message": "Payment successful",
            "total_amount": total_amount,
            "shipping_cost": shipping_cost,
            "order_id": payment_response['order_id']
        }), 200

    except BadRequest as e:
        logging.error(f"Bad request: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Error processing payment: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

### Note:
- The `PaymentGateway` class is a placeholder for an actual payment processing library.
- Ensure to replace `'your_api_key_here'` with a valid API key for the payment gateway.
- This code assumes the use of Flask for the web framework. Make sure to install Flask and any other dependencies required for your project.
