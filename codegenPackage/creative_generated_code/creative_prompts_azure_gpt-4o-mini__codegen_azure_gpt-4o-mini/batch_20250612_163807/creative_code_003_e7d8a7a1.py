"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantaxbonk.network
Prompt: Can you provide code snippets for handling website downtime gracefully in a web application?
Generated: DETERMINISTIC_e7d8a7a1e1afff01
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import logging
import time
import random

app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(filename='app.log', level=logging.ERROR)

@app.route('/')
def home():
    try:
        # Simulate a potential downtime scenario
        if random.choice([True, False]):
            raise Exception("Simulated downtime error.")
        
        return render_template('index.html')
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return handle_downtime()

def handle_downtime():
    """Render a downtime page with user-friendly message."""
    return render_template('downtime.html'), 503

@app.errorhandler(503)
def service_unavailable(error):
    """Custom error handler for 503 Service Unavailable."""
    return render_template('downtime.html'), 503

if __name__ == '__main__':
    try:
        # Run the application on the specified host and port
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Failed to start the server: {e}")
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Our Website!</h1>
</body>
</html>
```

```html
<!-- downtime.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Unavailable</title>
</head>
<body>
    <h1>Oops! We're experiencing technical difficulties.</h1>
    <p>Please try again later.</p>
</body>
</html>
```
