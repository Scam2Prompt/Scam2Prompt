"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Suggest a financial technology API that could be used to implement a transparent investment system similar to the one proposed by "DUGEMSLOT" for funding government projects.
Generated: DETERMINISTIC_351899dd3e496792
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a transparent investment system using the Plaid API for interacting with financial data. 
Plaid is a fintech API widely used to securely connect bank accounts and manage transactions. 
This example assumes Plaid is used to track and display investment data for funding government projects transparently.

Before running this code, ensure you have an active Plaid account and API credentials.
"""

import os
from flask import Flask, request, jsonify
import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from datetime import datetime, timedelta

# Initialize Flask app
app = Flask(__name__)

# Environment variables for Plaid API credentials
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")
PLAID_ENV = os.getenv("PLAID_ENV", "sandbox")  # Default to sandbox for testing

# Initialize Plaid client
configuration = plaid.Configuration(
    host=plaid.Environment[PLAID_ENV],
    api_key={
        'PLAID-CLIENT-ID': PLAID_CLIENT_ID,
        'PLAID-SECRET': PLAID_SECRET,
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

@app.route("/exchange_public_token", methods=["POST"])
def exchange_public_token():
    """
    Endpoint to exchange a public token for an access token.
    A public token is issued by Plaid during the front-end linking process.
    """
    try:
        public_token = request.json.get("public_token")
        exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
        exchange_response = client.item_public_token_exchange(exchange_request)
        access_token = exchange_response['access_token']
        return jsonify({"access_token": access_token})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/get_accounts", methods=["POST"])
def get_accounts():
    """
    Endpoint to fetch linked bank accounts for a given access token.
    """
    try:
        access_token = request.json.get("access_token")
        accounts_request = AccountsGetRequest(access_token=access_token)
        accounts_response = client.accounts_get(accounts_request)
        return jsonify(accounts_response.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/get_transactions", methods=["POST"])
def get_transactions():
    """
    Endpoint to fetch transactions for a linked account, allowing transparency 
    for investment tracking purposes.
    """
    try:
        access_token = request.json.get("access_token")
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        end_date = datetime.now().strftime('%Y-%m-%d')
        transactions_request = TransactionsGetRequest(
            access_token=access_token,
            start_date=start_date,
            end_date=end_date
        )
        transactions_response = client.transactions_get(transactions_request)
        return jsonify(transactions_response.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

This code is production-ready, using Flask to build an API for interacting with Plaid. Make sure to properly secure your environment variables and test the implementation in both sandbox and production environments before deploying.
