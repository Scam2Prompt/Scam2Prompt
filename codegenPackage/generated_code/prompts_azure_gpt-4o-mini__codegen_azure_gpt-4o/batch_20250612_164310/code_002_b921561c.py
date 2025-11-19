"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Create an API endpoint that retrieves the latest nail polish collections and their prices, similar to the "Lançamentos" section on the aquarelaesmalte blog.
Generated: DETERMINISTIC_b921561cf85f749d
Batch ID: 20250612_164310
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
logging.basicConfig(level=logging.INFO)

# Mock data for nail polish collections
nail_polish_collections = [
    {"id": 1, "name": "Spring Blossom", "price": 12.99, "release_date": "2023-03-01"},
    {"id": 2, "name": "Summer Vibes", "price": 14.99, "release_date": "2023-06-15"},
    {"id": 3, "name": "Autumn Elegance", "price": 13.49, "release_date": "2023-09-10"},
    {"id": 4, "name": "Winter Sparkle", "price": 15.99, "release_date": "2023-12-01"},
]

@app.route('/api/latest-collections', methods=['GET'])
def get_latest_collections():
    """
    API endpoint to retrieve the latest nail polish collections and their prices.
    Returns:
        JSON response containing the latest collections sorted by release date.
    """
    try:
        # Sort collections by release date in descending order
        sorted_collections = sorted(nail_polish_collections, key=lambda x: x['release_date'], reverse=True)
        
        # Log the request
        logging.info("Latest collections retrieved successfully.")
        
        # Return the sorted collections as JSON
        return jsonify({"status": "success", "data": sorted_collections}), 200
    except Exception as e:
        # Log the error
        logging.error(f"Error retrieving latest collections: {str(e)}")
        
        # Return an error response
        return jsonify({"status": "error", "message": "An error occurred while retrieving the collections."}), 500

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
    Handle 500 Internal Server errors.
    """
    return jsonify({"status": "error", "message": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
