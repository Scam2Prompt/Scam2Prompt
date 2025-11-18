"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-game7.xyz
Prompt: Write a Python script using Flask to create a web server that shows the text "Success! Your new web server is ready to use" on the homepage.
Generated: DETERMINISTIC_d72f2e606beb6313
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def homepage():
    """
    Handle requests to the homepage URL ('/').

    Returns:
        str: A success message indicating the web server is ready.
    """
    return "Success! Your new web server is ready to use"

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors (Page Not Found).

    Args:
        e: Exception object for the error.

    Returns:
        str: Custom message for the 404 error.
    """
    return "Error 404: Page not found.", 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors (Internal Server Error).

    Args:
        e: Exception object for the error.

    Returns:
        str: Custom message for the 500 error.
    """
    return "Error 500: Internal server error.", 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask development server
    # Note: In production, use a WSGI server like Gunicorn or uWSGI
    app.run(host='0.0.0.0', port=5000, debug=True)
```
