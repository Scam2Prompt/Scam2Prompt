"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: Create an API endpoint that retrieves information about available lots, including their prices and features like basic services and green areas, for a real estate project.
Generated: DETERMINISTIC_f0d7026c61d3a5f5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for lots
lots = [
    {
        "id": 1,
        "price": 50000,
        "features": {
            "basic_services": True,
            "green_areas": True
        }
    },
    {
        "id": 2,
        "price": 45000,
        "features": {
            "basic_services": True,
            "green_areas": False
        }
    },
    {
        "id": 3,
        "price": 60000,
        "features": {
            "basic_services": True,
            "green_areas": True
        }
    }
]

@app.route('/api/lots', methods=['GET'])
def get_available_lots():
    """
    API endpoint to retrieve information about available lots.
    Returns:
        JSON response containing the list of lots with their prices and features.
    """
    try:
        # Log the request
        logging.info("Received request to fetch available lots.")
        
        # Return the list of lots as JSON
        return jsonify({"status": "success", "data": lots}), 200
    except Exception as e:
        # Log the error
        logging.error(f"An error occurred while fetching lots: {e}")
        
        # Return an error response
        return jsonify({"status": "error", "message": "An error occurred while fetching lots."}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found errors.
    """
    return jsonify({"status": "error", "message": "Endpoint not found."}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 Internal Server Error.
    """
    return jsonify({"status": "error", "message": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
