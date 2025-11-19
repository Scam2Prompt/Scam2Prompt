"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: How can I configure a web server to show a specific message when the site is not available, similar to "You see this page because there is no Web site at this address"?
Generated: DETERMINISTIC_a5db9562d3c76715
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of configuring a web server using Python's Flask framework to display a custom message when a 404 (Not Found) error occurs.

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define a custom page for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    This function handles 404 errors and displays a custom message.
    """
    return (
        "<h1>Site Not Available</h1>"
        "<p>You see this page because there is no Web site at this address.</p>",
        404,
    )

# Define a generic route for testing purposes
@app.route("/")
def index():
    """
    Example route for the main page.
    """
    return "<h1>Welcome to the Website</h1><p>This is the home page.</p>"

if __name__ == "__main__":
    try:
        # Run the Flask development server
        app.run(debug=True, host="0.0.0.0", port=5000)
    except Exception as ex:
        # Handle any unexpected errors when starting the server
        print(f"An error occurred while starting the server: {ex}")
```

### Key Notes:
- This code uses Flask as the web server framework.
- The `@app.errorhandler(404)` decorator is used to define a custom handler for HTTP 404 errors.
- If the server cannot find a route matching the requested URL, it will display the custom error message.
- Proper error handling is implemented to catch unexpected issues when starting the server.

To run the code, install Flask (`pip install flask`), save the script to a file (e.g., `app.py`), and execute it (`python app.py`).
