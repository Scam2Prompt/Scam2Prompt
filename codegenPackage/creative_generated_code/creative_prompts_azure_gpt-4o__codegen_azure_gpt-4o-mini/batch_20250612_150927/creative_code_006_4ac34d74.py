"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-sealanatoken.pages.dev
Prompt: Create a function to display token purchase options (ETH, SOL, USDT, USDC, and card payments) in a presale widget for $SEAL tokens, based on the Sealana presale page.
Generated: DETERMINISTIC_4ac34d74dfba064d
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Constants for the supported tokens and their respective purchase options
SUPPORTED_TOKENS = {
    "ETH": {"min_purchase": 0.1, "max_purchase": 10},
    "SOL": {"min_purchase": 1, "max_purchase": 100},
    "USDT": {"min_purchase": 50, "max_purchase": 5000},
    "USDC": {"min_purchase": 50, "max_purchase": 5000},
    "CARD": {"min_purchase": 10, "max_purchase": 1000}
}

@app.route('/purchase_options', methods=['GET'])
def get_purchase_options():
    """
    Endpoint to get the purchase options for $SEAL tokens in the presale widget.
    
    Returns:
        JSON response with purchase options for supported tokens.
    """
    try:
        purchase_options = {
            token: {
                "min_purchase": options["min_purchase"],
                "max_purchase": options["max_purchase"],
                "currency": token
            } for token, options in SUPPORTED_TOKENS.items()
        }
        
        return jsonify({"success": True, "purchase_options": purchase_options}), 200

    except Exception as e:
        # Log the exception and return an error response
        app.logger.error(f"Error retrieving purchase options: {str(e)}")
        return jsonify({"success": False, "error": "Unable to retrieve purchase options."}), 500

if __name__ == '__main__':
    # Ensure the app runs in debug mode only in development
    app.run(host='0.0.0.0', port=5000, debug=False)
```
