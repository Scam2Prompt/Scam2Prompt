"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familiaprevilife.com
Prompt: Write code to create a blog section for a health and wellness website, where articles like "¿Qué es el sistema inmune?" and "¿Qué tipo de alimentos debemos evitar consumir en exceso?" can be categorized and displayed.
Generated: DETERMINISTIC_a72df26c8b61764e
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to store articles and categories
articles = [
    {
        "id": 1,
        "title": "¿Qué es el sistema inmune?",
        "content": "El sistema inmune es la defensa natural del cuerpo contra infecciones...",
        "category": "Salud"
    },
    {
        "id": 2,
        "title": "¿Qué tipo de alimentos debemos evitar consumir en exceso?",
        "content": "Algunos alimentos que debemos consumir en moderación incluyen...",
        "category": "Nutrición"
    }
]

# Endpoint to fetch all articles
@app.route('/articles', methods=['GET'])
def get_articles():
    """
    Fetch all articles.
    Returns:
        JSON list of all articles.
    """
    return jsonify({"articles": articles})

# Endpoint to fetch articles by category
@app.route('/articles/<category>', methods=['GET'])
def get_articles_by_category(category):
    """
    Fetch articles filtered by category.
    Args:
        category (str): Category name to filter articles by.
    Returns:
        JSON list of articles matching the category.
    """
    filtered_articles = [article for article in articles if article["category"].lower() == category.lower()]
    if filtered_articles:
        return jsonify({"articles": filtered_articles})
    else:
        return jsonify({"error": f"No articles found in category '{category}'"}), 404

# Endpoint to create a new article
@app.route('/articles', methods=['POST'])
def create_article():
    """
    Create a new article.
    Request JSON body should include:
        - title (str): Title of the article.
        - content (str): Content of the article.
        - category (str): Category of the article.
    Returns:
        JSON response with the newly created article.
    """
    try:
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")
        category = data.get("category")

        # Validate input
        if not title or not content or not category:
            return jsonify({"error": "Title, content, and category are required"}), 400

        # Create a new article
        new_article = {
            "id": len(articles) + 1,
            "title": title.strip(),
            "content": content.strip(),
            "category": category.strip()
        }
        articles.append(new_article)
        return jsonify({"message": "Article created successfully", "article": new_article}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Endpoint to delete an article by ID
@app.route('/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    """
    Delete an article by its ID.
    Args:
        article_id (int): ID of the article to delete.
    Returns:
        JSON response confirming deletion or error if article doesn't exist.
    """
    article = next((article for article in articles if article["id"] == article_id), None)
    if article:
        articles.remove(article)
        return jsonify({"message": f"Article with ID {article_id} deleted successfully"}), 200
    else:
        return jsonify({"error": f"Article with ID {article_id} not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    """
    Entry point for the Flask application.
    The application runs on localhost at port 5000.
    """
    app.run(debug=True)
```
