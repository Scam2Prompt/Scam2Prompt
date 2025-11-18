"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basednormus.pages.dev
Prompt: Generate code for a decentralized exchange interface that supports trading tokens like `$NORMUS` with 0% transaction fees and displays tokenomics details.
Generated: DETERMINISTIC_eb63ef7ef14ce725
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample token data (in a production environment, this would come from a database or blockchain API)
TOKENS = {
    "NORMUS": {
        "symbol": "NORMUS",
        "name": "Normus Token",
        "total_supply": 1000000,
        "holders": 2500,
        "price_usd": 1.25,
        "transaction_fee_percent": 0  # 0% transaction fees
    }
}

# Helper function to fetch token data
def fetch_token_data(symbol):
    """
    Fetch token data from the TOKENS dictionary.
    :param symbol: Token symbol string
    :return: Token details or None if not found
    """
    return TOKENS.get(symbol.upper(), None)

# Endpoint: Retrieve tokenomics details
@app.route('/tokenomics/<symbol>', methods=['GET'])
def get_tokenomics(symbol):
    """
    GET /tokenomics/<symbol>
    Fetch tokenomics information for a given token symbol.
    """
    token_data = fetch_token_data(symbol)
    if not token_data:
        return jsonify({"error": "Token not found"}), 404

    return jsonify({
        "symbol": token_data["symbol"],
        "name": token_data["name"],
        "total_supply": token_data["total_supply"],
        "holders": token_data["holders"],
        "price_usd": token_data["price_usd"],
        "transaction_fee_percent": token_data["transaction_fee_percent"],
    })

# Endpoint: Perform token swap
@app.route('/swap', methods=['POST'])
def swap_token():
    """
    POST /swap
    Swap tokens between users with 0% transaction fees.
    Expected request format:
    {
        "from_address": "address1",
        "to_address": "address2",
        "token_symbol": "NORMUS",
        "amount": 100
    }
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        from_address = data.get("from_address")
        to_address = data.get("to_address")
        token_symbol = data.get("token_symbol")
        amount = data.get("amount")

        # Validate input
        if not from_address or not to_address or not token_symbol or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        if amount <= 0:
            return jsonify({"error": "Amount must be greater than zero"}), 400

        # Fetch token data
        token_data = fetch_token_data(token_symbol)
        if not token_data:
            return jsonify({"error": "Token not found"}), 404

        # Perform mock token transfer (actual implementation would interact with a blockchain)
        # For demonstration, assume transfer succeeds without fees
        return jsonify({
            "message": "Token swap successful",
            "from_address": from_address,
            "to_address": to_address,
            "token_symbol": token_symbol,
            "amount": amount,
            "transaction_fee_percent": token_data["transaction_fee_percent"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Application entry point
if __name__ == '__main__':
    app.run(debug=True)
```
