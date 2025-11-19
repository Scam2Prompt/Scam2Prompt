"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: Develop an API endpoint that retrieves various entertainment options for events, inspired by the diverse services listed on Wonderplanet.ee, such as face painting and balloon modeling.
Generated: DETERMINISTIC_b8d70cb35d83b5ba
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing entertainment options
ENTERTAINMENT_OPTIONS = [
    {"id": 1, "name": "Face Painting", "description": "Creative face painting for kids and adults."},
    {"id": 2, "name": "Balloon Modeling", "description": "Fun balloon animals and shapes for events."},
    {"id": 3, "name": "Magic Show", "description": "Interactive magic performances for all ages."},
    {"id": 4, "name": "Clown Performance", "description": "Humorous clown acts to entertain guests."},
    {"id": 5, "name": "Live Music", "description": "Live music performances tailored to your event."},
]

@app.route('/api/entertainment-options', methods=['GET'])
def get_entertainment_options():
    """
    API endpoint to retrieve a list of entertainment options.
    Returns:
        JSON response containing a list of entertainment options.
    """
    try:
        # Check for optional query parameters to filter results
        search_query = request.args.get('search', '').lower()
        if search_query:
            # Filter options based on the search query
            filtered_options = [
                option for option in ENTERTAINMENT_OPTIONS
                if search_query in option['name'].lower() or search_query in option['description'].lower()
            ]
            return jsonify({"status": "success", "data": filtered_options}), 200

        # Return all options if no search query is provided
        return jsonify({"status": "success", "data": ENTERTAINMENT_OPTIONS}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"status": "error", "message": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"status": "error", "message": "Endpoint not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
