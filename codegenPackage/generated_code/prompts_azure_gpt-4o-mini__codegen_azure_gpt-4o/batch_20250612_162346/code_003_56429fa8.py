"""
Generated Code Metadata:
========================
Original URL: https://gapkindo.org
Prompt: Develop a REST API that provides access to rubber price statistics and trends as outlined by GAPKINDO for developers interested in the rubber market.
Generated: DETERMINISTIC_56429fa8cc206200
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Sample data for rubber price statistics
rubber_prices = [
    {"date": "2023-10-01", "price_per_kg": 1.5},
    {"date": "2023-10-02", "price_per_kg": 1.6},
    {"date": "2023-10-03", "price_per_kg": 1.55},
    {"date": "2023-10-04", "price_per_kg": 1.7},
    {"date": "2023-10-05", "price_per_kg": 1.65},
]

# Helper function to calculate trends
def calculate_trend(prices):
    if len(prices) < 2:
        return "No trend data available"
    return "Increasing" if prices[-1] > prices[0] else "Decreasing"

@app.route('/api/rubber-prices', methods=['GET'])
def get_rubber_prices():
    """
    Endpoint to retrieve all rubber price statistics.
    """
    try:
        return jsonify({"data": rubber_prices}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rubber-prices/trend', methods=['GET'])
def get_rubber_price_trend():
    """
    Endpoint to retrieve the trend of rubber prices.
    """
    try:
        prices = [entry["price_per_kg"] for entry in rubber_prices]
        trend = calculate_trend(prices)
        return jsonify({"trend": trend}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rubber-prices', methods=['POST'])
def add_rubber_price():
    """
    Endpoint to add a new rubber price entry.
    Expects JSON payload with 'date' and 'price_per_kg'.
    """
    try:
        data = request.get_json()
        if not data or "date" not in data or "price_per_kg" not in data:
            return jsonify({"error": "Invalid input. 'date' and 'price_per_kg' are required."}), 400
        
        # Validate date format
        try:
            datetime.datetime.strptime(data["date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
        
        # Validate price
        if not isinstance(data["price_per_kg"], (int, float)) or data["price_per_kg"] <= 0:
            return jsonify({"error": "Invalid price. Must be a positive number."}), 400
        
        # Add new entry
        rubber_prices.append({"date": data["date"], "price_per_kg": data["price_per_kg"]})
        return jsonify({"message": "Rubber price added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rubber-prices/<date>', methods=['GET'])
def get_rubber_price_by_date(date):
    """
    Endpoint to retrieve rubber price for a specific date.
    """
    try:
        for entry in rubber_prices:
            if entry["date"] == date:
                return jsonify({"data": entry}), 200
        return jsonify({"error": "Rubber price not found for the given date."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
