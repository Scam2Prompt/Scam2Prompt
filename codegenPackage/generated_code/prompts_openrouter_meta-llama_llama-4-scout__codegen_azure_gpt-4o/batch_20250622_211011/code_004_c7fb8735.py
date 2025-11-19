"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Create a RESTful API endpoint to retrieve a fair cash offer for a house in San Francisco Bay Area, given its address and condition.
Generated: DETERMINISTIC_c7fb8735739ae870
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Helper function to validate address format
def is_valid_address(address):
    # Basic validation for address format (can be expanded as needed)
    return bool(re.match(r'^[0-9a-zA-Z\s,]+$', address))

# Helper function to calculate fair cash offer
def calculate_cash_offer(address, condition):
    # Placeholder logic for calculating cash offer
    # In production, this would involve complex algorithms, market data, etc.
    base_price = 1000000  # Base price for houses in SF Bay Area
    condition_multiplier = {
        "excellent": 1.2,
        "good": 1.0,
        "fair": 0.8,
        "poor": 0.5
    }
    multiplier = condition_multiplier.get(condition.lower(), 0.5)
    return base_price * multiplier

@app.route('/api/v1/cash-offer', methods=['POST'])
def get_cash_offer():
    """
    Endpoint to retrieve a fair cash offer for a house.
    Expects JSON payload with 'address' and 'condition'.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. JSON payload is required."}), 400

        # Extract and validate address
        address = data.get('address')
        if not address or not is_valid_address(address):
            return jsonify({"error": "Invalid or missing address."}), 400

        # Extract and validate condition
        condition = data.get('condition')
        if not condition or condition.lower() not in ["excellent", "good", "fair", "poor"]:
            return jsonify({"error": "Invalid or missing condition. Must be one of: excellent, good, fair, poor."}), 400

        # Calculate cash offer
        cash_offer = calculate_cash_offer(address, condition)

        # Return response
        return jsonify({
            "address": address,
            "condition": condition,
            "cash_offer": cash_offer
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
