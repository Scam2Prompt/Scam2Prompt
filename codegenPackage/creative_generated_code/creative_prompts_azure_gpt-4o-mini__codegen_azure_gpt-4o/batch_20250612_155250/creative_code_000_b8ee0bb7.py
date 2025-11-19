"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Generate a code snippet for a web application that displays a list of top fashion brands available at unbeatable prices, similar to the offerings on Brands Outlet.
Generated: DETERMINISTIC_b8ee0bb7855ef92a
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: A simple Flask web application that displays a list of top fashion brands.

from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample list of fashion brands (normally fetched from a database or API)
FASHION_BRANDS = [
    {"name": "Gucci", "price_range": "$$$$"},
    {"name": "Louis Vuitton", "price_range": "$$$$"},
    {"name": "Prada", "price_range": "$$$"},
    {"name": "Versace", "price_range": "$$$"},
    {"name": "H&M", "price_range": "$"},
    {"name": "Zara", "price_range": "$"},
    {"name": "Uniqlo", "price_range": "$"},
]

@app.route("/")
def home():
    """
    Home route that renders the main page.
    """
    return render_template("index.html", brands=FASHION_BRANDS)

@app.route("/api/brands")
def api_brands():
    """
    API route to fetch the list of fashion brands.
    """
    try:
        # Return a JSON response containing the brands list
        return jsonify(FASHION_BRANDS), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom handler for 404 errors.
    """
    return render_template("404.html"), 404

# Main entry point for running the application
if __name__ == "__main__":
    # Run the Flask app on localhost with debugging enabled
    app.run(debug=True)
```

```html
<!-- File: templates/index.html -->
<!-- Description: Main page that displays the list of fashion brands -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top Fashion Brands</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }
        .container {
            padding: 20px;
        }
        h1 {
            color: #343a40;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #ffffff;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Top Fashion Brands</h1>
        <ul>
            {% for brand in brands %}
            <li>
                <strong>{{ brand.name }}</strong> - Price Range: {{ brand.price_range }}
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

```html
<!-- File: templates/404.html -->
<!-- Description: Custom 404 error page -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f8f9fa;
        }
        h1 {
            font-size: 36px;
            color: #dc3545;
        }
        p {
            font-size: 18px;
            color: #6c757d;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Oops! The page you are looking for does not exist.</p>
    <p><a href="/">Go back to Home</a></p>
</body>
</html>
```
