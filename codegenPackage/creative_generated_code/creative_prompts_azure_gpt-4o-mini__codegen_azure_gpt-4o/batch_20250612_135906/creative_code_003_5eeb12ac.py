"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaimsklogi.imweb.me
Prompt: What libraries can I use to create a custom maintenance page for my web application?
Generated: DETERMINISTIC_5eeb12acb2b41268
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example code for creating a custom maintenance page for a web application using Python and Flask. Flask is a lightweight web framework that allows you to build web applications quickly.

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Flag to indicate whether the application is under maintenance
IS_UNDER_MAINTENANCE = True

# Error handler for maintenance mode
@app.errorhandler(503)
def maintenance_mode(error):
    """
    Handles maintenance mode and returns a custom maintenance page.
    """
    # Render a custom maintenance page
    return render_template('maintenance.html'), 503

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the application is under maintenance.
    If so, abort the request with a 503 error.
    """
    if IS_UNDER_MAINTENANCE:
        # Abort the request and trigger the maintenance handler
        from flask import abort
        abort(503)

@app.route('/')
def home():
    """
    Normal route that serves the homepage when not under maintenance.
    """
    return jsonify(message="Welcome to the Homepage!")

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Example HTML File (`templates/maintenance.html`)
Create the following file in a folder named `templates` in the same directory as the Python script:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance Mode</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>We'll Be Back Soon!</h1>
    <p>Our website is currently undergoing scheduled maintenance. We apologize for the inconvenience.</p>
    <p>Please check back later.</p>
</body>
</html>
```

### Notes:
1. The `IS_UNDER_MAINTENANCE` flag can be toggled to switch between maintenance and normal modes.
2. The `maintenance.html` template is served as the custom maintenance page.
3. Proper error handling is implemented using Flask's `errorhandler` decorator.
4. Best practices for organizing templates and modularizing logic are followed.
