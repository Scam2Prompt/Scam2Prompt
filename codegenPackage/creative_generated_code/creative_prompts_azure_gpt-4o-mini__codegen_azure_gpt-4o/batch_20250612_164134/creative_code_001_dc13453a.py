"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: How can I configure a web server to show a specific HTML page when no content is available at the given URL?
Generated: DETERMINISTIC_dc13453ae681102a
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready code using Python and Flask to configure a web server to show a custom HTML page when no content is available at the given URL:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define the route for the homepage (optional)
@app.route('/')
def home():
    return "Welcome to the homepage!"

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    # Render a custom HTML page when a 404 error occurs
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the Flask development server
    # Production deployments should use a WSGI server (e.g., gunicorn)
    app.run(debug=True)
```

### Directory Structure:
Ensure you have the following structure in your project:
```
/project-directory
    /templates
        404.html
    app.py
```

### Example `404.html` file:
Place this file in the `templates` directory.

```html
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
            margin-top: 50px;
        }
        h1 {
            color: red;
        }
        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go back to the homepage</a>
</body>
</html>
```
