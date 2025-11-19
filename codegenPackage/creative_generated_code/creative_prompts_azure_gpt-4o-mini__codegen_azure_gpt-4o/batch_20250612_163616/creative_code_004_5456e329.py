"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inceptiontrades.net
Prompt: Develop a simple web application that allows users to manage their multi-assets portfolio, inspired by the services provided by Inception Trades.
Generated: DETERMINISTIC_5456e329c5969cf3
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Create the Flask application
app = Flask(__name__)

# Simulated database (In-memory storage)
portfolio = []

# Error handler for invalid HTTP requests
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP errors and return a JSON response."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "message": e.description
        }
    }).data
    response.content_type = "application/json"
    return response

# Route: Home
@app.route('/')
def home():
    """Basic route to verify the app is running."""
    return jsonify({"message": "Welcome to the Portfolio Manager"}), 200

# Route: Get all assets in the portfolio
@app.route('/assets', methods=['GET'])
def get_assets():
    """Retrieve all assets in the portfolio."""
    return jsonify({"portfolio": portfolio}), 200

# Route: Add a new asset to the portfolio
@app.route('/assets', methods=['POST'])
def add_asset():
    """
    Add a new asset to the portfolio.
    Expected payload:
    {
        "type": "Stock",
        "name": "AAPL",
        "quantity": 10,
        "price": 150
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON input"}), 400

        # Validate required fields
        required_fields = {"type", "name", "quantity", "price"}
        if not required_fields.issubset(data.keys()):
            return jsonify({"error": f"Missing fields: {required_fields - data.keys()}"}), 400

        # Add asset to portfolio
        asset = {
            "id": len(portfolio) + 1,
            "type": data["type"],
            "name": data["name"],
            "quantity": data["quantity"],
            "price": data["price"]
        }
        portfolio.append(asset)
        return jsonify({"message": "Asset added successfully", "asset": asset}), 201
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route: Update an asset in the portfolio by ID
@app.route('/assets/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    """
    Update an asset in the portfolio.
    Expected payload:
    {
        "type": "Stock",
        "name": "AAPL",
        "quantity": 15,
        "price": 155
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON input"}), 400

        # Find the asset by ID
        asset = next((a for a in portfolio if a["id"] == asset_id), None)
        if not asset:
            return jsonify({"error": "Asset not found"}), 404

        # Update asset fields
        asset.update({k: v for k, v in data.items() if k in {"type", "name", "quantity", "price"}})
        return jsonify({"message": "Asset updated successfully", "asset": asset}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route: Delete an asset from the portfolio by ID
@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    """Delete an asset from the portfolio using its ID."""
    try:
        global portfolio
        initial_length = len(portfolio)
        portfolio = [asset for asset in portfolio if asset["id"] != asset_id]

        if len(portfolio) == initial_length:
            return jsonify({"error": "Asset not found"}), 404

        return jsonify({"message": "Asset deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Enable debug mode for development purposes. Set to False for production.
    app.run(debug=True)
```
