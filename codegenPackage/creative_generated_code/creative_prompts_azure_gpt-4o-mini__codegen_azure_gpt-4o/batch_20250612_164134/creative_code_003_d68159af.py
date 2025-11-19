"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: What are the steps to customize the default page of a web server to improve user experience when the site is not available?
Generated: DETERMINISTIC_d68159af12c951aa
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code example using the Flask framework to customize the default page of a web server for user-friendly error handling when the site is not available. This includes a custom 404 error page.

```python
from flask import Flask, render_template

app = Flask(__name__)

# Custom error page for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors by displaying a custom page to improve user experience.
    :param e: The error object
    :return: Custom 404 page
    """
    return render_template('404.html'), 404

# Custom error page for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles 500 errors by displaying a custom page to improve user experience.
    :param e: The error object
    :return: Custom 500 page
    """
    return render_template('500.html'), 500

# Route for the home page
@app.route('/')
def home():
    """
    Main route of the web application.
    :return: A simple welcome message
    """
    return "Welcome to our site! Navigate to a non-existent URL to see the custom page."

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```

### File Structure
To make the above code work, ensure you have the following file structure:

```
/project_folder
  |-- app.py (the code above)
  |-- templates/
        |-- 404.html (custom HTML for 404 error)
        |-- 500.html (custom HTML for 500 error)
```

### Example `404.html`
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
        h1 {
            font-size: 50px;
        }
        p {
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Oops! The page you are looking for does not exist.</p>
    <a href="/">Go back to the home page</a>
</body>
</html>
```

### Example `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            font-size: 50px;
            color: red;
        }
        p {
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
    <a href="/">Go back to the home page</a>
</body>
</html>
```

### Notes:
- Replace `debug=True` with `debug=False` in the production environment.
- Customize the HTML pages to suit your site's branding and user experience needs.
