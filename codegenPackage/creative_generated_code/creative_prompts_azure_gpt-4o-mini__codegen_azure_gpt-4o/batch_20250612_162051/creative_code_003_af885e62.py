"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amalfihospicecare.com
Prompt: Develop a simple web application using Flask that provides information on hospice care philosophy and services, similar to the offerings of Amalfi Hospice Care.
Generated: DETERMINISTIC_af885e62958ab7b2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules from Flask
from flask import Flask, render_template, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Hospice care information (mock data)
hospice_info = {
    "philosophy": "Hospice care focuses on providing comfort and support to individuals with life-limiting illnesses, ensuring dignity and quality of life in their final stages.",
    "services": [
        "Pain and symptom management",
        "Emotional and spiritual support",
        "Support for family and caregivers",
        "Bereavement counseling",
        "Coordination of care with other health providers"
    ]
}

# Route: Home page
@app.route("/")
def home():
    """
    Home page route.
    Returns a simple HTML page with information about hospice care philosophy and services.
    """
    return render_template("home.html", hospice_info=hospice_info)

# Route: JSON API for hospice information
@app.route("/api/hospice-info")
def api_hospice_info():
    """
    API endpoint for hospice care information.
    Returns hospice data in JSON format.
    """
    return jsonify(hospice_info)

# Error handling: 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    Returns a user-friendly message for pages that cannot be found.
    """
    return render_template("404.html"), 404

# Error handling: 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error handler.
    Returns a user-friendly message for server errors.
    """
    return render_template("500.html"), 500

# Main entry point
if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)

```

### Template files required:
1. **`home.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospice Care Information</title>
</head>
<body>
    <h1>Welcome to Hospice Care Information</h1>
    <h2>Philosophy</h2>
    <p>{{ hospice_info.philosophy }}</p>
    <h2>Services</h2>
    <ul>
        {% for service in hospice_info.services %}
        <li>{{ service }}</li>
        {% endfor %}
    </ul>
    <footer>
        <p>Amalfi Hospice Care – Supporting you with compassion and dignity.</p>
    </footer>
</body>
</html>
```

2. **`404.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, we couldn't find the page you were looking for.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```

3. **`500.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end. Please try again later.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```
