"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totalwineusinc.com
Prompt: How can I implement a custom error page for a website that is currently unavailable, similar to the message shown on totalwineusinc.com?
Generated: DETERMINISTIC_4f799ac4cc765d11
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a production-ready implementation in Python using Flask for a custom error page:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define a custom error page route for 503 Service Unavailable
@app.errorhandler(503)
def service_unavailable(error):
    """
    Custom error handler for 503 Service Unavailable.
    Renders a user-friendly HTML page when the service is temporarily unavailable.
    """
    return render_template('503.html'), 503

# Route for demonstration purposes
@app.route('/')
def home():
    """
    Main route for the website.
    Raise a Service Unavailable error to demonstrate the custom error page.
    """
    # Simulate service unavailability for demonstration purposes
    abort(503)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Create a `templates/503.html` file for the custom error page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Temporarily Unavailable</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 2em;
            color: #333;
        }
        p {
            font-size: 1.2em;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Service Temporarily Unavailable</h1>
    <p>We're sorry, but the website is currently unavailable. Please try again later.</p>
</body>
</html>
```

This code properly handles 503 errors, displays a custom HTML page, and follows web application best practices.
