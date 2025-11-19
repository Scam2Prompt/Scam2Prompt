"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-metamesklogin.uteach.io
Prompt: Generate a code snippet that handles 404 errors in a web application, similar to the message displayed on the Uteach login page.
Generated: DETERMINISTIC_94cc5138ac346829
Batch ID: 20250612_155351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    """
    Handles 404 errors and returns a custom error page.
    :param error: The 404 error object
    :return: Rendered HTML template for the 404 error page
    """
    # Log the error (optional, for debugging purposes)
    app.logger.error(f"404 Error: {error}")

    # Render a custom 404 error page
    return render_template('404.html'), 404

# Define a sample route for demonstration
@app.route('/')
def home():
    """
    Returns the homepage.
    :return: HTML content for the homepage
    """
    return "Welcome to the homepage!"

# Run the application
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```

### Additional Notes:
1. Ensure you have a `404.html` file in your `templates` directory with the desired design and message for the 404 error page.
2. Use `debug=False` in production to prevent exposing sensitive information.
