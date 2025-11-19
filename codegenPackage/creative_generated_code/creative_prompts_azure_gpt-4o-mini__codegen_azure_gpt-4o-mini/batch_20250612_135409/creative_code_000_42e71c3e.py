"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extenso-mayotte.fr
Prompt: What are the best practices for handling website maintenance notifications in a user-friendly manner?
Generated: DETERMINISTIC_42e71c3e4530fafd
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, abort
import logging
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Maintenance mode flag
MAINTENANCE_MODE = True

# Maintenance message
MAINTENANCE_MESSAGE = "We're currently performing scheduled maintenance. Please check back later."

def is_maintenance_mode():
    """Check if the site is in maintenance mode."""
    return MAINTENANCE_MODE

@app.errorhandler(503)
def service_unavailable(e):
    """Handle service unavailable errors."""
    return render_template('maintenance.html', message=MAINTENANCE_MESSAGE), 503

@app.before_request
def check_maintenance_mode():
    """Check if the application is in maintenance mode before processing requests."""
    if is_maintenance_mode():
        logging.info("Maintenance mode is active. Redirecting to maintenance page.")
        abort(503)  # Trigger a 503 Service Unavailable error

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

if __name__ == '__main__':
    try:
        # Run the application
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error("An error occurred while starting the application: %s", e)
```

**maintenance.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance</title>
</head>
<body>
    <h1>We'll be back soon!</h1>
    <p>{{ message }}</p>
</body>
</html>
```

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <p>This is the home page content.</p>
</body>
</html>
```
