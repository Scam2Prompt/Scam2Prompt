"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-olympia.xyz
Prompt: How can I create a custom error page for my web application to inform users about service disruptions?
Generated: DETERMINISTIC_65fa1e202fb212cf
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of creating a custom error page for a web application in Python using the Flask framework:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Custom error handler for 404 errors (Page Not Found)
@app.errorhandler(404)
def not_found_error(error):
    # Render a custom 404 error page
    return render_template('404.html'), 404

# Custom error handler for 500 errors (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(error):
    # Render a custom 500 error page
    return render_template('500.html'), 500

# Route for testing (optional, for development purposes)
@app.route('/')
def home():
    return "Welcome to the web application."

# Simulate a 500 error for testing purposes
@app.route('/cause-error')
def cause_error():
    raise Exception("This is a test error to trigger a 500 error page.")

# Ensure the application runs properly
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```

**404.html** (HTML for custom 404 error page):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go to Homepage</a>
</body>
</html>
```

**500.html** (HTML for custom 500 error page):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end. Please try again later.</p>
    <a href="/">Go to Homepage</a>
</body>
</html>
```
