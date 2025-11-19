"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayatrecruitment.com
Prompt: Outline a workflow for integrating a payment gateway like Instamojo into a web application for processing application fees similar to Rayat Shikshan Sanstha's system.
Generated: DETERMINISTIC_4c8bd562366a847b
Batch ID: 20250612_160742
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.instamojo.com/v2/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/payment-status": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import requests

# Initialize Flask application
app = Flask(__name__)

# Configuration for Instamojo
INSTAMOJO_API_URL = "https://api.instamojo.com/v2/"
INSTAMOJO_AUTH_KEY = "YOUR_AUTH_KEY"  # Replace with your actual Auth Key
INSTAMOJO_AUTH_TOKEN = "YOUR_AUTH_TOKEN"  # Replace with your actual Auth Token

# Function to create a payment order
def create_payment_order(amount, purpose, buyer_name, buyer_email):
    """
    Create a payment order with Instamojo.

    :param amount: Amount to be charged
    :param purpose: Purpose of the payment
    :param buyer_name: Name of the buyer
    :param buyer_email: Email of the buyer
    :return: Response from Instamojo API
    """
    headers = {
        "X-Auth-Token": INSTAMOJO_AUTH_TOKEN,
        "Content-Type": "application/json"
    }
    
    payload = {
        "purpose": purpose,
        "amount": amount,
        "buyer_name": buyer_name,
        "buyer_email": buyer_email,
        "redirect_url": "http://localhost:5000/payment-status"  # Your redirect URL
    }
    
    try:
        response = requests.post(INSTAMOJO_API_URL + "payments/request/", json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating payment order: {e}")
        return None

# Route for payment initiation
@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    """
    Endpoint to initiate payment.

    :return: JSON response with payment link or error message
    """
    data = request.json
    amount = data.get("amount")
    purpose = data.get("purpose")
    buyer_name = data.get("buyer_name")
    buyer_email = data.get("buyer_email")

    order = create_payment_order(amount, purpose, buyer_name, buyer_email)

    if order and 'payment_request' in order:
        return jsonify({'payment_url': order['payment_request']['longurl']}), 200
    else:
        return jsonify({'error': 'Failed to create payment order'}), 500

# Route for payment status
@app.route('/payment-status', methods=['GET'])
def payment_status():
    """
    Endpoint to handle payment status redirect.

    :return: Rendered payment status page
    """
    payment_id = request.args.get('payment_id')
    payment_status = request.args.get('payment_status')

    # Render a simple confirmation page
    return render_template('payment_status.html', payment_id=payment_id, payment_status=payment_status)

# Main function to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (payment_status.html)
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Payment Status</title>
</head>
<body>
    <h1>Payment Status</h1>
    <p>Payment ID: {{ payment_id }}</p>
    <p>Status: {{ payment_status }}</p>
</body>
</html>
```
### Ensure to install Flask and requests:
```bash
pip install Flask requests
```
### Note: 
- Replace `YOUR_AUTH_KEY` and `YOUR_AUTH_TOKEN` with actual credentials from Instamojo.
- Ensure the application is tested thoroughly before production deployment.
- Update the redirect URL to a valid endpoint in your application.
