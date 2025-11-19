"""
Generated Code Metadata:
========================
Original URL: https://motor-muse.com
Prompt: Create a RESTful API to manage and retrieve news articles related to electric vehicle price wars, specifically those involving Tesla in Australia.
Generated: DETERMINISTIC_5a0a2ca08c9d85ed
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for storing articles
articles = [
    {
        "id": 1,
        "title": "Tesla slashes prices in Australia amid EV price wars",
        "content": "Tesla has reduced prices for its Model 3 and Model Y in Australia, intensifying competition in the electric vehicle market.",
        "author": "John Doe",
        "date": "2023-10-01"
    },
    {
        "id": 2,
        "title": "EV price wars heat up in Australia",
        "content": "Electric vehicle manufacturers are competing fiercely in Australia, with Tesla leading the charge.",
        "author": "Jane Smith",
        "date": "2023-10-02"
    }
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to retrieve all articles
@app.route('/api/articles', methods=['GET'])
def get_articles():
    """
    Retrieve all articles related to EV price wars involving Tesla in Australia.
    """
    return jsonify(articles), 200

# Route to retrieve a single article by ID
@app.route('/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """
    Retrieve a specific article by its ID.
    """
    article = next((article for article in articles if article["id"] == article_id), None)
    if article is None:
        return jsonify({"error": "Article not found"}), 404
    return jsonify(article), 200

# Route to add a new article
@app.route('/api/articles', methods=['POST'])
def add_article():
    """
    Add a new article to the database.
    """
    data = request.get_json()
    if not data or not all(key in data for key in ("title", "content", "author", "date")):
        return jsonify({"error": "Invalid input"}), 400

    new_article = {
        "id": max(article["id"] for article in articles) + 1 if articles else 1,
        "title": data["title"],
        "content": data["content"],
        "author": data["author"],
        "date": data["date"]
    }
    articles.append(new_article)
    return jsonify(new_article), 201

# Route to update an existing article
@app.route('/api/articles/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    """
    Update an existing article by its ID.
    """
    article = next((article for article in articles if article["id"] == article_id), None)
    if article is None:
        return jsonify({"error": "Article not found"}), 404

    data = request.get_json()
    if not data or not any(key in data for key in ("title", "content", "author", "date")):
        return jsonify({"error": "Invalid input"}), 400

    article.update({key: data[key] for key in data if key in article})
    return jsonify(article), 200

# Route to delete an article by ID
@app.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    """
    Delete an article by its ID.
    """
    article = next((article for article in articles if article["id"] == article_id), None)
    if article is None:
        return jsonify({"error": "Article not found"}), 404

    articles.remove(article)
    return jsonify({"message": "Article deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
