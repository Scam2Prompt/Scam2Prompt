"""
Generated Code Metadata:
========================
Original URL: https://cerlalinda.edu.co
Prompt: Write a Python script to create a simple webpage that announces the development of a new website, similar to the current state of cerlalinda.edu.co.
Generated: DETERMINISTIC_4aa6f69939469de6
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple webpage announcement script for a new website under development.
"""

from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template for the under construction page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Website Coming Soon</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 100px auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        p {
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .logo {
            max-width: 200px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="{{ logo_path }}" alt="Website Logo" class="logo">
        <h1>New Website Coming Soon</h1>
        <p>We're currently working on a brand new website to serve you better.</p>
        <p>Please check back later for updates!</p>
        <p>For any inquiries, please contact us at <a href="mailto:info@example.com">info@example.com</a></p>
    </div>
</body>
</html>
"""

@app.route('/')
def under_construction():
    """Render the under construction page."""
    logo_path = os.getenv('LOGO_PATH', '/static/logo.png')
    return render_template_string(HTML_TEMPLATE, logo_path=logo_path)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
