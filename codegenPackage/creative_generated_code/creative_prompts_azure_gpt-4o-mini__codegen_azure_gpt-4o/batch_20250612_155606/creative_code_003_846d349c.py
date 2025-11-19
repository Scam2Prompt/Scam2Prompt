"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jnanbarta.com
Prompt: Describe how to implement a pagination feature for displaying articles, as seen in the Jnanbarta archives section.
Generated: DETERMINISTIC_846d349cede2cce0
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Pagination feature for displaying articles in Jnanbarta archives section

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data: List of articles
ARTICLES = [
    {"id": 1, "title": "Article 1", "content": "Content of Article 1"},
    {"id": 2, "title": "Article 2", "content": "Content of Article 2"},
    {"id": 3, "title": "Article 3", "content": "Content of Article 3"},
    {"id": 4, "title": "Article 4", "content": "Content of Article 4"},
    {"id": 5, "title": "Article 5", "content": "Content of Article 5"},
    # Add more articles as needed
]

# Constants for default page size and validation
DEFAULT_PAGE_SIZE = 2
MAX_PAGE_SIZE = 50

@app.route('/articles', methods=['GET'])
def get_articles():
    """
    Endpoint to retrieve paginated articles.
    Query parameters:
    - page: The page number (default is 1)
    - page_size: Number of articles per page (default is DEFAULT_PAGE_SIZE)
    """
    try:
        # Retrieve query parameters
        page = request.args.get('page', default=1, type=int)
        page_size = request.args.get('page_size', default=DEFAULT_PAGE_SIZE, type=int)

        # Validate page size to prevent excessive data fetching
        if page_size > MAX_PAGE_SIZE:
            return jsonify({"error": f"Page size cannot exceed {MAX_PAGE_SIZE}"}), 400

        # Calculate start and end indices for slicing the articles list
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size

        # Slice the articles list to get the requested page
        paginated_articles = ARTICLES[start_idx:end_idx]

        # Check if there are no articles for the requested page
        if not paginated_articles:
            return jsonify({"error": "No articles found for the requested page"}), 404

        # Construct and return the response
        response = {
            "page": page,
            "page_size": page_size,
            "total_articles": len(ARTICLES),
            "articles": paginated_articles
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
