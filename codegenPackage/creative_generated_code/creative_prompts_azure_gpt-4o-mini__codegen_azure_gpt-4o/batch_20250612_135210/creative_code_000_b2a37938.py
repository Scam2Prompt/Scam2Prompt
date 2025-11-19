"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.cityp.net
Prompt: What are the common reasons for encountering a 404 error on a website, and how can I handle this in my web application?
Generated: DETERMINISTIC_b2a37938c3f167d1
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example using Flask to handle 404 errors gracefully in a web application:

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route definitions
@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "This is the About Page."

# Error handler for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors gracefully by returning a custom error message or page.
    """
    # Log the error (in a real application, use a structured logging mechanism)
    app.logger.error(f"404 Error: Requested URL not found - {error}")

    # Option 1: Return a custom HTML page
    return render_template('404.html'), 404

    # Option 2: Return a JSON response (uncomment below to use)
    # return jsonify({"error": "Page not found", "status_code": 404}), 404

# Run the application
if __name__ == '__main__':
    # Ensure debug mode is off for production usage
    app.run(debug=False)
```

### Example `404.html` File (Optional)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>Oops! Page Not Found</h1>
    <p>The page you're looking for doesn't exist. Please check the URL or return to the <a href="/">home page</a>.</p>
</body>
</html>
```

### Key Notes:
1. Ensure the `404.html` file is placed in the `templates` directory (required for Flask to locate it).
2. This code includes logging for production monitoring and error analysis.
3. The `app.errorhandler` decorator ensures that custom behavior is applied for 404 errors.
