"""
Generated Code Metadata:
========================
Original URL: https://choruc.one
Prompt: Write a Python function that logs 404 errors and redirects users to a custom error page.
Generated: DETERMINISTIC_8000da8ab2032352
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from flask import Flask, redirect, url_for, render_template

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='error.log')

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors by logging the error and redirecting to a custom error page.

    Args:
        e: The error object containing information about the 404 error.

    Returns:
        A redirect to the custom error page.
    """
    # Log the 404 error
    logging.error(f'404 Error: {e}, Path: {e.path}')
    
    # Redirect to the custom error page
    return redirect(url_for('custom_404'))

@app.route('/custom_404')
def custom_404():
    """
    Render the custom 404 error page.

    Returns:
        Rendered HTML for the custom 404 error page.
    """
    return render_template('404.html'), 404

# Example route for demonstration
@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        Rendered HTML for the home page.
    """
    return '<h1>Welcome to the Home Page!</h1>'

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to create a `404.html` file in the templates directory for the custom error page.
