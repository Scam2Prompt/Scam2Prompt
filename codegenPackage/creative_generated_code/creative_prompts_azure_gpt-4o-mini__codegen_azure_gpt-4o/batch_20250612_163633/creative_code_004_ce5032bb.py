"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codeflick.site
Prompt: "Provide a code snippet to implement a search feature for a blog, focusing on categories like plumbing and kitchen accessories."
Generated: DETERMINISTIC_ce5032bb6ccc7141
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)

# Sample blog data
BLOG_POSTS = [
    {"id": 1, "title": "Fixing a Leaky Faucet", "category": "plumbing", "content": "Detailed guide on fixing a leaky faucet."},
    {"id": 2, "title": "Top 10 Kitchen Accessories", "category": "kitchen accessories", "content": "A list of must-have kitchen tools."},
    {"id": 3, "title": "Unclogging Drains", "category": "plumbing", "content": "Tips and tricks for unclogging your drains."},
    {"id": 4, "title": "Organizing Your Kitchen", "category": "kitchen accessories", "content": "Ideas to organize your kitchen effectively."},
]

def search_posts_by_category(category: str) -> List[Dict]:
    """
    Search for blog posts by category.

    Args:
        category (str): The category to filter blog posts.

    Returns:
        List[Dict]: A list of blog posts that match the specified category.
    """
    # Filter blog posts by the given category
    return [post for post in BLOG_POSTS if post["category"].lower() == category.lower()]

@app.route('/search', methods=['GET'])
def search():
    """
    API endpoint to search blog posts by category.

    Query Parameter:
        category (str): The category to search for.

    Returns:
        JSON response containing matching blog posts or an error message.
    """
    category = request.args.get('category')
    if not category:
        # Return error if the category is not provided
        return jsonify({"error": "Category parameter is required."}), 400

    # Search for posts in the specified category
    results = search_posts_by_category(category)
    
    if not results:
        # Return an empty response if no posts match the category
        return jsonify({"message": "No blog posts found for the specified category."}), 404

    # Return matching posts
    return jsonify({"posts": results}), 200

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
