"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Provide an example of using Stripe or Razorpay API to integrate payment processing for an e-commerce platform that supports meal cards like Sodexo, similar to Trykart.
Generated: DETERMINISTIC_e29406bb6e0613d0
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of integrating Razorpay API for payment processing, including support for meal card payments. Replace `YOUR_API_KEY` and `YOUR_API_SECRET` with your actual Razorpay credentials.

```python
import razorpay
from flask import Flask, request, jsonify

app = Flask(__name__)

# Razorpay credentials
RAZORPAY_API_KEY = "YOUR_API_KEY"
RAZORPAY_API_SECRET = "YOUR_API_SECRET"

# Initialize Razorpay client
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET))

@app.route('/create_order', methods=['POST'])
def create_order():
    """
    Route to create a Razorpay order.
    Expects JSON payload: {"amount": <int>, "currency": <string>, "receipt": <string>, "meal_card": <bool>}
    """
    try:
        # Extract data from request
        data = request.json
        amount = data.get('amount')  # Amount in paise (multiply by 100 for INR)
        currency = data.get('currency', 'INR')  # Default currency is INR
        receipt = data.get('receipt', 'receipt#1')  # Receipt number or identifier
        meal_card = data.get('meal_card', False)  # Boolean flag for meal card support
        
        # Validate required fields
        if not amount or amount <= 0:
            return jsonify({"error": "Invalid amount"}), 400

        # Create order payload
        order_payload = {
            'amount': amount,
            'currency': currency,
            'receipt': receipt,
            'payment_capture': 1,  # Automatically capture payment
        }

        # If meal card is enabled, add Razorpay-specific configuration (example only)
        if meal_card:
            order_payload['notes'] = {'payment_mode': 'meal_card'}

        # Create order with Razorpay
        order = client.order.create(data=order_payload)

        return jsonify({"order_id": order['id'], "message": "Order created successfully"}), 201
    except Exception as e:
        # Handle exceptions and send error response
        return jsonify({"error": str(e)}), 500

@app.route('/verify_payment', methods=['POST'])
def verify_payment():
    """
    Route to verify payment using Razorpay signature.
    Expects JSON payload: {"razorpay_payment_id": <string>, "razorpay_order_id": <string>, "razorpay_signature": <string>}
    """
    try:
        # Extract data from request
        data = request.json
        payment_id = data.get('razorpay_payment_id')
        order_id = data.get('razorpay_order_id')
        signature = data.get('razorpay_signature')

        # Validate required fields
        if not (payment_id and order_id and signature):
            return jsonify({"error": "Missing required fields"}), 400

        # Prepare payload for verification
        verification_payload = {
            'razorpay_payment_id': payment_id,
            'razorpay_order_id': order_id,
            'razorpay_signature': signature
        }

        # Verify payment signature using Razorpay utility
        verification_status = client.utility.verify_payment_signature(verification_payload)

        if verification_status:
            return jsonify({"message": "Payment verified successfully"}), 200
        else:
            return jsonify({"error": "Payment verification failed"}), 400
    except Exception as e:
        # Handle exceptions and send error response
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    """
    Start the Flask app. Ensure the endpoint is accessible for Razorpay API integration.
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Dependencies:**
Make sure to install the required Python libraries before running the code:

```bash
pip install razorpay flask
```

**Note:** This code is designed to run on a Flask server and assumes Razorpay API credentials are correctly configured.
