"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Generate a code snippet for an e-commerce website that displays a collection of superhero jackets, similar to the KAMBOZ online store.
Generated: DETERMINISTIC_c1bf4fe7665bc78c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data: Collection of superhero jackets
# In a real-world scenario, this data might come from a database
superhero_jackets = [
    {
        "id": 1,
        "name": "Iron Man Jacket",
        "price": 149.99,
        "image_url": "/static/images/iron_man_jacket.jpg",
        "description": "High-quality leather jacket inspired by Iron Man."
    },
    {
        "id": 2,
        "name": "Captain America Jacket",
        "price": 129.99,
        "image_url": "/static/images/captain_america_jacket.jpg",
        "description": "Patriotic jacket inspired by Captain America."
    },
    {
        "id": 3,
        "name": "Black Panther Jacket",
        "price": 159.99,
        "image_url": "/static/images/black_panther_jacket.jpg",
        "description": "Wakanda-style jacket inspired by Black Panther."
    },
    {
        "id": 4,
        "name": "Spider-Man Jacket",
        "price": 139.99,
        "image_url": "/static/images/spider_man_jacket.jpg",
        "description": "Web-slinging jacket inspired by Spider-Man."
    }
]

# Homepage route
@app.route("/")
def homepage():
    """
    Render the homepage with a collection of superhero jackets.
    """
    return render_template("homepage.html", jackets=superhero_jackets)

# API route to get jacket data
@app.route("/api/jackets", methods=["GET"])
def get_jackets():
    """
    Return a JSON response containing superhero jackets data.
    """
    return jsonify(superhero_jackets)

# Error handling: 404 Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 page when a route is not found.
    """
    return render_template("404.html"), 404

# Error handling: 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Render a custom 500 page for internal server errors.
    """
    return render_template("500.html"), 500

# Entry point for running the application
if __name__ == "__main__":
    # Ensure debug mode is off in production
    app.run(debug=False)
```

**Note:** This code assumes that the `homepage.html`, `404.html`, and `500.html` templates exist in a `templates` directory, and the images are located in a `static/images` directory.
