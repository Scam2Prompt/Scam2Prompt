"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.magpiexyz.click
Prompt: How do I troubleshoot a web server that shows a default page instead of my intended content?
Generated: DETERMINISTIC_03ab898f60c69f8a
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, send_from_directory, abort

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    """
    Serve the main page of the web application.
    If the intended content (index.html) is not found, a default page is displayed.
    """
    try:
        # Attempt to serve the intended content
        return send_from_directory('static', 'index.html')
    except FileNotFoundError:
        # Log an error and serve the default page if the intended content is missing
        logging.error("index.html not found, serving default page.")
        return send_from_directory('static', 'default.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    Returns a custom 404 page.
    """
    logging.warning("404 error: Page not found")
    return send_from_directory('static', '404.html'), 404

def check_server_setup():
    """
    Check if the expected files are present in the static directory.
    This is a preliminary check to assist with troubleshooting.
    """
    expected_files = ['index.html', 'default.html', '404.html']
    missing_files = [file for file in expected_files if not os.path.isfile(os.path.join('static', file))]

    if missing_files:
        logging.error(f"Missing files: {', '.join(missing_files)}. Please ensure all required files are in the static directory.")
        return False
    logging.info("All required files are present.")
    return True

if __name__ == '__main__':
    # Ensure server setup is valid before starting the application
    if check_server_setup():
        app.run(host='0.0.0.0', port=5000)
    else:
        logging.critical("Server setup is invalid. Exiting...")
```

Make sure to have a folder named `static` in the same directory as this script, containing `index.html`, `default.html`, and `404.html` files for the web server to function correctly.
