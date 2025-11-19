"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://valentina-rossi.com
Prompt: Can you provide code examples for creating a maintenance mode feature in a web application?
Generated: DETERMINISTIC_a080f730c0aab0a1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from functools import wraps

app = Flask(__name__)

# Flag to indicate whether the application is in maintenance mode
MAINTENANCE_MODE = True

def maintenance_required(f):
    """Decorator to enforce maintenance mode."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if MAINTENANCE_MODE:
            return render_template('maintenance.html'), 503  # Service Unavailable
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@maintenance_required
def home():
    """Home page route."""
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
@maintenance_required
def get_data():
    """API endpoint to get data."""
    data = {"message": "This is your data."}
    return jsonify(data)

@app.route('/admin/maintenance', methods=['POST'])
def set_maintenance_mode():
    """Admin endpoint to toggle maintenance mode."""
    global MAINTENANCE_MODE
    mode = request.json.get('mode')
    if mode is None:
        return jsonify({"error": "Mode is required"}), 400
    if mode not in [True, False]:
        return jsonify({"error": "Invalid mode value"}), 400

    MAINTENANCE_MODE = mode
    return jsonify({"maintenance_mode": MAINTENANCE_MODE}), 200

if __name__ == '__main__':
    # Run the application
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        # Log any error that occurs when starting the application
        print(f"Error starting the application: {e}")
```

**Templates:**

*maintenance.html:*
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maintenance Mode</title>
</head>
<body>
    <h1>We'll be back soon!</h1>
    <p>Our website is currently undergoing maintenance. Please check back later.</p>
</body>
</html>
```

*index.html:*
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Home Page!</h1>
    <p>This is the main content of the application.</p>
</body>
</html>
```
