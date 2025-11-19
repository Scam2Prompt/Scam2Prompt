"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totalwineusinc.com
Prompt: What are the best practices for handling website downtime and displaying maintenance messages in a user-friendly way?
Generated: DETERMINISTIC_5c3da67ad82b2102
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Flag to simulate maintenance mode (could be controlled by environment variable or config file)
MAINTENANCE_MODE = bool(os.getenv('MAINTENANCE_MODE', False))


@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the application is in maintenance mode.
    If true, serve a maintenance page for all requests.
    """
    if MAINTENANCE_MODE:
        return render_template('maintenance.html'), 503


@app.route('/')
def home():
    """
    Home page route.
    """
    return render_template('index.html')


@app.route('/api/data')
def api_data():
    """
    Example API route.
    """
    example_data = {"message": "This is a sample API response."}
    return jsonify(example_data)


@app.errorhandler(503)
def maintenance_mode_error(error):
    """
    Custom error handler for HTTP 503 (Service Unavailable).
    """
    return render_template('maintenance.html'), 503


# Run the application
if __name__ == '__main__':
    # Ensure debug mode is off for production
    app.run(host='0.0.0.0', port=5000, debug=False)

```

### Template: `maintenance.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #dd4b39;
        }
    </style>
</head>
<body>
    <h1>Site Under Maintenance</h1>
    <p>We're currently performing some scheduled maintenance.</p>
    <p>Please check back later. Thank you for your patience.</p>
</body>
</html>
```
