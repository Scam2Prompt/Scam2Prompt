"""
Generated Code Metadata:
========================
Original URL: https://2857qualifications.blogspot.com
Prompt: Generate code to create a custom search function for a Blogger site.
Generated: DETERMINISTIC_2b375f1137f9e334
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample blog data (In production, this would be replaced with a database or API)
BLOG_POSTS = [
    {"id": 1, "title": "How to Learn Python", "content": "Python is a versatile programming language..."},
    {"id": 2, "title": "Flask for Beginners", "content": "Flask is a lightweight web framework for Python..."},
    {"id": 3, "title": "Advanced JavaScript Techniques", "content": "JavaScript is a powerful language for web development..."},
    {"id": 4, "title": "Understanding Databases", "content": "Databases are essential for storing structured data..."},
]

def search_blog_posts(query):
    """
    Custom search function to filter blog posts based on a query.
    :param query: The search term provided by the user.
    :return: List of blog posts that match the query.
    """
    # Ensure the query is not empty
    if not query:
        return []

    # Convert query to lowercase for case-insensitive search
    query = query.lower()

    # Filter blog posts based on whether the query appears in the title or content
    results = [
        post for post in BLOG_POSTS
        if query in post["title"].lower() or query in post["content"].lower()
    ]

    return results

@app.route('/search', methods=['GET'])
def search():
    """
    API endpoint to search blog posts.
    :return: JSON response containing the search results.
    """
    try:
        # Get the search query from the request parameters
        query = request.args.get('query', '')

        # Perform the search using the custom search function
        results = search_blog_posts(query)

        # Return the search results as a JSON response
        return jsonify({"query": query, "results": results}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
