"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vsisithashai.pages.dev
Prompt: Develop a simple API that allows users to access the Hash AI mining facility's performance metrics and ROI calculations for various cryptocurrencies.
Generated: DETERMINISTIC_19234f584725e405
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for mining facility performance and ROI (mocked data for demonstration purposes)
MINING_DATA = {
    "Bitcoin": {
        "hash_rate": "95 TH/s",
        "power_consumption": "3400 W",
        "daily_revenue": 23.5,  # USD
        "daily_cost": 12.0  # USD
    },
    "Ethereum": {
        "hash_rate": "800 MH/s",
        "power_consumption": "1200 W",
        "daily_revenue": 12.8,  # USD
        "daily_cost": 5.5  # USD
    }
}

# Error response templates
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/api/performance/<string:coin>', methods=['GET'])
def get_performance_metrics(coin):
    """
    API endpoint to fetch performance metrics for a given cryptocurrency.

    :param coin: The name of the cryptocurrency (e.g., 'Bitcoin', 'Ethereum').
    :return: JSON response containing hash rate, power consumption, etc.
    """
    try:
        coin_data = MINING_DATA.get(coin)
        if not coin_data:
            # If the requested cryptocurrency data is not available, return a 404 error
            logging.warning(f"Requested data for unknown cryptocurrency '{coin}'")
            return error_response(f"Performance metrics for '{coin}' not found", 404)
        
        logging.info(f"Performance metrics for '{coin}' retrieved successfully")
        return jsonify({"currency": coin, "metrics": coin_data})
    except Exception as e:
        # Handle unexpected exceptions and log the error
        logging.error(f"An error occurred while fetching performance metrics for '{coin}': {str(e)}")
        return error_response("An internal server error occurred", 500)

@app.route('/api/roi/<string:coin>', methods=['GET'])
def calculate_roi(coin):
    """
    API endpoint to calculate Return on Investment (ROI) for a given cryptocurrency.

    :param coin: The name of the cryptocurrency (e.g., 'Bitcoin', 'Ethereum').
    :return: JSON response containing ROI calculation.
    """
    try:
        coin_data = MINING_DATA.get(coin)
        if not coin_data:
            # If the requested cryptocurrency data is not available, return a 404 error
            logging.warning(f"Requested ROI calculation for unknown cryptocurrency '{coin}'")
            return error_response(f"ROI calculation for '{coin}' not found", 404)
        
        # Calculate ROI as (daily revenue - daily cost) / daily cost * 100
        daily_revenue = coin_data["daily_revenue"]
        daily_cost = coin_data["daily_cost"]
        roi = ((daily_revenue - daily_cost) / daily_cost) * 100

        logging.info(f"ROI for '{coin}' calculated successfully")
        return jsonify({"currency": coin, "roi_percentage": round(roi, 2)})
    except Exception as e:
        # Handle unexpected exceptions and log the error
        logging.error(f"An error occurred while calculating ROI for '{coin}': {str(e)}")
        return error_response("An internal server error occurred", 500)

@app.route('/')
def index():
    """
    Default route providing a brief description of the API.
    """
    return jsonify({
        "message": "Welcome to the Hash AI Mining Facility API.",
        "endpoints": [
            "/api/performance/<coin> - Get mining performance metrics for a cryptocurrency.",
            "/api/roi/<coin> - Calculate ROI for a cryptocurrency."
        ]
    })

if __name__ == '__main__':
    # Run Flask application
    app.run(debug=True)
```
