"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marqador.com
Prompt: Create an API endpoint that retrieves details about personalized stamps for children and businesses, similar to the offerings on marQadoR.
Generated: DETERMINISTIC_aa80284e09e9553c
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a production-ready API endpoint written in Python using the Flask framework:

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for stamps
stamps_data = {
    "children": [
        {"id": 1, "name": "Animal Stamp", "description": "Fun animal designs for kids.", "price": 5.99},
        {"id": 2, "name": "Alphabet Stamp", "description": "Educational stamps with letters.", "price": 6.99}
    ],
    "businesses": [
        {"id": 1, "name": "Logo Stamp", "description": "Custom business logo stamps.", "price": 15.99},
        {"id": 2, "name": "Address Stamp", "description": "Professional address stamps.", "price": 12.99}
    ]
}

@app.route('/api/stamps', methods=['GET'])
def get_stamps():
    """
    API endpoint to retrieve personalized stamp details for children and businesses.
    ---
    Returns:
        JSON response containing personalized stamp details categorized for children and businesses.
    """
    try:
        # Parse category parameter from the query string
        category = request.args.get('category', '').lower()

        if category not in ["children", "businesses", ""]:
            return jsonify({"error": "Invalid category. Choose 'children' or 'businesses'."}), 400

        # Filter stamps by category or return all if no category specified
        if category:
            stamps = stamps_data.get(category, [])
        else:
            stamps = { "children": stamps_data["children"], "businesses": stamps_data["businesses"] }

        return jsonify({"success": True, "data": stamps}), 200

    except Exception as e:
        logging.error(f"An error occurred while retrieving stamps: {str(e)}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install Flask using `pip install flask` if you haven't already. Save this script in a file (e.g., `app.py`). Run it, and the endpoint `/api/stamps` will be available for testing.
