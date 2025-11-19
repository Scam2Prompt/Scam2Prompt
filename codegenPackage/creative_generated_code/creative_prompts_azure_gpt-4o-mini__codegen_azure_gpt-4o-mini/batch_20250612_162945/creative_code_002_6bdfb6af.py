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
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data simulating categories from an online store
CATEGORIES = {
    "interior_design": {
        "name": "Interior Design",
        "popularity": 95
    },
    "exterior_design": {
        "name": "Exterior Design",
        "popularity": 90
    },
    "landscaping": {
        "name": "Landscaping",
        "popularity": 85
    }
}

@app.route('/api/categories/popular', methods=['GET'])
def get_popular_categories():
    """
    API endpoint to retrieve popular categories from the store. 
    Returns a JSON response with the list of categories.

    Returns:
        JSON response containing popular categories.
    """
    try:
        # Filter categories based on popularity threshold
        popular_categories = {key: value for key, value in CATEGORIES.items() if value['popularity'] > 80}
        
        # Log the retrieval of popular categories
        logging.info("Retrieved popular categories successfully.")

        return jsonify(popular_categories), 200

    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Error retrieving popular categories: {str(e)}")
        return jsonify({"error": "Unable to retrieve popular categories."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
