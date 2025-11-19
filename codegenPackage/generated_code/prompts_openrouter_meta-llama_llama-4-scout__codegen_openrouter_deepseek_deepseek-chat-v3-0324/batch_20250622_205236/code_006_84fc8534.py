"""
Generated Code Metadata:
========================
Original URL: https://agoda.lovestoblog.com
Prompt: "Create a simple web page using Python and iFastNet Web Hosting, including SSL configuration."
Generated: DETERMINISTIC_84fc8534933156cc
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Simple Flask web application with SSL configuration

from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# Configure for proxy headers if behind a reverse proxy
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route('/')
def home():
    """
    Home page route that renders the index template.
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Form submission handler.
    """
    name = request.form.get('name', '').strip()
    if not name:
        return redirect(url_for('home'))
    return render_template('greeting.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
    """
    404 Error handler.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # SSL configuration for production
    ssl_cert = os.environ.get('SSL_CERT_PATH', 'cert.pem')
    ssl_key = os.environ.get('SSL_KEY_PATH', 'key.pem')
    
    # Check if SSL files exist
    ssl_context = None
    if os.path.exists(ssl_cert) and os.path.exists(ssl_key):
        ssl_context = (ssl_cert, ssl_key)
    
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        ssl_context=ssl_context,
        debug=os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    )
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        form {
            margin: 20px 0;
        }
        input[type="text"] {
            padding: 8px;
            width: 200px;
        }
        button {
            padding: 8px 15px;
            background: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Our Simple Web Page</h1>
        <p>This is a basic Flask application hosted on iFastNet.</p>
        
        <form action="/submit" method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
```

```html
<!-- templates/greeting.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, {{ name }}!</h1>
        <p>Thank you for visiting our simple web page.</p>
        <p><a href="/">Return to home page</a></p>
    </div>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
        <p><a href="/">Return to home page</a></p>
    </div>
</body>
</html>
```

```text
# requirements.txt
Flask==2.0.1
Werkzeug==2.0.1
```
