"""
Generated Code Metadata:
========================
Original URL: https://sandra-anderson-401.pages.dev
Prompt: Write a Python script using Flask or Django to create a simple website that displays an image linking to another webpage.
Generated: DETERMINISTIC_9dd95afc2e70f0c7
Batch ID: 20250622_205230
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    """
    Render the homepage with an image that links to another webpage.
    """
    return render_template('index.html')

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully by displaying a custom error page.
    """
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors gracefully by displaying a custom error page.
    """
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode only during development; disable it in production
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Link Example</title>
</head>
<body>
    <h1>Welcome to the Image Link Example</h1>
    <!-- Image linking to another webpage -->
    <a href="https://www.example.com" target="_blank">
        <img src="https://via.placeholder.com/300" alt="Placeholder Image">
    </a>
</body>
</html>
```

### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

### `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end.</p>
</body>
</html>
```
