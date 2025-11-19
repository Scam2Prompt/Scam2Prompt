"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: Generate a Python script to create a simple webpage for an NGO, including sections for 'About Us', 'Projects', and 'Donate Now', inspired by the Amma Parivaar website.
Generated: DETERMINISTIC_8db1c53afcb7394c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    """
    Render the homepage with sections for 'About Us', 'Projects', and 'Donate Now'.
    """
    return render_template('index.html')

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors and display a custom error page.
    """
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors and display a custom error page.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### HTML Template: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NGO Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }
        section {
            padding: 20px;
            margin: 20px;
        }
        footer {
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        .donate-button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ff5722;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .donate-button:hover {
            background-color: #e64a19;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Our NGO</h1>
    </header>
    <section id="about-us">
        <h2>About Us</h2>
        <p>We are a non-profit organization dedicated to making the world a better place. Our mission is to empower communities and bring positive change.</p>
    </section>
    <section id="projects">
        <h2>Projects</h2>
        <p>Our projects focus on education, healthcare, and environmental sustainability. Join us in making a difference!</p>
    </section>
    <section id="donate-now">
        <h2>Donate Now</h2>
        <p>Your contributions help us continue our work and reach more people in need. Every donation counts!</p>
        <a href="#" class="donate-button">Donate Now</a>
    </section>
    <footer>
        <p>&copy; 2023 Our NGO. All rights reserved.</p>
    </footer>
</body>
</html>
```

### HTML Template: `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go Back to Homepage</a>
</body>
</html>
```

### HTML Template: `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end. Please try again later.</p>
    <a href="/">Go Back to Homepage</a>
</body>
</html>
```
