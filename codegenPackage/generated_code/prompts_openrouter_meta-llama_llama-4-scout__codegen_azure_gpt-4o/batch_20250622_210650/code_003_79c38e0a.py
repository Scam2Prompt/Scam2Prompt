"""
Generated Code Metadata:
========================
Original URL: https://jesse-presales1.pages.dev
Prompt: Design an API for tracking and displaying real-time information about a token sale, including metrics like presale cap, total supply, and exchange rates, as seen on this $JESSE presale page.
Generated: DETERMINISTIC_79c38e0aac9c5e75
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Mock data for the token sale
TOKEN_SALE_DATA = {
    "token_name": "$JESSE",
    "presale_cap": 1000000,  # Maximum number of tokens available in presale
    "total_supply": 5000000,  # Total supply of tokens
    "exchange_rate": 0.01,  # Exchange rate in USD per token
    "tokens_sold": 250000,  # Tokens sold so far
    "start_time": datetime(2023, 10, 1, 12, 0, 0),  # Presale start time
    "end_time": datetime(2023, 10, 15, 12, 0, 0),  # Presale end time
}

# Helper function to calculate remaining tokens
def calculate_remaining_tokens():
    return TOKEN_SALE_DATA["presale_cap"] - TOKEN_SALE_DATA["tokens_sold"]

# Helper function to check if the presale is active
def is_presale_active():
    now = datetime.now()
    return TOKEN_SALE_DATA["start_time"] <= now <= TOKEN_SALE_DATA["end_time"]

@app.route('/api/token-sale', methods=['GET'])
def get_token_sale_info():
    """
    Endpoint to retrieve real-time information about the token sale.
    Returns:
        JSON object containing token sale metrics.
    """
    try:
        remaining_tokens = calculate_remaining_tokens()
        presale_active = is_presale_active()

        response = {
            "token_name": TOKEN_SALE_DATA["token_name"],
            "presale_cap": TOKEN_SALE_DATA["presale_cap"],
            "total_supply": TOKEN_SALE_DATA["total_supply"],
            "exchange_rate": TOKEN_SALE_DATA["exchange_rate"],
            "tokens_sold": TOKEN_SALE_DATA["tokens_sold"],
            "remaining_tokens": remaining_tokens,
            "presale_active": presale_active,
            "start_time": TOKEN_SALE_DATA["start_time"].isoformat(),
            "end_time": TOKEN_SALE_DATA["end_time"].isoformat(),
        }

        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while fetching token sale data.", "details": str(e)}), 500

@app.route('/api/token-sale/update', methods=['POST'])
def update_token_sale():
    """
    Endpoint to update token sale metrics.
    Expects JSON payload with keys: 'tokens_sold', 'exchange_rate'.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data:
            return jsonify({"error": "Invalid input. JSON payload required."}), 400

        if "tokens_sold" in data:
            tokens_sold = data["tokens_sold"]
            if not isinstance(tokens_sold, int) or tokens_sold < 0:
                return jsonify({"error": "Invalid 'tokens_sold' value. Must be a non-negative integer."}), 400
            TOKEN_SALE_DATA["tokens_sold"] = tokens_sold

        if "exchange_rate" in data:
            exchange_rate = data["exchange_rate"]
            if not isinstance(exchange_rate, (int, float)) or exchange_rate <= 0:
                return jsonify({"error": "Invalid 'exchange_rate' value. Must be a positive number."}), 400
            TOKEN_SALE_DATA["exchange_rate"] = exchange_rate

        return jsonify({"message": "Token sale data updated successfully."}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while updating token sale data.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
