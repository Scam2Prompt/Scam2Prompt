"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Create a code snippet for a web application that allows users to compare different investment portfolios, including cannabis and crypto investments, as detailed by Brexphil Inc.
Generated: DETERMINISTIC_302d065559d86efc
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for comparing investment portfolios
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setup logging for production-grade error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample investment portfolio data for demonstration
investment_portfolios = {
    "portfolio_1": {"name": "Cannabis Portfolio", "assets": {"Asset_A": 3000, "Asset_B": 2000, "Asset_C": 4000}},
    "portfolio_2": {"name": "Crypto Portfolio", "assets": {"Bitcoin": 50000, "Ethereum": 3000, "Solana": 1000}},
    "portfolio_3": {"name": "Traditional Portfolio", "assets": {"Stocks": 15000, "Bonds": 10000, "ETFs": 7000}},
}

@app.route('/compare-portfolios', methods=['POST'])
def compare_portfolios():
    """
    Endpoint to compare investment portfolios based on user input.
    Request body should include portfolio IDs to compare.
    Example Request Body: {"portfolios": ["portfolio_1", "portfolio_2"]}
    """
    try:
        # Parse the request JSON
        data = request.get_json()
        if not data or 'portfolios' not in data:
            return jsonify({"error": "Invalid request. Please provide portfolio IDs to compare."}), 400
        
        portfolio_ids = data['portfolios']
        selected_portfolios = []

        # Validate and fetch the requested portfolios
        for portfolio_id in portfolio_ids:
            if portfolio_id in investment_portfolios:
                selected_portfolios.append(investment_portfolios[portfolio_id])
            else:
                return jsonify({"error": f"Portfolio ID '{portfolio_id}' not found."}), 404

        # Compare portfolios (for simplicity, calculate total asset value for each portfolio)
        comparison_result = []
        for portfolio in selected_portfolios:
            total_value = sum(portfolio['assets'].values())
            comparison_result.append({"name": portfolio["name"], "total_value": total_value})

        # Return comparison results
        return jsonify({"comparison_result": comparison_result}), 200

    except Exception as e:
        # Log and handle unexpected errors
        logging.error(f"Error occurred while comparing portfolios: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

@app.route('/portfolios', methods=['GET'])
def get_portfolios():
    """
    Endpoint to fetch all available investment portfolios.
    """
    try:
        return jsonify({"portfolios": investment_portfolios}), 200
    except Exception as e:
        logging.error(f"Error occurred while fetching portfolios: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
