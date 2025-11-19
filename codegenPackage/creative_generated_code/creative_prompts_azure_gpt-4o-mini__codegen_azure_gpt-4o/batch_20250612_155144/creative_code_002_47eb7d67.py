"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Generate a code snippet for an API that allows users to access private equity investment opportunities, similar to those provided by Grade World Investment Limited.
Generated: DETERMINISTIC_47eb7d67b0f6c3ee
Batch ID: 20250612_155144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Mock data for private equity investment opportunities
investment_opportunities = [
    {"id": 1, "name": "Tech Startup Fund", "description": "Invest in early-stage tech startups.", "minimum_investment": 100000, "currency": "USD"},
    {"id": 2, "name": "Real Estate Growth Fund", "description": "Invest in commercial real estate projects.", "minimum_investment": 50000, "currency": "USD"},
    {"id": 3, "name": "Healthcare Innovation Fund", "description": "Invest in cutting-edge healthcare solutions.", "minimum_investment": 150000, "currency": "USD"}
]

# Error messages for consistent API responses
ERROR_MESSAGES = {
    "not_found": "Investment opportunity not found.",
    "invalid_id": "Invalid ID provided.",
    "internal_error": "An internal error occurred."
}


@app.route('/api/investments', methods=['GET'])
def get_investment_opportunities():
    """
    Endpoint to fetch all private equity investment opportunities.
    Accessible via: GET /api/investments
    """
    try:
        logging.info("Fetching investment opportunities.")
        return jsonify({"status": "success", "data": investment_opportunities}), 200
    except Exception as e:
        logging.error(f"Error fetching investment opportunities: {str(e)}")
        return jsonify({"status": "error", "message": ERROR_MESSAGES["internal_error"]}), 500


@app.route('/api/investments/<int:investment_id>', methods=['GET'])
def get_investment_opportunity(investment_id):
    """
    Endpoint to fetch a specific investment opportunity by ID.
    Accessible via: GET /api/investments/<investment_id>
    """
    try:
        logging.info(f"Fetching investment opportunity with ID: {investment_id}")
        opportunity = next((item for item in investment_opportunities if item["id"] == investment_id), None)
        
        if opportunity:
            return jsonify({"status": "success", "data": opportunity}), 200
        else:
            logging.warning(f"Investment opportunity with ID {investment_id} not found.")
            return jsonify({"status": "error", "message": ERROR_MESSAGES["not_found"]}), 404
    except ValueError:
        logging.error(f"Invalid ID provided: {investment_id}")
        return jsonify({"status": "error", "message": ERROR_MESSAGES["invalid_id"]}), 400
    except Exception as e:
        logging.error(f"Error fetching investment opportunity: {str(e)}")
        return jsonify({"status": "error", "message": ERROR_MESSAGES["internal_error"]}), 500


@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    """
    logging.warning("Route not found.")
    return jsonify({"status": "error", "message": "Route not found."}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    logging.error("Internal server error.")
    return jsonify({"status": "error", "message": ERROR_MESSAGES["internal_error"]}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
