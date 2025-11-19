"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create an API endpoint that allows users to search for sports items like "Troféus" and "Medalhas" based on specific sports or activities mentioned in the blog content.
Generated: DETERMINISTIC_5b4b146731684aa3
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing blog content with sports items
BLOG_CONTENT = [
    {"id": 1, "title": "Football Trophies", "content": "Troféus for football champions."},
    {"id": 2, "title": "Running Medals", "content": "Medalhas awarded for marathon runners."},
    {"id": 3, "title": "Basketball Awards", "content": "Troféus and Medalhas for basketball players."},
    {"id": 4, "title": "Swimming Achievements", "content": "Medalhas for swimming competitions."},
]

@app.route('/search', methods=['GET'])
def search_sports_items():
    """
    API endpoint to search for sports items based on specific sports or activities.
    Query parameters:
        - query: The search term (e.g., "Troféus", "Medalhas", "Football").
    Returns:
        - JSON response with matching blog content.
    """
    try:
        # Get the search query from request arguments
        query = request.args.get('query', '').strip().lower()
        
        if not query:
            return jsonify({"error": "Query parameter is required."}), 400

        # Filter blog content based on the search query
        results = [
            item for item in BLOG_CONTENT
            if query in item['title'].lower() or query in item['content'].lower()
        ]

        # Return the results
        return jsonify({"results": results}), 200

    except HTTPException as http_err:
        # Handle HTTP exceptions
        return jsonify({"error": str(http_err)}), http_err.code

    except Exception as err:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(err)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
