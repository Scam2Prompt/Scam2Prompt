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

# Maintenance mode flag
MAINTENANCE_MODE = True

@app.route('/')
def home():
    """Render the home page or redirect to maintenance page."""
    if MAINTENANCE_MODE:
        return redirect(url_for('maintenance'))
    return "Welcome to the main page!"

@app.route('/maintenance')
def maintenance():
    """Render the maintenance page."""
    return "We're currently undergoing maintenance. Please check back later."

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)  # Run the app on the specified host and port
    except Exception as e:
        # Proper error handling for the server run
        print(f"An error occurred: {e}")
```
