"""
Generated Code Metadata:
========================
Original URL: https://91cangkuahh82hgf332b.buzz
Prompt: "Create a simple API to recommend adult videos based on user ratings and preferences."
Generated: DETERMINISTIC_a72e193182b7e29f
Batch ID: 20250622_211508
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

# Sample data: A list of videos with ratings and tags
videos = [
    {"id": 1, "title": "Video A", "rating": 4.5, "tags": ["action", "thriller"]},
    {"id": 2, "title": "Video B", "rating": 4.0, "tags": ["romance", "drama"]},
    {"id": 3, "title": "Video C", "rating": 3.5, "tags": ["comedy", "action"]},
    {"id": 4, "title": "Video D", "rating": 5.0, "tags": ["thriller", "horror"]},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/recommend', methods=['POST'])
def recommend_videos():
    """
    Endpoint to recommend videos based on user preferences.
    Expects a JSON payload with 'min_rating' and 'tags' fields.
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Extract user preferences
        min_rating = data.get("min_rating", 0)
        tags = data.get("tags", [])

        # Validate input
        if not isinstance(min_rating, (int, float)) or not isinstance(tags, list):
            return jsonify({"error": "Invalid input format"}), 400

        # Filter videos based on preferences
        recommended = [
            video for video in videos
            if video["rating"] >= min_rating and any(tag in video["tags"] for tag in tags)
        ]

        # Return recommendations
        return jsonify({"recommended_videos": recommended}), 200

    except Exception as e:
        # Log the error (in production, use a logging library)
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
