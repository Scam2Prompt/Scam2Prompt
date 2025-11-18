"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismdashboard.xyz
Prompt: Develop a web application that integrates with Moralis API to track wallet activity and token transfers on the Optimism blockchain.
Generated: DETERMINISTIC_41a5a3d34f048c0f
Batch ID: 20250612_151932
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://deep-index.moralis.io/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify
import requests
import os

# Flask Web Application Initialization
app = Flask(__name__)

# Load Moralis API Key from Environment Variables
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")
if not MORALIS_API_KEY:
    raise RuntimeError("MORALIS_API_KEY environment variable is not set.")

# Moralis API Base URL for Optimism Blockchain
MORALIS_API_URL = "https://deep-index.moralis.io/api/v2"

# Helper Function: Fetch Wallet Activity
def get_wallet_activity(wallet_address):
    """
    Fetches wallet activity including token transactions for a given address on the Optimism blockchain.

    Args:
        wallet_address (str): Wallet address to fetch transactions for.

    Returns:
        dict: JSON response from Moralis API.
    """
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": MORALIS_API_KEY,
    }
    url = f"{MORALIS_API_URL}/{wallet_address}/erc20/transfers"
    params = {"chain": "optimism"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Successful response JSON
    except requests.exceptions.RequestException as e:
        # Handle API errors gracefully
        return {"error": str(e), "message": "Failed to fetch wallet activity"}

# API Route: Home/Health Check
@app.route("/", methods=["GET"])
def home():
    """
    Health check endpoint for the API.
    """
    return jsonify({"message": "Wallet Activity Tracker for Optimism Blockchain", "status": "running"})

# API Route: Wallet Activity
@app.route("/wallet/<wallet_address>", methods=["GET"])
def wallet_activity(wallet_address):
    """
    API endpoint to get wallet activity for a specified wallet address.

    Args:
        wallet_address (str): Wallet address from the URL parameter.

    Returns:
        JSON: Wallet activity or error message.
    """
    if not wallet_address:
        return jsonify({"error": "Wallet address is required"}), 400

    # Fetch wallet activity using helper function
    data = get_wallet_activity(wallet_address)
    return jsonify(data)

# Error Handling for Invalid Routes
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for unsupported routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Error Handling for Internal Server Errors
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for internal server issues.
    """
    return jsonify({"error": "An internal server error occurred"}), 500

# Run Application
if __name__ == "__main__":
    # Flask application runs in debug mode; disable debug mode for production
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Notes:
- Set the `MORALIS_API_KEY` environment variable with your Moralis API key before running the application.
- Install required dependencies with `pip install flask requests`.
- This code is structured to ensure readability, maintainability, and error handling for production use.
