"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Illustrate how to implement a search feature in a web app that retrieves articles from the SRH Life Foundation, emphasizing personalized medicine and preventative health checks.
Generated: DETERMINISTIC_f9011282af48cac6
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Flask-based web application to implement a search feature for retrieving articles 
from the SRH Life Foundation, emphasizing personalized medicine and preventative health checks.
"""

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Dummy data - In a production app, this would be replaced with a database or external API
ARTICLES = [
    {
        "id": 1,
        "title": "Personalized Medicine: The Future of Healthcare",
        "content": "An in-depth look at how individualized treatment plans are transforming healthcare.",
        "tags": ["personalized medicine", "healthcare innovation"],
    },
    {
        "id": 2,
        "title": "Preventative Health Checks: Saving Lives",
        "content": "Why regular checkups are crucial for early detection and prevention.",
        "tags": ["preventative health", "checkups", "early detection"],
    },
    {
        "id": 3,
        "title": "Genetics and Personalized Medicine",
        "content": "The role of genetics in tailoring medical treatments for individual needs.",
        "tags": ["genetics", "personalized medicine"],
    },
]

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

@app.route('/search', methods=['GET'])
def search_articles():
    """
    Search for articles based on a query string. The search matches titles and tags.
    Example request: /search?q=personalized
    """
    try:
        # Get the query parameter from the request
        query = request.args.get('q', '').lower()  # Default to empty string if 'q' is not provided

        if not query:
            logging.warning("Search query is empty.")
            return jsonify({"error": "Search query cannot be empty."}), 400

        # Perform the search by filtering articles that match the query in title or tags
        results = [
            article for article in ARTICLES
            if query in article["title"].lower() or any(query in tag.lower() for tag in article["tags"])
        ]

        # Return the results
        if results:
            logging.info(f"Found {len(results)} articles matching the query '{query}'.")
            return jsonify({"query": query, "results": results}), 200
        else:
            logging.info(f"No articles found for the query '{query}'.")
            return jsonify({"query": query, "results": [], "message": "No articles found."}), 200

    except Exception as e:
        logging.error(f"An error occurred while searching for articles: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
