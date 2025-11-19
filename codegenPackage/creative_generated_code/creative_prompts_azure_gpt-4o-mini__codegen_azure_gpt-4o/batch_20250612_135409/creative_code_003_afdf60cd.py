"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extenso-mayotte.fr
Prompt: Write a code snippet to redirect users to a maintenance page during downtime.
Generated: DETERMINISTIC_afdf60cdc14dfc77
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

# Flag to indicate whether the website is under maintenance
UNDER_MAINTENANCE = True

@app.before_request
def check_maintenance_mode():
    """
    Middleware function to check if the site is under maintenance.
    Redirects all users to a maintenance page if the flag is set to True.
    """
    if UNDER_MAINTENANCE and not is_maintenance_page_request():
        return redirect(url_for('maintenance'))

@app.route('/maintenance')
def maintenance():
    """
    Route for the maintenance page.
    Displays a simple maintenance message to the users.
    """
    return '<h1>Site Under Maintenance</h1><p>We are currently performing scheduled updates. Please check back soon.</p>', 503

def is_maintenance_page_request():
    """
    Helper function to check if the current request is for the maintenance page.
    Ensures users are not redirected in a loop when visiting the maintenance page directly.
    """
    return '/maintenance' in str(url_for('maintenance'))

@app.route('/')
def home():
    """
    Regular route for the home page.
    This will be inaccessible during maintenance.
    """
    return '<h1>Welcome to the Home Page!</h1>'

@app.route('/about')
def about():
    """
    Regular route for the About page.
    This will also be inaccessible during maintenance.
    """
    return '<h1>About Us</h1>'

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
