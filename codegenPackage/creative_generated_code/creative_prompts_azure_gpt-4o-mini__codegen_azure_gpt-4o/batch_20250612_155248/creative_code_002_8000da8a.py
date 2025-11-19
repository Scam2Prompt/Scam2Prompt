"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choruc.one
Prompt: Write a Python function that logs 404 errors and redirects users to a custom error page.
Generated: DETERMINISTIC_8000da8ab2032352
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, render_template, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(
    filename='error.log',  # Log file to store errors
    level=logging.ERROR,   # Log level set to capture errors
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

@app.errorhandler(404)
def handle_404_error(error):
    """
    Flask error handler for 404 errors.
    Logs the error and redirects the user to a custom error page.

    Args:
        error: The error object containing details of the 404 error.

    Returns:
        A rendered template for the custom error page.
    """
    # Log the error details
    logging.error(f"404 Error: {error}")
    
    # Redirect user to a custom error page
    return render_template('404.html'), 404

# A sample route to test the application
@app.route('/')
def home():
    """
    Sample route for the home page.
    
    Returns:
        A simple welcome message as the home page content.
    """
    return "Welcome to the homepage!"

# Run the application
if __name__ == '__main__':
    # Start the Flask server in debug mode
    app.run(debug=True)
```
