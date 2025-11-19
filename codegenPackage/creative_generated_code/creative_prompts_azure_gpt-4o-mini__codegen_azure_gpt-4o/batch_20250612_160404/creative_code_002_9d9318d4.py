"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehnlo.com
Prompt: Provide an example of how to create a user-friendly checkout process for domain purchases, incorporating local currency options as mentioned on hehnlo.com.
Generated: DETERMINISTIC_9d9318d4c1517e68
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database for domains and prices in USD
DOMAINS = {
    "example.com": 10.0,
    "mywebsite.org": 15.0,
    "coolsite.net": 12.0,
}

# Exchange rates to convert USD to local currencies
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.81,
    "INR": 82.74,
    "JPY": 148.86,
}

# Utility function to convert prices to local currencies
def convert_currency(amount, currency):
    if currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported currency: {currency}")
    return round(amount * EXCHANGE_RATES[currency], 2)

@app.route("/checkout", methods=["POST"])
def checkout():
    try:
        # Parse the incoming request data
        data = request.json
        if not data:
            return jsonify({"error": "Request must contain JSON data"}), 400
        
        domain = data.get("domain")
        currency = data.get("currency", "USD")
        
        if not domain:
            return jsonify({"error": "Domain is required"}), 400
        
        if domain not in DOMAINS:
            return jsonify({"error": f"Domain '{domain}' not available"}), 404
        
        if currency not in EXCHANGE_RATES:
            return jsonify({"error": f"Currency '{currency}' is not supported"}), 400
        
        # Calculate price in local currency
        price_usd = DOMAINS[domain]
        price_local = convert_currency(price_usd, currency)
        
        # Generate a transaction ID
        transaction_id = str(uuid.uuid4())
        
        # Return checkout details
        return jsonify({
            "transaction_id": transaction_id,
            "domain": domain,
            "price_usd": price_usd,
            "price_local": price_local,
            "currency": currency
        }), 200
    
    except ValueError as ve:
        # Handle currency conversion errors
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Main entry point for running the application
if __name__ == "__main__":
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```
