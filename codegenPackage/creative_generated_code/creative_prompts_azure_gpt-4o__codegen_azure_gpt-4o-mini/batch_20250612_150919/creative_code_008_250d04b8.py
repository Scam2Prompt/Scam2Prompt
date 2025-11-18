"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Recommend best practices for handling default system-generated pages in web hosting environments.
Generated: DETERMINISTIC_250d04b8f8d519af
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# Define a custom error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    # Render a custom 404 error page
    return render_template('404.html'), 404

# Function to check if the default system page exists
def check_default_page(page_name):
    # Construct the path to the default page
    page_path = os.path.join(app.root_path, 'templates', page_name)
    return os.path.isfile(page_path)

# Route to serve custom pages
@app.route('/<page_name>')
def serve_page(page_name):
    # Check if the requested page exists
    if check_default_page(page_name):
        return render_template(page_name)
    else:
        # If the page does not exist, return a 404 error
        abort(404)

if __name__ == '__main__':
    # Set debug=False for production to avoid displaying error details
    app.run(debug=False)
```

```html
<!-- 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Oops! The page you are looking for does not exist.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```
