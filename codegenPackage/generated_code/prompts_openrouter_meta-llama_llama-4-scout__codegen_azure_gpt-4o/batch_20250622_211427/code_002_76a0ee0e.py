"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Generate a code snippet for a travel consultancy website that showcases services like DMCC, MICE & Tourism Safaris, and Study Abroad facilitations.
Generated: DETERMINISTIC_76a0ee0e37ee45c1
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the services offered by the travel consultancy
services = [
    {
        "name": "DMCC (Destination Management Company Consultancy)",
        "description": "Providing expert guidance for destination management and event planning."
    },
    {
        "name": "MICE (Meetings, Incentives, Conferences, and Exhibitions)",
        "description": "Organizing corporate events, conferences, and exhibitions tailored to your needs."
    },
    {
        "name": "Tourism Safaris",
        "description": "Offering unforgettable safari experiences in exotic destinations."
    },
    {
        "name": "Study Abroad Facilitations",
        "description": "Helping students with admissions, visas, and accommodations for studying abroad."
    }
]

# Route to display the homepage
@app.route('/')
def homepage():
    """
    Render the homepage with a list of services.
    """
    return render_template('index.html', services=services)

# API route to fetch services as JSON
@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Return the list of services as a JSON response.
    """
    return jsonify(services)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors and return a custom error page.
    """
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors and return a custom error page.
    """
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(debug=True)
```

### HTML Templates (to be placed in a `templates` folder):

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Consultancy Services</title>
</head>
<body>
    <h1>Welcome to Our Travel Consultancy</h1>
    <h2>Our Services</h2>
    <ul>
        {% for service in services %}
        <li>
            <h3>{{ service.name }}</h3>
            <p>{{ service.description }}</p>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `404.html`
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
    <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end. Please try again later.</p>
</body>
</html>
```
