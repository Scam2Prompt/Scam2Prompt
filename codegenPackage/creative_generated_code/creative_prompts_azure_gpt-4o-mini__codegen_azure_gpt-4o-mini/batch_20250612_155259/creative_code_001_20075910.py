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

```python
from flask import Flask, render_template, jsonify
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom error handler for 500 errors (server errors)
@app.errorhandler(500)
def internal_server_error(e):
    # Log the error details
    logging.error(f"Server error: {e}")
    # Render a user-friendly error page
    return render_template('error.html', error_message="Sorry, something went wrong on our end."), 500

# Custom error handler for 404 errors (not found)
@app.errorhandler(404)
def page_not_found(e):
    # Log the not found error
    logging.warning(f"Page not found: {e}")
    # Render a user-friendly 404 error page
    return render_template('404.html', error_message="Sorry, the page you are looking for does not exist."), 404

# Route to simulate downtime
@app.route('/simulate_downtime')
def simulate_downtime():
    # Simulate an internal server error for testing
    raise Exception("Simulated server error!")

# Function to check service health
def check_service_health():
    # Here we could implement actual health checks (e.g., database, external APIs)
    return True  # Placeholder for health check

# Route to display the status of the website
@app.route('/status')
def status():
    if check_service_health():
        return jsonify(status="OK"), 200
    else:
        return jsonify(status="SERVICE UNAVAILABLE"), 503

if __name__ == '__main__':
    # Run the app, you can set host='0.0.0.0' for production
    app.run(host='127.0.0.1', port=os.getenv('PORT', 5000), debug=False)
```

### HTML Files (error.html and 404.html)
**error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>Oops!</h1>
    <p>{{ error_message }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Sorry!</h1>
    <p>{{ error_message }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
