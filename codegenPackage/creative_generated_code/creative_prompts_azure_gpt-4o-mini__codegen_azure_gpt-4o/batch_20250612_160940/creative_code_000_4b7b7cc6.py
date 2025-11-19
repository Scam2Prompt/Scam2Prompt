"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smardex.live
Prompt: What code can I use to set up a web server that displays a custom default page instead of a generic message?
Generated: DETERMINISTIC_4b7b7cc6c4398ad4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s production-ready code for setting up a web server in Python using Flask, which displays a custom default page:

```python
from flask import Flask, render_template, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Route for the custom default page
@app.route('/')
def home():
    """
    Custom default page route.
    Returns a simple HTML page with a custom message.
    """
    return render_template('index.html')  # Render the custom HTML page

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 error.
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Page not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 error.
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Internal server error"}), 500

# Entry point for running the server
if __name__ == '__main__':
    # Start the Flask app on localhost and port 5000
    # Debug mode should be disabled in production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**HTML File (`templates/index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Default Page</title>
</head>
<body>
    <h1>Welcome to the Custom Web Server!</h1>
    <p>This is your custom default page.</p>
</body>
</html>
```

**Requirements:** Ensure Flask is installed in your Python environment (`pip install flask`). Place the `index.html` file inside a `templates/` directory relative to your Python script.
