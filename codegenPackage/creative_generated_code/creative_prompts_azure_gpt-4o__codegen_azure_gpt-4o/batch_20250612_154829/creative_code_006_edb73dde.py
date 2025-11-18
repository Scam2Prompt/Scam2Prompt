"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Develop an API endpoint to fetch and update mining statistics (e.g., daily earnings, profit percentages) for BTC, XRP, and SOL, using the data structure provided on the webpage.
Generated: DETERMINISTIC_edb73ddea0069ad6
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python implementation for the requested API endpoint using Flask:

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Sample data structure to store mining statistics
mining_statistics = {
    "BTC": {"daily_earnings": 0.0, "profit_percentage": 0.0},
    "XRP": {"daily_earnings": 0.0, "profit_percentage": 0.0},
    "SOL": {"daily_earnings": 0.0, "profit_percentage": 0.0}
}

@app.route('/mining-stats/<string:currency>', methods=['GET', 'PUT'])
def mining_stats(currency):
    """
    API endpoint to fetch or update mining statistics for a specific currency.
    Supported currencies: BTC, XRP, SOL
    
    Methods:
    - GET: Fetch statistics for the specified currency.
    - PUT: Update statistics for the specified currency.
    """
    # Validate currency
    if currency not in mining_statistics:
        return jsonify({"error": "Unsupported currency. Valid options are BTC, XRP, and SOL."}), 400

    if request.method == 'GET':
        # Fetch mining statistics for the specified currency
        return jsonify({"currency": currency, "statistics": mining_statistics[currency]}), 200

    elif request.method == 'PUT':
        try:
            # Parse the JSON payload from the request to update statistics
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid or missing JSON payload."}), 400
            
            # Validate and update mining statistics
            if "daily_earnings" in data:
                if isinstance(data["daily_earnings"], (int, float)):
                    mining_statistics[currency]["daily_earnings"] = data["daily_earnings"]
                else:
                    return jsonify({"error": "daily_earnings must be a number."}), 400

            if "profit_percentage" in data:
                if isinstance(data["profit_percentage"], (int, float)):
                    mining_statistics[currency]["profit_percentage"] = data["profit_percentage"]
                else:
                    return jsonify({"error": "profit_percentage must be a number."}), 400

            return jsonify({"message": "Statistics updated successfully.", "currency": currency, "statistics": mining_statistics[currency]}), 200
        
        except Exception as e:
            # Handle unexpected errors
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Entry point for running the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Notes:
- Install Flask (`pip install flask`) to run this code.
- Use the `GET` method to fetch mining statistics for `BTC`, `XRP`, or `SOL`.
- Use the `PUT` method with a JSON payload to update statistics for the currencies.
- Example JSON payload for updating statistics:
  ```json
  {
      "daily_earnings": 123.45,
      "profit_percentage": 12.34
  }
  ```
