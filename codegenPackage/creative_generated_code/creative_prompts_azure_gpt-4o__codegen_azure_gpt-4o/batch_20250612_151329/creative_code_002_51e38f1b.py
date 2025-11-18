"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdddd.pages.dev
Prompt: Generate code to detect whether a user is accessing a website from a desktop or mobile device and display an optimized message, similar to the desktop usage optimization mentioned on the chimpers-dojo website.
Generated: DETERMINISTIC_51e38f1b01895b6f
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template

app = Flask(__name__)

# A dictionary to store device-specific messages
DEVICE_MESSAGES = {
    "mobile": "Welcome! You're using a mobile device. This website is optimized for smaller screens.",
    "desktop": "Welcome! You're using a desktop device. Enjoy our optimized layout for larger screens."
}

def detect_device(user_agent):
    """
    Detects the device type based on the User-Agent string.

    Args:
        user_agent (str): The User-Agent string from the HTTP request headers.

    Returns:
        str: 'mobile' if the user is accessing from a mobile device, otherwise 'desktop'.
    """
    mobile_keywords = [
        'Android', 'iPhone', 'iPad', 'iPod', 'BlackBerry', 'Windows Phone', 'webOS'
    ]
    
    for keyword in mobile_keywords:
        if keyword in user_agent:
            return 'mobile'
    return 'desktop'

@app.route('/')
def home():
    """
    Route for the home page. Detects the user's device and displays an optimized message.

    Returns:
        str: Rendered HTML template with the device-specific message.
    """
    try:
        user_agent = request.headers.get('User-Agent', '')
        device_type = detect_device(user_agent)
        message = DEVICE_MESSAGES.get(device_type, "Welcome to our website!")
        return render_template('index.html', message=message)
    except Exception as e:
        # Log error and return a fallback message
        app.logger.error(f"Error detecting device: {e}")
        return render_template('error.html', message="An error occurred while detecting your device type.")

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Create `templates/index.html` and `templates/error.html` as part of your Flask project to render messages.
- The `index.html` template can contain code like:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>Device Detection</title>
  </head>
  <body>
      <h1>{{ message }}</h1>
  </body>
  </html>
  ```
- The `error.html` template can contain code like:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>Error</title>
  </head>
  <body>
      <h1>{{ message }}</h1>
  </body>
  </html>
  ```
