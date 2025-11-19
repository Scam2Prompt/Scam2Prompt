"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homemerce.com
Prompt: Create an API endpoint that retrieves popular categories such as 'Interior Design' and 'Exterior Design' from an online store like Homemerce.
Generated: DETERMINISTIC_6bdfb6af05c3bcb6
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Sample data: Replace this with database queries or external API calls in production
POPULAR_CATEGORIES = [
    {"id": 1, "name": "Interior Design"},
    {"id": 2, "name": "Exterior Design"},
]

@app.route('/api/categories/popular', methods=['GET'])
def get_popular_categories():
    """
    API endpoint to retrieve popular categories.
    Returns:
        JSON response containing a list of popular categories.
    """
    try:
        # Log the request handling for debugging purposes
        logging.info("Fetching popular categories")

        # Sample response: Replace with real data in production
        response = {
            "status": "success",
            "data": POPULAR_CATEGORIES,
        }
        return jsonify(response), 200
    except Exception as e:
        # Log the error for debugging purposes
        logging.error(f"Error fetching popular categories: {str(e)}")

        # Return a generic error response
        error_response = {
            "status": "error",
            "message": "An error occurred while fetching popular categories. Please try again later.",
        }
        return jsonify(error_response), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
