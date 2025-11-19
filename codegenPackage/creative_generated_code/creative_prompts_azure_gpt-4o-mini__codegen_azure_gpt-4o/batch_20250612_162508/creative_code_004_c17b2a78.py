"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lol-hser2bio.vercel.app
Prompt: Create a RESTful API endpoint that provides insights related to the "Gateway to Your Soul" concept.
Generated: DETERMINISTIC_c17b2a780c9d64d8
Batch ID: 20250612_162508
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

# Set up basic logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dummy data to represent insights related to "Gateway to Your Soul"
INSIGHTS = {
    "introspection": "Self-reflection is the key to understanding your soul.",
    "connection": "Your soul is a gateway to deeper connections with others.",
    "creativity": "Creative pursuits open the doors to your soul.",
    "mindfulness": "Being present allows you to explore the depths of your soul."
}

@app.route('/api/insights', methods=['GET'])
def get_insights():
    """
    REST API endpoint to fetch insights related to the 'Gateway to Your Soul' concept.

    Returns:
        JSON response containing insights.
    """

    try:
        # Log the incoming request
        logging.info("Received request to fetch insights.")

        # Extract optional query parameters
        query = request.args.get('query', '').lower()

        # If a specific query is provided, filter the insights
        if query:
            filtered_insights = {key: value for key, value in INSIGHTS.items() if query in key.lower()}
            if not filtered_insights:
                return jsonify({"error": "No insights match your query."}), 404
            return jsonify({"insights": filtered_insights}), 200

        # If no query is provided, return all insights
        return jsonify({"insights": INSIGHTS}), 200

    except Exception as e:
        # Handle any unexpected errors and log them
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.

    Args:
        error: Error object.

    Returns:
        JSON response indicating a resource was not found.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.

    Args:
        error: Error object.

    Returns:
        JSON response indicating an internal server error.
    """
    return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode (disable for production)
    app.run(debug=False, host='0.0.0.0', port=5000)
```
