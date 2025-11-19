"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extenso-mayotte.fr
Prompt: What are the best practices for handling website maintenance notifications in a user-friendly manner?
Generated: DETERMINISTIC_42e71c3e4530fafd
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready example in Python using Flask (a web framework) to implement website maintenance notifications in a user-friendly manner.

```python
from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

# Define maintenance schedule
MAINTENANCE_START = datetime.datetime(2023, 10, 15, 2, 0, 0)  # Example start time
MAINTENANCE_END = datetime.datetime(2023, 10, 15, 4, 0, 0)   # Example end time

def is_under_maintenance():
    """
    Check if the current time falls within the maintenance window.
    Returns True if under maintenance, otherwise False.
    """
    current_time = datetime.datetime.now()
    return MAINTENANCE_START <= current_time <= MAINTENANCE_END

@app.before_request
def check_maintenance():
    """
    Middleware to check if the website is under maintenance.
    If yes, serve a maintenance notification page.
    """
    if is_under_maintenance():
        maintenance_message = {
            "status": "Maintenance Mode",
            "message": "Our website is currently undergoing maintenance. Please check back later.",
            "maintenance_start": MAINTENANCE_START.strftime("%Y-%m-%d %H:%M:%S"),
            "maintenance_end": MAINTENANCE_END.strftime("%Y-%m-%d %H:%M:%S")
        }
        return render_template("maintenance.html", maintenance_info=maintenance_message), 503

@app.route('/')
def home():
    """
    Homepage route.
    """
    return "Welcome to the website! Everything is running smoothly."

@app.route('/api/data')
def api_data():
    """
    Example API endpoint.
    """
    return jsonify({"data": "Here is some data from the API."})

# Ensure custom 503 error handler for production readiness
@app.errorhandler(503)
def handle_maintenance_error(error):
    """
    Custom error handler for HTTP 503 Service Unavailable.
    """
    return render_template("maintenance.html", maintenance_info=error.description), 503

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True)
```

### Example `maintenance.html` Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance Notice</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
        }
        h1 {
            color: #d9534f;
        }
        p {
            color: #5a5a5a;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ maintenance_info['status'] }}</h1>
        <p>{{ maintenance_info['message'] }}</p>
        <p><strong>Start Time:</strong> {{ maintenance_info['maintenance_start'] }}</p>
        <p><strong>End Time:</strong> {{ maintenance_info['maintenance_end'] }}</p>
    </div>
</body>
</html>
```
