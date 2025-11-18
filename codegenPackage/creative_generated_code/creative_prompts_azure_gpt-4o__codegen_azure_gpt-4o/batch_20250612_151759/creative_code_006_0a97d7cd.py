"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-lab.net
Prompt: Suggest an API for calculating taxes during checkout for digital music purchases, as described in Soniculture's shopping cart system.
Generated: DETERMINISTIC_0a97d7cd10a2eb6d
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants for tax rates based on location
TAX_RATES = {
    "US": 0.07,  # 7% tax for the United States
    "EU": 0.20,  # 20% tax for European Union
    "IN": 0.18,  # 18% tax for India
    # Add more regions as necessary
}

@app.route('/calculate-tax', methods=['POST'])
def calculate_tax():
    """
    API endpoint to calculate taxes for digital music purchases during checkout.
    Accepts a JSON payload with purchase amount and location.
    """
    try:
        # Parse JSON payload
        data = request.get_json()

        # Validate input
        if not data or 'amount' not in data or 'location' not in data:
            return jsonify({"error": "Invalid input. 'amount' and 'location' are required."}), 400
        
        amount = data['amount']
        location = data['location']

        # Ensure amount is a positive numeric value
        if not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"error": "Invalid amount. Must be a positive number."}), 400

        # Retrieve the tax rate for the location
        tax_rate = TAX_RATES.get(location.upper())
        if tax_rate is None:
            return jsonify({"error": f"Unsupported location: {location}."}), 400

        # Calculate tax and total
        tax = round(amount * tax_rate, 2)
        total = round(amount + tax, 2)

        # Return the calculated tax and total
        return jsonify({
            "amount": amount,
            "location": location.upper(),
            "tax_rate": tax_rate,
            "tax": tax,
            "total": total
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)  # Set debug to True during development, False in production
```
