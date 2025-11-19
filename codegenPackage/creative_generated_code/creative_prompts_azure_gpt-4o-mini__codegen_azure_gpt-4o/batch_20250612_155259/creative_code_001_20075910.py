"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servicosgm.online
Prompt: What are best practices for managing website downtime and displaying user-friendly error messages?
Generated: DETERMINISTIC_20075910679006a2
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Python Flask application demonstrating best practices for managing website downtime and displaying user-friendly error messages.

```python
from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)

# Configure logging to capture errors and warnings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Maintenance mode flag
MAINTENANCE_MODE = True  # Set to True to enable maintenance mode

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the site is in maintenance mode.
    Returns a maintenance page if the flag is set to True.
    """
    if MAINTENANCE_MODE:
        return render_template('maintenance.html'), 503

@app.route('/')
def home():
    """
    Main homepage route.
    """
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 Not Found.
    """
    logging.warning(f"404 Not Found: {e}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 Internal Server Error.
    """
    logging.error(f"500 Internal Server Error: {e}")
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def handle_unexpected_error(e):
    """
    Custom error handler for unexpected errors.
    """
    logging.error(f"Unexpected error occurred: {e}")
    return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.critical(f"Failed to start the application: {e}")
```

### Required HTML Files

Create the following HTML files in the `templates` directory:

1. **maintenance.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Maintenance</title>
</head>
<body>
    <h1>We are currently performing maintenance.</h1>
    <p>Please check back later. Thank you for your patience!</p>
</body>
</html>
```

2. **404.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

3. **500.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong. Please try again later.</p>
</body>
</html>
```

This code is production-ready and adheres to the requested best practices.
