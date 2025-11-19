"""
Generated Code Metadata:
========================
Original URL: https://choruc.one
Prompt: Write a Python script to handle 404 page not found errors similar to the one on choruc.one.
Generated: DETERMINISTIC_b029ce5992cdecb9
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

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 Page Not Found errors.
    
    Args:
        e: The error object containing information about the error.
    
    Returns:
        A rendered HTML template for the 404 error page.
    """
    # Log the error for debugging purposes
    app.logger.error(f"404 Error: {request.path} not found.")
    
    # Render the custom 404 error page
    return render_template('404.html'), 404

@app.route('/')
def home():
    """
    Home route that serves the main page of the application.
    
    Returns:
        A simple welcome message.
    """
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**404.html** (Create this file in a `templates` directory):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 50px;
        }
        h2 {
            font-size: 30px;
        }
        p {
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>404</h1>
    <h2>Page Not Found</h2>
    <p>Sorry, the page you are looking for does not exist.</p>
    <p><a href="/">Return to Home</a></p>
</body>
</html>
```

**Note**: Ensure you have Flask installed in your environment. You can install it using:
```bash
pip install Flask
```
