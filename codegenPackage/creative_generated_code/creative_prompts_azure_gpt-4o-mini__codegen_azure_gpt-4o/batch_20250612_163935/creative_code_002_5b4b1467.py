"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create an API endpoint that allows users to search for sports items like "Troféus" and "Medalhas" based on specific sports or activities mentioned in the blog content.
Generated: DETERMINISTIC_5b4b146731684aa3
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data: Blog content with sports items and associated sports/activities
BLOG_CONTENT = [
    {"id": 1, "title": "Troféus de Futebol", "items": ["Troféus"], "sport": "Futebol"},
    {"id": 2, "title": "Medalhas de Natação", "items": ["Medalhas"], "sport": "Natação"},
    {"id": 3, "title": "Troféus de Basquete", "items": ["Troféus"], "sport": "Basquete"},
    {"id": 4, "title": "Medalhas de Atletismo", "items": ["Medalhas"], "sport": "Atletismo"},
]

@app.route('/search', methods=['GET'])
def search_items():
    """
    API endpoint to search for sports items based on sports or activities.
    
    Query Parameters:
    - sport: (optional) Name of the specific sport or activity to filter by.
    - item: (optional) Name of the item to filter by ("Troféus", "Medalhas", etc.).
    
    Returns:
    - JSON response with a list of matching blog content.
    """
    try:
        # Get query parameters
        sport = request.args.get('sport', '').lower()
        item = request.args.get('item', '').lower()

        # Filter blog content based on query parameters
        filtered_content = [
            blog for blog in BLOG_CONTENT
            if (sport in blog['sport'].lower() if sport else True) and
               (item in map(str.lower, blog['items']) if item else True)
        ]

        # Return filtered results
        return jsonify({"results": filtered_content}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(error):
    """
    Global error handler for HTTP exceptions.
    """
    return jsonify({"error": error.name, "details": error.description}), error.code

@app.errorhandler(404)
def page_not_found(error):
    """
    Custom error handler for 404 Not Found errors.
    """
    return jsonify({"error": "Endpoint not found", "details": "The requested URL was not found on the server."}), 404

if __name__ == '__main__':
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```
