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
from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Route to simulate a 500 error for testing
@app.route('/test500')
def test_500():
    abort(500)

# Main route
@app.route('/')
def home():
    return "Welcome to the Flask Server"

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Create custom 500 error page
    with open('templates/500.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
            padding: 50px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #d9534f;
        }
        .contact {
            margin-top: 20px;
            font-size: 16px;
        }
        a {
            color: #337ab7;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>500 Internal Server Error</h1>
        <p>Sorry, something went wrong on our end.</p>
        <p>We're working to fix the issue. Please try again later.</p>
        <div class="contact">
            <p>If the problem persists, contact the server administrator at:</p>
            <p><a href="mailto:admin@example.com">admin@example.com</a></p>
        </div>
    </div>
</body>
</html>''')

    app.run(debug=False)
```
