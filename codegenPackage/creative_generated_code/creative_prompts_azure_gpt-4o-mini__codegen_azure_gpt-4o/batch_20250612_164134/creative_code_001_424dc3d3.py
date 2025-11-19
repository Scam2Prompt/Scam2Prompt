"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappddrop.pages.dev
Prompt: What are best practices for creating a custom error page in a web framework?
Generated: DETERMINISTIC_424dc3d352aa7bab
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example implementation in Python using the Flask framework:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Custom error handler for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors by returning a custom HTML page.
    
    Args:
        e: Exception object associated with the 404 error.
    
    Returns:
        Tuple: A rendered HTML template and HTTP status code (404).
    """
    return render_template("404.html"), 404

# Custom error handler for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(e):
    """
    Handle 500 errors by returning a custom HTML page.
    
    Args:
        e: Exception object associated with the 500 error.
    
    Returns:
        Tuple: A rendered HTML template and HTTP status code (500).
    """
    return render_template("500.html"), 500

# Sample route to demonstrate the app running normally
@app.route("/")
def home():
    """
    Render the homepage.
    
    Returns:
        String: A simple welcome message.
    """
    return "Welcome to the homepage!"

# Run the application
if __name__ == "__main__":
    # Ensure debug mode is disabled for production
    app.run(debug=False)
```

Note: Be sure to create `404.html` and `500.html` templates inside your `templates` folder with appropriate custom error messages for those pages.
