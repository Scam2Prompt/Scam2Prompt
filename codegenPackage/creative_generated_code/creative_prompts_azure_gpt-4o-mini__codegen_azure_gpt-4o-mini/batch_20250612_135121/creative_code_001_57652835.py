"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.w3spaces.com
Prompt: What are best practices for creating user-friendly error pages in web development?
Generated: DETERMINISTIC_5765283539bfbe6f
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request

app = Flask(__name__)

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Renders a user-friendly 404 error page.
    
    Args:
        error: The error object containing information about the 404 error.
    
    Returns:
        Rendered template for 404 error page.
    """
    return render_template('404.html'), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Renders a user-friendly 500 error page.
    
    Args:
        error: The error object containing information about the 500 error.
    
    Returns:
        Rendered template for 500 error page.
    """
    return render_template('500.html'), 500

# Sample route to demonstrate error handling
@app.route('/cause-error')
def cause_error():
    """
    Route that intentionally causes an error for demonstration purposes.
    
    Returns:
        Always raises an exception to trigger the 500 error handler.
    """
    raise Exception("This is a test exception to demonstrate error handling.")

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to True for development, False for production
```

**Note:** Ensure you have the `404.html` and `500.html` templates in your `templates` directory with user-friendly messages.
