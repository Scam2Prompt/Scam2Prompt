"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Recommend an API or library for implementing an "Online Donation" system specifically tailored for church websites, as described on ChurchProWeb. Include code examples for integrating payment gateways.
Generated: DETERMINISTIC_a9fd5d6ea104c3ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This code demonstrates how to integrate Stripe as a payment gateway for an online donation system.
Stripe is a reliable and widely-used library. Ensure you have your Stripe API keys and install the Stripe Python SDK:
`pip install stripe`
"""

import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stripe API keys (replace with your actual keys from your Stripe dashboard)
stripe.api_key = "sk_test_your_secret_key"  # Secret Key

# Route to handle donations
@app.route("/donate", methods=["POST"])
def donate():
    """
    Endpoint to handle donation requests.
    Expects a JSON payload with:
    - 'amount' (in cents)
    - 'currency' (e.g., 'usd')
    - 'source' (Stripe payment method such as a token or card ID)
    - 'description' (optional description of the donation)
    """
    try:
        # Parse the JSON request data
        data = request.get_json()
        amount = data["amount"]
        currency = data["currency"]
        source = data["source"]
        description = data.get("description", "Church Donation")

        # Create a charge using Stripe's API
        charge = stripe.Charge.create(
            amount=amount,  # Amount in cents
            currency=currency,
            source=source,  # Payment method token
            description=description
        )

        # Return success response
        return jsonify({"message": "Donation successful", "charge_id": charge.id}), 200
    except stripe.error.StripeError as e:
        # Handle Stripe API errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


# Route to display donation form (optional)
@app.route("/")
def donation_form():
    """
    Simple HTML donation form for testing.
    Users would typically generate a Stripe token client-side using Stripe.js or Stripe Elements.
    """
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Church Donation</title>
    </head>
    <body>
        <h1>Donate to Our Church</h1>
        <form action="/donate" method="POST">
            <label for="amount">Donation Amount (in cents):</label>
            <input type="number" name="amount" id="amount" required><br>
            <label for="currency">Currency:</label>
            <select name="currency" id="currency">
                <option value="usd">USD</option>
                <option value="eur">EUR</option>
                <option value="gbp">GBP</option>
            </select><br>
            <label for="source">Payment Source Token:</label>
            <input type="text" name="source" id="source" required><br>
            <label for="description">Description:</label>
            <input type="text" name="description" id="description"><br>
            <button type="submit">Donate</button>
        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
1. Replace `sk_test_your_secret_key` with your actual Stripe secret key.
2. Integrate Stripe.js or Stripe Elements on the front end to securely collect payment method details and generate tokens. The example here assumes you pass a token (`source`) via the JSON payload.
3. Use environment variables or a secure method to store and access API keys in production.
