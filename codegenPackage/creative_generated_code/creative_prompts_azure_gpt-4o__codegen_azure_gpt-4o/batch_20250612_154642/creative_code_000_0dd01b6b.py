"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Write code to create a web-based application that showcases architectural projects, inspired by Études' approach to merging creativity and functionality.
Generated: DETERMINISTIC_0dd01b6b98617565
Batch ID: 20250612_154642
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/futuristic_office.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/minimalist_house.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/eco_villa.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Sample data to represent architectural projects
projects = [
    {
        "id": 1,
        "title": "Modern Minimalist House",
        "description": "A sleek and functional design with clean lines and open spaces.",
        "image_url": "https://example.com/images/minimalist_house.jpg"
    },
    {
        "id": 2,
        "title": "Eco-Friendly Urban Villa",
        "description": "A sustainable design merging green architecture with urban living.",
        "image_url": "https://example.com/images/eco_villa.jpg"
    },
    {
        "id": 3,
        "title": "Futuristic Office Space",
        "description": "An innovative workspace featuring cutting-edge design and technology.",
        "image_url": "https://example.com/images/futuristic_office.jpg"
    }
]

@app.route("/")
def home():
    """
    Home route to render the main page showcasing architectural projects.
    """
    return render_template("index.html", projects=projects)

@app.route("/api/projects", methods=["GET"])
def get_projects():
    """
    API endpoint to fetch the list of architectural projects.
    Returns a JSON response containing all projects.
    """
    return jsonify(projects)

# Error handling for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors and returns a custom error page.
    """
    return render_template("404.html"), 404

# Error handling for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles 500 errors and provides a user-friendly message.
    """
    return render_template("500.html"), 500

# Run the application only if the script is executed directly
if __name__ == "__main__":
    # Use debug mode only in development
    app.run(debug=True)

```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Projects</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
        .project {
            border: 1px solid #ddd;
            margin: 20px 0;
            padding: 20px;
            display: flex;
            align-items: center;
        }
        .project img {
            max-width: 150px;
            margin-right: 20px;
        }
        .project-details {
            flex-grow: 1;
        }
        .project-title {
            font-size: 1.5em;
            margin: 0;
        }
        .project-description {
            margin: 10px 0 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Architectural Projects</h1>
        {% for project in projects %}
        <div class="project">
            <img src="{{ project.image_url }}" alt="{{ project.title }}">
            <div class="project-details">
                <h2 class="project-title">{{ project.title }}</h2>
                <p class="project-description">{{ project.description }}</p>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Error 404</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/500.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
</head>
<body>
    <h1>Error 500</h1>
    <p>An unexpected error occurred. Please try again later.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### Directory Structure:

```
project/
├── app.py
├── templates/
│   ├── index.html
│   ├── 404.html
│   ├── 500.html
```
