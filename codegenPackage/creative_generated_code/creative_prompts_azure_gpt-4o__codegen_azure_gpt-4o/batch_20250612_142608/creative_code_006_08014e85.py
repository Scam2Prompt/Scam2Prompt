"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrvm.dev
Prompt: Generate a RESTful API request to retrieve portfolio data for SOLANA and CARDANO assets tracked by the BLOCKCHAIN app.
Generated: DETERMINISTIC_08014e85e563220a
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock portfolio data for demonstration purposes
PORTFOLIO_DATA = {
    "SOLANA": {
        "asset_name": "Solana",
        "symbol": "SOL",
        "quantity": 100,
        "current_value_usd": 2200.00
    },
    "CARDANO": {
        "asset_name": "Cardano",
        "symbol": "ADA",
        "quantity": 500,
        "current_value_usd": 1500.00
    }
}

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    """
    Endpoint to retrieve portfolio data for specified assets.
    Query parameters:
      - assets (comma-separated): List of asset names (e.g., "SOLANA,CARDANO")
    Returns:
      JSON response containing portfolio data for the requested assets.
    """
    # Extract query parameter from URL
    assets_param = request.args.get('assets')
    if not assets_param:
        abort(400, description="Missing 'assets' query parameter")

    # Parse assets from query parameter and validate existence
    requested_assets = assets_param.split(',')
    portfolio_response = {}
    for asset in requested_assets:
        asset_upper = asset.strip().upper()
        if asset_upper in PORTFOLIO_DATA:
            portfolio_response[asset_upper] = PORTFOLIO_DATA[asset_upper]
        else:
            portfolio_response[asset_upper] = {"error": f"Asset '{asset_upper}' not found"}

    # Return portfolio data as JSON
    return jsonify(portfolio_response)

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    """
    Custom error handler for 400 Bad Request errors.
    Returns:
      JSON response with error message.
    """
    response = jsonify({"error": error.description})
    response.status_code = 400
    return response

# Entry point to start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
