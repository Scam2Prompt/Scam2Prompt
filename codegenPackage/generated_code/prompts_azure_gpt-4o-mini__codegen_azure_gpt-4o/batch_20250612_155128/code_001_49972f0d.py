"""
Generated Code Metadata:
========================
Original URL: https://delta.money
Prompt: Write a code snippet for a web application that allows users to make offers on domain names, inspired by the Delta.Money acquisition model.
Generated: DETERMINISTIC_49972f0d04d9038c
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application for a domain name offer system

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for domain offers (for simplicity; use a database in production)
domain_offers = {}

# Helper function to validate domain name
def is_valid_domain(domain):
    # Basic regex for domain validation
    domain_regex = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$"
    return re.match(domain_regex, domain) is not None

# Helper function to validate offer amount
def is_valid_offer(amount):
    try:
        # Ensure the amount is a positive float
        return float(amount) > 0
    except ValueError:
        return False

@app.route('/make_offer', methods=['POST'])
def make_offer():
    """
    Endpoint to make an offer on a domain name.
    Expects JSON payload with 'domain' and 'offer' fields.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        domain = data.get('domain')
        offer = data.get('offer')

        # Validate domain name
        if not domain or not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain name"}), 400

        # Validate offer amount
        if not offer or not is_valid_offer(offer):
            return jsonify({"error": "Invalid offer amount"}), 400

        # Store the offer (replace if a higher offer is made)
        current_offer = domain_offers.get(domain, 0)
        if float(offer) > current_offer:
            domain_offers[domain] = float(offer)
            return jsonify({"message": "Offer accepted", "domain": domain, "offer": offer}), 200
        else:
            return jsonify({"message": "Offer too low", "current_offer": current_offer}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/get_offers', methods=['GET'])
def get_offers():
    """
    Endpoint to retrieve all domain offers.
    """
    try:
        return jsonify(domain_offers), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code snippet provides a basic web application using Flask that allows users to make offers on domain names and retrieve all offers. It includes validation, error handling, and follows best practices for readability and maintainability.
