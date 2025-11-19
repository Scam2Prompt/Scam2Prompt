"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Generate a code snippet that implements an interactive warning system for mobile devices, focusing on product-specific alerts and safety notifications.
Generated: DETERMINISTIC_8e074cb7d5bb3ecc
Batch ID: 20250612_163835
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

# Sample configuration for product-specific alerts
PRODUCT_ALERTS = {
    "productA": {
        "warnings": [
            "Update available: Version 2.1.0",
            "Battery overheating detected. Please charge device in a cool place."
        ],
        "safety_notifications": [
            "Avoid exposing device to extreme temperatures.",
            "Ensure the device is kept away from water."
        ]
    },
    "productB": {
        "warnings": [
            "New safety alert: Check for loose components.",
            "Software malfunction detected. Please restart your device."
        ],
        "safety_notifications": [
            "Keep the device out of reach of children.",
            "Use only certified chargers."
        ]
    }
}

@app.route('/get_alerts', methods=['GET'])
def get_alerts():
    """
    Retrieves product-specific alerts and safety notifications based on the provided product ID.
    """
    product_id = request.args.get('product_id')

    if not product_id:
        # Return an error if no product ID is provided
        return jsonify({"error": "Product ID is required."}), 400

    # Fetch alerts for the given product ID
    alerts = PRODUCT_ALERTS.get(product_id)

    if alerts is None:
        # Return an error if the product ID is not recognized
        return jsonify({"error": "Product not found."}), 404

    # Return the alerts as a JSON response
    return jsonify(alerts), 200

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the application.
    """
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on localhost port 5000
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Failed to start the application: {e}")
```

This code implements a simple interactive warning system for mobile devices using Flask, where users can request product-specific alerts and safety notifications via an HTTP GET request.
