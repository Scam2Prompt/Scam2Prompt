"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.uk
Prompt: How can I create an API to handle inquiries for domain names like 1inch.uk, including fields for name, email, and offer amount?
Generated: DETERMINISTIC_3670b09b5a927fbd
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation for creating an API to handle inquiries about domain names. The code is written in Python using the Flask framework.

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Helper function to validate email addresses
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Helper function to validate domain names
def is_valid_domain(domain):
    regex = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, domain) is not None

# Route to handle domain inquiries
@app.route('/api/inquiry', methods=['POST'])
def handle_inquiry():
    try:
        # Parse and validate JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format. JSON payload expected."}), 400
        
        name = data.get('name')
        email = data.get('email')
        domain = data.get('domain')
        offer_amount = data.get('offer_amount')
        
        # Validate required fields
        if not name or not email or not domain or offer_amount is None:
            return jsonify({"error": "Missing required fields: name, email, domain, offer_amount."}), 400
        
        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format."}), 400

        # Validate domain format
        if not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain name format."}), 400
        
        # Validate offer amount
        try:
            offer_amount = float(offer_amount)
            if offer_amount <= 0:
                return jsonify({"error": "Offer amount must be greater than 0."}), 400
        except ValueError:
            return jsonify({"error": "Invalid offer amount. Must be a number."}), 400

        # Simulated response for a successful inquiry submission
        response = {
            "message": "Inquiry successfully submitted!",
            "data": {
                "name": name,
                "email": email,
                "domain": domain,
                "offer_amount": offer_amount
            }
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes:
1. Install Flask before running this code: `pip install flask`.
2. Save this code to a file named `app.py` or similar and run it using `python app.py`.
3. This API listens for POST requests at `/api/inquiry` and expects a JSON payload with `name`, `email`, `domain`, and `offer_amount`.
