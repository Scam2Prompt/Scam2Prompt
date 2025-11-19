"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: Generate a code snippet to set up a web server that displays a custom default page instead of the standard "no website at this address" message.
Generated: DETERMINISTIC_06b7c2f42488ecc5
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the requested code snippet in Python using Flask:

```python
from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# Custom HTML for the default page
custom_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
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
    <h1>Welcome to Our Website</h1>
    <p>We're working on something amazing. Stay tuned!</p>
</body>
</html>
"""

@app.route('/')
def default_page():
    """
    Route for the default page.
    Returns a custom HTML message when the user visits the root URL.
    """
    return render_template_string(custom_page_html)

@app.errorhandler(404)
def page_not_found(e):
    """
    Error handler for 404 Not Found.
    Displays the custom default page instead of the standard error message.
    """
    return render_template_string(custom_page_html), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handler for 500 Internal Server Error.
    Displays a user-friendly message.
    """
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Server Error</title>
        </head>
        <body style="text-align: center; font-family: Arial, sans-serif;">
            <h1>Something Went Wrong</h1>
            <p>Our team has been notified and is working to resolve the issue. Please try again later.</p>
        </body>
        </html>
    """), 500

# Entry point for running the application
if __name__ == '__main__':
    try:
        # Run the app on localhost and port 5000
        app.run(host='127.0.0.1', port=5000)
    except Exception as e:
        # Log any unexpected errors and exit gracefully
        print(f"Error starting the server: {str(e)}")
```

Save this code in a file (e.g., `app.py`) and run it using `python app.py`. Install Flask beforehand with `pip install flask` if not already installed.
