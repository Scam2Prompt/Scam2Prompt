"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serverscoc.com
Prompt: Create a REST API in Flask that allows users to search for movies like "Gowok: Kamasutra Jawa" or "MuMu: Unspoken Love" by title and retrieve their synopsis and release date.
Generated: DETERMINISTIC_19b9e8dea767843c
Batch ID: 20250612_151525
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

# Sample movie database
movies = [
    {
        "title": "Gowok: Kamasutra Jawa",
        "synopsis": "A cultural exploration of ancient traditions in Java.",
        "release_date": "2023-01-15"
    },
    {
        "title": "MuMu: Unspoken Love",
        "synopsis": "A heartfelt tale of love and loss.",
        "release_date": "2023-02-10"
    },
    {
        "title": "Hidden Gems",
        "synopsis": "An adventure to uncover hidden treasures.",
        "release_date": "2022-11-25"
    }
]

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions with a JSON response."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    """Handle general exceptions with a JSON response."""
    response = {
        "error": "Internal Server Error",
        "description": str(e),
        "status_code": 500
    }
    return jsonify(response), 500

@app.route("/search", methods=["GET"])
def search_movies():
    """
    Search for movies by title.

    Query Parameters:
        title: The title of the movie to search for.

    Returns:
        A JSON response containing matching movies or an error message.
    """
    title_query = request.args.get('title', '').lower()

    # Validate input
    if not title_query:
        return jsonify({
            "error": "Bad Request",
            "description": "Query parameter 'title' is required.",
            "status_code": 400
        }), 400

    # Filter movies based on the title query
    matching_movies = [
        movie for movie in movies if title_query in movie["title"].lower()
    ]

    if not matching_movies:
        return jsonify({
            "message": "No movies found matching your search criteria.",
            "query": title_query
        }), 404

    return jsonify({
        "query": title_query,
        "results": matching_movies
    })

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
