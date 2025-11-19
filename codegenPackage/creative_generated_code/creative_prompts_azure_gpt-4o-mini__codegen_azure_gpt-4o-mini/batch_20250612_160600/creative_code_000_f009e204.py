"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://now-5000ether.paperplane.io
Prompt: What are the implications of a website being permanently moved, and how can I handle 301 redirects in my code?
Generated: DETERMINISTIC_f009e2048209ba68
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, redirect, url_for, request, abort

app = Flask(__name__)

# Dictionary to store permanent redirects
# Key: Old URL path, Value: New URL path
redirects = {
    '/old-url': '/new-url',
    '/another-old-url': '/another-new-url'
}

@app.route('/old-url')
def old_url_redirect():
    """Redirect /old-url to /new-url permanently (HTTP 301)"""
    return redirect(url_for('new_url'), code=301)

@app.route('/new-url')
def new_url():
    """New URL destination"""
    return "This is the new URL!"

@app.route('/another-old-url')
def another_old_url_redirect():
    """Redirect /another-old-url to /another-new-url permanently (HTTP 301)"""
    return redirect(url_for('another_new_url'), code=301)

@app.route('/another-new-url')
def another_new_url():
    """Another new URL destination"""
    return "This is another new URL!"

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return "Page not found! Please check the URL.", 404

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Log the exception and exit gracefully
        print(f"An error occurred: {e}")
```
