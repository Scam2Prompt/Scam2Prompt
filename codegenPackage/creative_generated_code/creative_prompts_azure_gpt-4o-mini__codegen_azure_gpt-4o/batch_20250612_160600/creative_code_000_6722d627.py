"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-gifts.blogspot.com
Prompt: Generate a code snippet for a gift recommendation API that suggests personalized gifts based on user preferences.
Generated: DETERMINISTIC_6722d6275565dea6
Batch ID: 20250612_160600
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

# Initialize Flask App
app = Flask(__name__)

# Configure logging for debugging and tracing errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample data for gifts and preferences
GIFTS = [
    {"id": 1, "name": "Wireless Headphones", "category": "Electronics"},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 3, "name": "Chocolate Gift Box", "category": "Food"},
    {"id": 4, "name": "Smartwatch", "category": "Electronics"},
    {"id": 5, "name": "Novel - Mystery Genre", "category": "Books"}
]

# Error messages
ERROR_MESSAGES = {
    "missing_preferences": "User preferences are required to generate recommendations.",
    "invalid_preferences": "Preferences should be a non-empty list of categories."
}

@app.route('/recommend-gifts', methods=['POST'])
def recommend_gifts():
    """
    API endpoint to recommend personalized gifts based on user preferences.
    Expects a JSON payload with 'preferences' field containing a list of categories.
    """
    try:
        # Parse JSON payload from request
        data = request.get_json()

        # Validate 'preferences' field
        if not data or 'preferences' not in data:
            logger.error("User preferences missing in request.")
            return jsonify({"error": ERROR_MESSAGES["missing_preferences"]}), 400

        preferences = data['preferences']

        if not isinstance(preferences, list) or len(preferences) == 0:
            logger.error("Invalid preferences format.")
            return jsonify({"error": ERROR_MESSAGES["invalid_preferences"]}), 400

        # Filter gifts matching user preferences
        recommended_gifts = [gift for gift in GIFTS if gift['category'] in preferences]

        return jsonify({"recommended_gifts": recommended_gifts}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        logger.exception("An unexpected error occurred.")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run Flask application only if invoked directly
if __name__ == "__main__":
    app.run(debug=True)
```
