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
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing blog posts
BLOG_POSTS = [
    {"id": 1, "title": "Plumbing Tips for DIY Enthusiasts", "category": "plumbing"},
    {"id": 2, "title": "10 Must-Have Kitchen Accessories", "category": "kitchen"},
    {"id": 3, "title": "Advanced Plumbing Techniques", "category": "plumbing"},
    {"id": 4, "title": "Top Kitchen Gadgets of 2023", "category": "kitchen"},
]

@app.route('/search', methods=['GET'])
def search_blog():
    """
    Search for blog posts by category.
    
    Query Parameters:
    - category: The category to filter blog posts (e.g., plumbing, kitchen).
    
    Returns:
    - JSON response containing matching blog posts.
    """
    category = request.args.get('category')

    # Validate input
    if not category:
        return jsonify({"error": "Category parameter is required."}), 400

    # Filter blog posts by the specified category
    filtered_posts = [post for post in BLOG_POSTS if post["category"].lower() == category.lower()]

    # Check if any posts were found
    if not filtered_posts:
        return jsonify({"message": "No blog posts found for the specified category."}), 404

    return jsonify(filtered_posts), 200

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
