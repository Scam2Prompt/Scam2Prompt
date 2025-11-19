"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delta.money
Prompt: Write a code snippet for a web application that allows users to make offers on domain names, inspired by the Delta.Money acquisition model.
Generated: DETERMINISTIC_49972f0d04d9038c
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required imports
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory database to hold domain offers
offers = {}

def is_valid_domain(domain):
    """
    Validate domain name using regex.
    """
    domain_regex = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$"
    return re.match(domain_regex, domain) is not None

@app.route("/offer", methods=["POST"])
def make_offer():
    """
    Endpoint to allow users to make an offer on a domain name.
    """
    try:
        data = request.json

        # Validate input data
        if not data or 'domain' not in data or 'offer' not in data:
            return jsonify({"error": "Invalid request. Please provide 'domain' and 'offer' fields."}), 400

        domain = data['domain'].strip().lower()
        offer = data['offer']

        # Validate domain
        if not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain name format."}), 400

        # Validate offer
        if not isinstance(offer, (int, float)) or offer <= 0:
            return jsonify({"error": "Offer must be a positive number."}), 400

        # Check if the domain already has an offer
        if domain in offers:
            existing_offer = offers[domain]
            if offer <= existing_offer:
                return jsonify({"error": f"Offer must exceed the current offer of {existing_offer}."}), 400

        # Save the offer
        offers[domain] = offer
        return jsonify({"message": f"Offer of {offer} placed on domain '{domain}' successfully."}), 200
    except Exception as ex:
        # General error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(ex)}), 500

@app.route("/offers", methods=["GET"])
def get_offers():
    """
    Endpoint to retrieve all domain offers.
    """
    try:
        return jsonify({"offers": offers}), 200
    except Exception as ex:
        return jsonify({"error": "An unexpected error occurred.", "details": str(ex)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
