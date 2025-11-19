"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Develop a simple web application using Flask that provides information on hospice care philosophy and services, similar to the offerings of Amalfi Hospice Care.
Generated: DETERMINISTIC_af885e62958ab7b2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for hospice care philosophy and services
hospice_data = {
    "philosophy": "Hospice care focuses on providing comfort and support to patients and their families during the end-of-life journey. It emphasizes dignity, compassion, and quality of life.",
    "services": [
        "Pain and symptom management",
        "Emotional and spiritual support",
        "Assistance with daily activities",
        "Bereavement support for families",
        "Coordination of care with healthcare providers"
    ]
}

@app.route('/')
def home():
    """
    Home route that renders the main page.
    """
    return render_template('index.html', title="Hospice Care Information")

@app.route('/api/philosophy', methods=['GET'])
def get_philosophy():
    """
    API endpoint to retrieve hospice care philosophy.
    """
    return jsonify({"philosophy": hospice_data["philosophy"]})

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    API endpoint to retrieve hospice care services.
    """
    return jsonify({"services": hospice_data["services"]})

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Page not found"}), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### `templates/index.html` (HTML Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        main {
            padding: 2rem;
        }
        footer {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Hospice Care Information</h1>
    </header>
    <main>
        <h2>Welcome to our Hospice Care Information Portal</h2>
        <p>Learn more about our philosophy and services by accessing the API endpoints:</p>
        <ul>
            <li><a href="/api/philosophy" target="_blank">Philosophy</a></li>
            <li><a href="/api/services" target="_blank">Services</a></li>
        </ul>
    </main>
    <footer>
        <p>&copy; 2023 Hospice Care Information</p>
    </footer>
</body>
</html>
```
