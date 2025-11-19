"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gapkindo.org
Prompt: Develop a REST API that provides access to rubber price statistics and trends as outlined by GAPKINDO for developers interested in the rubber market.
Generated: DETERMINISTIC_56429fa8cc206200
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Sample data for rubber price statistics
rubber_prices = [
    {"date": "2023-10-01", "price_per_kg": 2.5},
    {"date": "2023-10-02", "price_per_kg": 2.6},
    {"date": "2023-10-03", "price_per_kg": 2.55},
    {"date": "2023-10-04", "price_per_kg": 2.58},
]

# Utility function to calculate statistics
def calculate_statistics(data):
    prices = [entry["price_per_kg"] for entry in data]
    return {
        "average_price": sum(prices) / len(prices),
        "max_price": max(prices),
        "min_price": min(prices),
    }

# Route to get all rubber price data
@app.route("/api/rubber-prices", methods=["GET"])
def get_rubber_prices():
    """
    Returns the list of rubber prices recorded in the system.
    """
    return jsonify({"rubber_prices": rubber_prices})

# Route to get price statistics
@app.route("/api/rubber-price-statistics", methods=["GET"])
def get_rubber_price_statistics():
    """
    Returns statistics (average, max, min) of rubber prices.
    """
    try:
        stats = calculate_statistics(rubber_prices)
        return jsonify({"statistics": stats})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get rubber price trends
@app.route("/api/rubber-price-trends", methods=["GET"])
def get_rubber_price_trends():
    """
    Returns trends in rubber prices (e.g., daily changes).
    """
    try:
        trends = []
        for i in range(1, len(rubber_prices)):
            prev_day = rubber_prices[i - 1]
            curr_day = rubber_prices[i]
            daily_change = curr_day["price_per_kg"] - prev_day["price_per_kg"]
            trends.append({
                "date": curr_day["date"],
                "daily_change": daily_change,
                "trend": "up" if daily_change > 0 else "down" if daily_change < 0 else "stable"
            })
        return jsonify({"trends": trends})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add rubber price data
@app.route("/api/rubber-prices", methods=["POST"])
def add_rubber_price():
    """
    Adds a new rubber price entry. Expects JSON payload with 'date' and 'price_per_kg'.
    """
    try:
        data = request.get_json()
        if not data or "date" not in data or "price_per_kg" not in data:
            return jsonify({"error": "Invalid input. 'date' and 'price_per_kg' are required."}), 400
        
        # Validate date format
        try:
            datetime.datetime.strptime(data["date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD'."}), 400
        
        # Validate price format
        if not isinstance(data["price_per_kg"], (int, float)) or data["price_per_kg"] <= 0:
            return jsonify({"error": "Invalid price format. Must be a positive number."}), 400

        # Add new entry
        rubber_prices.append(data)
        return jsonify({"message": "Rubber price added successfully.", "data": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """
    Handles 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

# Main entry point for the application
if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
