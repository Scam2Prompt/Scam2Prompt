"""
Generated Code Metadata:
========================
Original URL: https://choruc.one
Prompt: How can I implement a custom 404 page not found error handler using a web framework, inspired by the example on choruc.one?
Generated: DETERMINISTIC_9f9ca4ca63e16437
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler."""
    # Get the requested path
    requested_path = request.path
    # Get all valid routes
    valid_routes = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and not rule.rule.startswith('/static'):
            valid_routes.append(rule.rule)
    
    # Suggest similar routes using Levenshtein distance
    from difflib import get_close_matches
    suggestions = get_close_matches(requested_path, valid_routes, n=3, cutoff=0.3)
    
    return render_template(
        '404.html',
        path=requested_path,
        suggestions=suggestions
    ), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            color: #343a40;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .container {
            max-width: 600px;
            padding: 2rem;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        .suggestions {
            margin-top: 2rem;
            text-align: left;
        }
        .suggestions h3 {
            margin-bottom: 0.5rem;
        }
        .suggestions ul {
            list-style-type: none;
            padding: 0;
        }
        .suggestions li {
            margin-bottom: 0.5rem;
        }
        .suggestions a {
            color: #007bff;
            text-decoration: none;
        }
        .suggestions a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>The page <code>{{ path }}</code> could not be found.</p>
        
        {% if suggestions %}
        <div class="suggestions">
            <h3>Were you looking for one of these?</h3>
            <ul>
                {% for suggestion in suggestions %}
                <li><a href="{{ suggestion }}">{{ suggestion }}</a></li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <p>Try visiting a non-existent page to see the custom 404 handler.</p>
</body>
</html>
```
