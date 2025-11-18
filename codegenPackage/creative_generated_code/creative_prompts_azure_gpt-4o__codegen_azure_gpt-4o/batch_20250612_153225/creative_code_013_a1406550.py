"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Create a Python program using the Flask framework to showcase blog posts and services such as "Affaires de justice" and "Réussite Professionnelle," as described on the website.
Generated: DETERMINISTIC_a1406550136d6754
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)

# Sample data for blog posts and services
blog_posts = [
    {"id": 1, "title": "Understanding Justice Systems", "content": "Content about justice systems."},
    {"id": 2, "title": "Professional Success Tips", "content": "Content about achieving professional success."},
]

services = [
    {"id": 1, "name": "Affaires de Justice", "description": "Legal consulting and support services."},
    {"id": 2, "name": "Réussite Professionnelle", "description": "Career mentoring and growth strategies."},
]

@app.route("/")
def home():
    """
    Home route to display a welcome message and available endpoints.
    """
    return render_template("home.html")

@app.route("/blog-posts", methods=["GET"])
def get_blog_posts():
    """
    Endpoint to retrieve all blog posts.
    """
    return jsonify(blog_posts), 200

@app.route("/blog-posts/<int:post_id>", methods=["GET"])
def get_single_blog_post(post_id):
    """
    Endpoint to retrieve a single blog post by its ID.
    """
    post = next((post for post in blog_posts if post["id"] == post_id), None)
    if post is None:
        abort(404, description="Blog post not found.")
    return jsonify(post), 200

@app.route("/services", methods=["GET"])
def get_services():
    """
    Endpoint to retrieve all services.
    """
    return jsonify(services), 200

@app.route("/services/<int:service_id>", methods=["GET"])
def get_single_service(service_id):
    """
    Endpoint to retrieve a single service by its ID.
    """
    service = next((service for service in services if service["id"] == service_id), None)
    if service is None:
        abort(404, description="Service not found.")
    return jsonify(service), 200

# Error handlers for clean error responses
@app.errorhandler(404)
def not_found_error(e):
    """
    Handler for 404 errors.
    """
    return jsonify({"error": "Not found", "message": str(e)}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for 500 errors.
    """
    return jsonify({"error": "Internal server error", "message": "Something went wrong."}), 500

if __name__ == "__main__":
    # Run the server in debug mode for development purposes
    app.run(debug=True)

```

This code includes sample data and appropriate endpoints for retrieving blog posts and services. It also features error handling for 404 and 500 errors. To use this code in production, replace the sample data with dynamic data sources like a database.
