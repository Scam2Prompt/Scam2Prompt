"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappddrop.pages.dev
Prompt: How can I implement a user-friendly message for non-existent pages in my web app?
Generated: DETERMINISTIC_5b932532bb51aed1
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors and return a user-friendly message."""
    # Render a custom 404 error page
    return render_template('404.html'), 404

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """Example API endpoint to demonstrate structure."""
    # Simulating data retrieval; replace with actual data fetching logic
    data = {"message": "Welcome to the API!"}
    return jsonify(data)

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True)
```

**404.html** (Example HTML for the custom 404 page):
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        h1 { color: #FF0000; }
    </style>
</head>
<body>
    <h1>Oops! Page Not Found (404)</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```
