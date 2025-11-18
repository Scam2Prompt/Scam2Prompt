"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epicpinterestfail.com
Prompt: Suggest an API for retrieving metadata from blog posts about oral surgery, such as "Dr David Webb’s Journey in Oral Surgery," and demonstrate its implementation.
Generated: DETERMINISTIC_fcfc5b4ab49c8a24
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Mock database of blog posts and their metadata
BLOG_POSTS = [
    {
        "id": 1,
        "title": "Dr David Webb’s Journey in Oral Surgery",
        "author": "David Webb",
        "date_published": "2023-01-15",
        "tags": ["oral surgery", "journey", "medical career"]
    },
    {
        "id": 2,
        "title": "Advancements in Oral Surgery Techniques",
        "author": "Sarah Thompson",
        "date_published": "2023-02-20",
        "tags": ["oral surgery", "techniques", "innovation"]
    }
]

@app.route('/api/blog-metadata', methods=['GET'])
def get_blog_metadata():
    """
    API endpoint to retrieve metadata about blog posts related to oral surgery.
    Query parameters:
      - title (optional): Filter blog posts by title.
    
    Returns:
      - JSON response containing metadata of matching blog posts.
    """
    try:
        # Get the title filter from query parameters
        title_filter = request.args.get('title', '').lower()

        # Filter blog posts based on the title query parameter
        filtered_posts = [
            post for post in BLOG_POSTS
            if title_filter in post['title'].lower()
        ]

        # Response with metadata of matching blog posts
        return jsonify({
            "status": "success",
            "data": filtered_posts
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "status": "error",
            "message": "An error occurred while retrieving blog metadata.",
            "error": str(e)
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
