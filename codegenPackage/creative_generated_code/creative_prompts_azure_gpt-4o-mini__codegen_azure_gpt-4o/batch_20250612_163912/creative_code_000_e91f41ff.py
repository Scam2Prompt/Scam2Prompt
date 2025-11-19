"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop-playboicarti.com
Prompt: What code can I use to create a maintenance mode feature for an e-commerce website similar to Playboi Carti's shop?
Generated: DETERMINISTIC_e91f41ff3525a874
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# maintenance_mode.py

from flask import Flask, request, jsonify, redirect, url_for
import os

app = Flask(__name__)

# Global variable to enable/disable maintenance mode
MAINTENANCE_MODE = os.getenv('MAINTENANCE_MODE', 'off').lower() == 'on'

def maintenance_mode_middleware(func):
    """
    Middleware to check if the site is in maintenance mode.
    If maintenance mode is active, redirect all requests to a maintenance page.
    """
    def wrapper(*args, **kwargs):
        if MAINTENANCE_MODE:
            return redirect(url_for('maintenance_page'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/')
@maintenance_mode_middleware
def home():
    """Main homepage route."""
    return jsonify({"message": "Welcome to the e-commerce site!"})

@app.route('/product/<product_id>')
@maintenance_mode_middleware
def product(product_id):
    """Product page route."""
    return jsonify({"product_id": product_id, "message": "Product details page!"})

@app.route('/maintenance')
def maintenance_page():
    """
    Route for the maintenance page.
    This is displayed when the e-commerce site is in maintenance mode.
    """
    return jsonify({"message": "The site is currently under maintenance. Please check back later."}), 503

@app.errorhandler(404)
def not_found(error):
    """Custom handler for 404 errors."""
    return jsonify({"error": "Page not found."}), 404

@app.errorhandler(500)
def server_error(error):
    """Custom handler for server errors."""
    return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Usage:
- Set the `MAINTENANCE_MODE` environment variable to `on` or `off` to toggle the mode.
- Example:
  ```bash
  export MAINTENANCE_MODE=on
  python maintenance_mode.py
  ```
