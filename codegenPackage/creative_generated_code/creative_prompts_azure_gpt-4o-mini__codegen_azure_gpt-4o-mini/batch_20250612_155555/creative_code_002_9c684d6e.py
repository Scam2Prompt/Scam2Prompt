"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrolly-claim.xyz
Prompt: Can you provide code examples for handling website downtime gracefully in a web application?
Generated: DETERMINISTIC_9c684d6eb4ed2b05
Batch ID: 20250612_155555
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom error handling for downtime
@app.errorhandler(503)
def service_unavailable(e):
    """Handle service unavailable errors gracefully."""
    return render_template('503.html'), 503

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

def check_service_status():
    """Simulate checking an external service status."""
    # In a real application, replace this with actual health check logic
    # For demonstration, we'll assume the service is down 20% of the time.
    import random
    return random.choice([True, True, True, True, False])  # 80% chance of being up

@app.route('/external-service')
def external_service():
    """Handle requests to an external service."""
    if not check_service_status():
        # Log the error
        logging.error('External service is down.')
        # Raise a 503 Service Unavailable error
        return service_unavailable(503)
    
    # If the service is available, proceed with the logic
    return render_template('external_service.html')

if __name__ == '__main__':
    # Run the application
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error(f"Failed to start the application: {e}")
```

```html
<!-- templates/503.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Unavailable</title>
</head>
<body>
    <h1>503 Service Unavailable</h1>
    <p>Sorry, the service is currently unavailable. Please try again later.</p>
</body>
</html>
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <p><a href="/external-service">Check External Service</a></p>
</body>
</html>
```

```html
<!-- templates/external_service.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>External Service</title>
</head>
<body>
    <h1>External Service is Available</h1>
    <p>You have accessed the external service successfully.</p>
</body>
</html>
```
