"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga2fight.com
Prompt: Write a script that automatically redirects users to a maintenance page during scheduled downtime.
Generated: DETERMINISTIC_15f2b5250a7db253
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, redirect, url_for

app = Flask(__name__)

# Define the scheduled maintenance time (24-hour format)
MAINTENANCE_START = datetime.time(2, 0)  # 2:00 AM
MAINTENANCE_END = datetime.time(4, 0)    # 4:00 AM

@app.before_request
def check_maintenance_window():
    """
    Middleware to check if the current time falls within the scheduled maintenance window.
    If yes, redirect to the maintenance page.
    """
    current_time = datetime.datetime.now().time()
    
    # Check if current time is within the maintenance window
    if MAINTENANCE_START <= current_time <= MAINTENANCE_END:
        return redirect(url_for('maintenance'))

@app.route('/')
def home():
    """
    Main homepage of the application.
    """
    return "Welcome to the main application!"

@app.route('/maintenance')
def maintenance():
    """
    Maintenance page displayed during scheduled downtime.
    """
    return "The site is currently undergoing maintenance. Please check back later.", 503

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return "Page not found. Please check the URL.", 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error handler.
    """
    return "An internal server error occurred. Please try again later.", 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
