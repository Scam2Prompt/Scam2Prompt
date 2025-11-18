"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write code to integrate payment processing for an e-commerce site, supporting transactions for items like "ageLOC® LumiSpa® Limpiador-Sensible" and "Super Glue Knauff."
Generated: DETERMINISTIC_15299dcfc13fa0a3
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stripe
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for the Stripe API (this should be kept secret)
stripe.api_key = "your_secret_key_here"

# List of products with their respective prices
products = {
    "ageLOC® LumiSpa® Limpiador-Sensible": 10000,  # Price in cents
    "Super Glue Knauff": 5000,  # Price in cents
}

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Handle checkout process by creating a payment intent.

    Request JSON format:
    {
        "product": "product_name",
        "currency": "currency_code"
    }
    """
    try:
        # Parse the request
        data = request.get_json()
        product_name = data['product']
        currency = data.get('currency', 'usd')  # Default to USD if no currency is provided

        # Validate product
        if product_name not in products:
            return jsonify({"error": "Product not found."}), 404
        
        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=products[product_name],
            currency=currency,
            payment_method_types=["card"],
        )
        
        # Return the client secret to the frontend
        return jsonify({
            "clientSecret": payment_intent["client_secret"],
            "product": product_name,
            "amount": products[product_name],
            "currency": currency
        }), 200

    except Exception as e:
        # Log the error for debugging purposes (in production, consider using a logging framework)
        print(f"Error occurred: {str(e)}")
        
        # Return a meaningful error response
        return jsonify({"error": "An error occurred while processing the payment."}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```

Make sure to install the required dependencies using:
```bash
pip install flask stripe
```

Replace `"your_secret_key_here"` with your actual Stripe secret key.
