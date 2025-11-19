"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tojsat.net
Prompt: Create a REST API endpoint that allows users to submit their research articles to an open-access journal, incorporating features similar to those found in TOJSAT's submission guidelines.
Generated: DETERMINISTIC_9250983049b7e65e
Batch ID: 20250612_161514
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

# In-memory database for simplicity (use a real database for production)
articles = []

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Custom error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e)
    }), 500

@app.route('/submit-article', methods=['POST'])
def submit_article():
    """
    Endpoint to submit a research article.
    Expects JSON data with the following keys:
    - title: Title of the research article
    - author: Author's name
    - abstract: Abstract of the research article
    - content: Full content of the research article
    - keywords: List of keywords relevant to the article
    """
    try:
        # Parse input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input", "description": "Missing JSON data"}), 400

        # Validate required fields
        required_fields = ['title', 'author', 'abstract', 'content', 'keywords']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing field '{field}'", "description": f"The field '{field}' is required"}), 400

        # Validate keywords (must be a list)
        if not isinstance(data['keywords'], list):
            return jsonify({"error": "Invalid field 'keywords'", "description": "'keywords' must be a list"}), 400

        # Save the article (for simplicity, store in memory)
        article_id = len(articles) + 1
        article = {
            "id": article_id,
            "title": data['title'],
            "author": data['author'],
            "abstract": data['abstract'],
            "content": data['content'],
            "keywords": data['keywords']
        }
        articles.append(article)

        # Respond with success
        return jsonify({
            "message": "Article submitted successfully",
            "article": article
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "description": str(e)}), 500

@app.route('/articles', methods=['GET'])
def get_articles():
    """
    Endpoint to retrieve all submitted articles.
    """
    return jsonify({"articles": articles}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
