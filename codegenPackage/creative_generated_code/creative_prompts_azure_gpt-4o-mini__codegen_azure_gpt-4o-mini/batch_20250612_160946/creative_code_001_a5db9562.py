"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: How can I configure a web server to show a specific message when the site is not available, similar to "You see this page because there is no Web site at this address"?
Generated: DETERMINISTIC_a5db9562d3c76715
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the web server!"

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    Returns a specific message when the site is not available.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    try:
        # Run the web server on port 5000
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        # Handle any exception that occurs while starting the server
        print(f"Failed to start the web server: {e}")
```

Create a `404.html` file in a `templates` folder with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>Not Found</h1>
    <p>You see this page because there is no Web site at this address.</p>
</body>
</html>
```

Make sure you have Flask installed. You can install it using pip if you haven't already:

```bash
pip install Flask
```
