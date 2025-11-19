"""
Generated Code Metadata:
========================
Original URL: https://dappdroppage.pages.dev
Prompt: Recommend an API or library that can be used to create a simple webpage that displays a "page not found" or "organization no longer exists" message, similar to the content on the provided URL.
Generated: DETERMINISTIC_2348bd38e4f28ec1
Batch ID: 20250622_204851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation using Python's Flask framework to create a simple webpage that displays a "Page Not Found" or "Organization No Longer Exists" message.

```python
from flask import Flask, render_template, abort

app = Flask(__name__)

# Custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    """
    Handles 404 errors and displays a custom 'Page Not Found' message.
    """
    return render_template('404.html'), 404

@app.route('/organization/<org_id>')
def organization_page(org_id):
    """
    Simulates an organization lookup. If the organization does not exist,
    it returns a 404 error.
    """
    # Simulated organization database (replace with actual database lookup)
    organizations = {
        "123": "Organization A",
        "456": "Organization B"
    }

    # Check if the organization exists
    if org_id not in organizations:
        abort(404)  # Trigger the custom 404 error handler

    # Render a page for the organization (if it exists)
    return f"<h1>Welcome to {organizations[org_id]}</h1>"

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
```

### HTML Template (`templates/404.html`)
Create a folder named `templates` in the same directory as the Python script, and add the following `404.html` file:

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
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 10%;
        }
        h1 {
            color: #dc3545;
        }
        p {
            color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404 - Page Not Found</h1>
        <p>The page or organization you are looking for no longer exists.</p>
        <p><a href="/">Return to Home</a></p>
    </div>
</body>
</html>
```

### Notes:
- Install Flask using `pip install flask` if not already installed.
- The `debug=True` flag in `app.run()` is for development purposes. Remove it in production.
- Replace the simulated `organizations` dictionary with a real database or API integration for actual use cases.
