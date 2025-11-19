"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaptimizer.com
Prompt: Develop an API endpoint to retrieve the latest promotions and bonuses for members of an online gambling platform, similar to those offered by HOLYWIN69.
Generated: DETERMINISTIC_10002293c9127a5c
Batch ID: 20250612_135736
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

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Sample data representing promotions and bonuses for members
PROMOTIONS = [
    {"id": 1, "title": "Welcome Bonus", "description": "Get a 100% match on your first deposit!", "valid_until": "2023-12-31"},
    {"id": 2, "title": "Weekly Cashback", "description": "Enjoy 10% cashback every Monday!", "valid_until": "2023-11-30"},
    {"id": 3, "title": "VIP Program", "description": "Exclusive rewards for VIP members.", "valid_until": "2024-01-15"},
]

@app.route('/api/promotions', methods=['GET'])
def get_promotions():
    """
    API Endpoint to retrieve the latest promotions and bonuses.
    
    Returns:
        JSON response containing the list of promotions.
    """
    try:
        logging.info("Request received to fetch promotions.")
        
        # Check for optional query parameters (e.g., filtering promotions)
        valid_until = request.args.get('valid_until')
        if valid_until:
            filtered_promotions = [
                promo for promo in PROMOTIONS if promo['valid_until'] <= valid_until
            ]
            response = {"status": "success", "data": filtered_promotions}
        else:
            response = {"status": "success", "data": PROMOTIONS}

        logging.info("Promotions successfully retrieved.")
        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"An error occurred: {str(e)}")
        response = {"status": "error", "message": "An unexpected error occurred. Please try again later."}
        return jsonify(response), 500


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    response = {"status": "error", "message": "Endpoint not found."}
    return jsonify(response), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for server issues.
    """
    response = {"status": "error", "message": "An internal server error occurred."}
    return jsonify(response), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
