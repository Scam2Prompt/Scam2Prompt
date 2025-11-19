"""
Generated Code Metadata:
========================
Original URL: https://uniapt.space
Prompt: "Design a simple web server using Flask that returns a custom 500 internal server error page, similar to the one seen on uniapt.space, with an email contact for server administrators."
Generated: DETERMINISTIC_2b8906b9db2deea7
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a custom 500 internal server error handler
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 internal server error handler.

    Returns a custom error page with contact information for server administrators.

    :param e: The error exception
    :return: A rendered HTML template with error information
    """
    # Log the error for debugging purposes
    app.logger.error(f"Internal Server Error: {e}")

    # Render a custom 500 error page
    return render_template("500.html"), 500

# Define a route for the root URL
@app.route("/")
def index():
    """
    A simple route to test the server.

    :return: A success message
    """
    return "Server is running."

# Define a custom error handler for a generic exception
@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Generic exception handler.

    Logs the error and returns a 500 internal server error.

    :param e: The error exception
    :return: A 500 internal server error
    """
    app.logger.error(f"Generic Exception: {e}")
    return internal_server_error(Exception("An unexpected error occurred."))

# Run the application if this script is executed directly
if __name__ == "__main__":
    # Set the logging level to DEBUG
    app.logger.setLevel("DEBUG")

    # Run the application on localhost at port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
```

**templates/500.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>500 Internal Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>An unexpected error occurred while processing your request.</p>
    <p>Please contact <a href="mailto:admin@example.com">admin@example.com</a> for assistance.</p>
</body>
</html>
```
