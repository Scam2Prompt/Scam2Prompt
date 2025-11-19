"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jm4-dapp.pages.dev
Prompt: Create an API call to enable buying and selling of DApps on mobile wallets as described in the content.
Generated: DETERMINISTIC_d61b749a4d9c27df
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Mock database for storing DApp buy/sell data
mock_dapp_marketplace = {
    "dapps": [
        {"id": 1, "name": "DApp1", "price": 10, "status": "available"},
        {"id": 2, "name": "DApp2", "price": 20, "status": "available"},
    ]
}

@app.route('/api/dapp/buy', methods=['POST'])
def buy_dapp():
    """
    Endpoint to buy a DApp.
    Request payload: {"dapp_id": <int>, "wallet_address": <string>}
    Response: JSON object with success status and details.
    """
    try:
        data = request.get_json()
        dapp_id = data['dapp_id']
        wallet_address = data['wallet_address']

        # Validate input data
        if not dapp_id or not wallet_address:
            return jsonify({"error": "Invalid input, dapp_id and wallet_address are required"}), 400

        # Check if the DApp is available
        dapp = next((item for item in mock_dapp_marketplace["dapps"] if item["id"] == dapp_id), None)
        if not dapp or dapp["status"] != "available":
            return jsonify({"error": "DApp not available for purchase"}), 404

        # Simulate the purchase process (e.g., updating the status to sold)
        dapp["status"] = "sold"

        # Return success response
        return jsonify({"message": f"Successfully purchased {dapp['name']}!", "wallet_address": wallet_address}), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/api/dapp/sell', methods=['POST'])
def sell_dapp():
    """
    Endpoint to sell a DApp.
    Request payload: {"dapp_name": <string>, "price": <float>}
    Response: JSON object with success status and details.
    """
    try:
        data = request.get_json()
        dapp_name = data['dapp_name']
        price = data['price']

        # Validate input data
        if not dapp_name or not price or price <= 0:
            return jsonify({"error": "Invalid input, dapp_name and positive price are required"}), 400

        # Add the DApp to the marketplace
        new_dapp = {
            "id": len(mock_dapp_marketplace["dapps"]) + 1,
            "name": dapp_name,
            "price": price,
            "status": "available"
        }
        mock_dapp_marketplace["dapps"].append(new_dapp)

        # Return success response
        return jsonify({"message": f"Successfully listed {dapp_name} for sale!", "dapp_id": new_dapp["id"]}), 201

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/api/dapp/list', methods=['GET'])
def list_dapps():
    """
    Endpoint to list all DApps in the marketplace.
    No request payload.
    Response: JSON object with details of all DApps.
    """
    try:
        # Return all DApps in the marketplace
        return jsonify({"dapps": mock_dapp_marketplace["dapps"]}), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
