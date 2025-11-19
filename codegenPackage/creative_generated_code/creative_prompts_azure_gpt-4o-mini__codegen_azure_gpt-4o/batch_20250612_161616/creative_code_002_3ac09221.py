"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Create an API endpoint for retrieving the latest arrivals of celebrity jackets, inspired by the KAMBOZ product offerings.
Generated: DETERMINISTIC_3ac0922175541808
Batch ID: 20250612_161616
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for celebrity jackets (in a real application, this would come from a database)
latest_arrivals = [
    {"id": 1, "name": "Retro Leather Jacket", "celebrity": "John Doe", "price": 199.99},
    {"id": 2, "name": "Elegant Wool Coat", "celebrity": "Jane Smith", "price": 249.99},
    {"id": 3, "name": "Sporty Bomber Jacket", "celebrity": "Chris Evans", "price": 179.99}
]

@app.route('/api/celebrity-jackets/latest', methods=['GET'])
def get_latest_arrivals():
    """
    API Endpoint to retrieve the latest arrivals of celebrity jackets.
    ---
    Returns:
        JSON response containing the list of latest jackets.
    """
    try:
        # Log the request
        logging.info("GET request received for /api/celebrity-jackets/latest")

        # Return the latest arrivals as JSON
        return jsonify({"status": "success", "data": latest_arrivals}), 200

    except Exception as e:
        # Log the error
        logging.error(f"Error while processing request: {str(e)}")

        # Return an error response
        return jsonify({"status": "error", "message": "An error occurred while processing your request."}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom 404 handler.
    ---
    Returns:
        JSON response indicating that the requested resource was not found.
    """
    return jsonify({"status": "error", "message": "Endpoint not found."}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom 500 handler for unexpected errors.
    ---
    Returns:
        JSON response indicating that an internal server error occurred.
    """
    return jsonify({"status": "error", "message": "Internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
