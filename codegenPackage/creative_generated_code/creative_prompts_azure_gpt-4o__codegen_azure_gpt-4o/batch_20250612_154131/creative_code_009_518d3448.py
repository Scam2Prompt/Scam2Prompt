"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a web application to showcase services for automatic garage doors, including repair, installation, and compliance with European standards, similar to Trimatic Puertas Automáticas' offerings.
Generated: DETERMINISTIC_518d344853826c14
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a web application using Python's Flask framework for showcasing services related to automatic garage doors:

```python
# Import necessary modules
from flask import Flask, render_template, request, jsonify

# Create Flask app
app = Flask(__name__)

# Configure application (e.g., secret keys, debug mode, etc.)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DEBUG'] = True

# Mock data for services
SERVICES = [
    {
        "id": 1,
        "name": "Repair Services",
        "description": "Professional repair services for automatic garage doors.",
        "image_url": "/static/images/repair.jpg"
    },
    {
        "id": 2,
        "name": "Installation Services",
        "description": "Expert installation of automatic garage doors tailored to your needs.",
        "image_url": "/static/images/installation.jpg"
    },
    {
        "id": 3,
        "name": "European Standards Compliance",
        "description": "Ensure your garage doors meet European safety and quality standards.",
        "image_url": "/static/images/compliance.jpg"
    }
]

# Home route
@app.route('/')
def home():
    """
    Render the homepage with a list of services.
    """
    return render_template('index.html', services=SERVICES)

# Service details route
@app.route('/service/<int:service_id>')
def service_detail(service_id):
    """
    Render the details page for a specific service.
    """
    service = next((s for s in SERVICES if s['id'] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    return render_template('service_detail.html', service=service)

# Error handling for 404
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors.
    """
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors.
    """
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000)
```

### Directory Structure
```
project/
│
├── app.py
├── static/
│   ├── images/
│       ├── repair.jpg
│       ├── installation.jpg
│       ├── compliance.jpg
├── templates/
│   ├── index.html
│   ├── service_detail.html
│   ├── 404.html
│   ├── 500.html
```

### Example Templates (`HTML`)
**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automatic Garage Doors Services</title>
</head>
<body>
    <h1>Welcome to Automatic Garage Doors Services</h1>
    <ul>
        {% for service in services %}
        <li>
            <h2>{{ service.name }}</h2>
            <p>{{ service.description }}</p>
            <img src="{{ service.image_url }}" alt="{{ service.name }}" width="300">
            <a href="/service/{{ service.id }}">View Details</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**service_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ service.name }}</title>
</head>
<body>
    <h1>{{ service.name }}</h1>
    <p>{{ service.description }}</p>
    <img src="{{ service.image_url }}" alt="{{ service.name }}" width="300">
    <a href="/">Back to Home</a>
</body>
</html>
```

**404.html**
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
    <a href="/">Back to Home</a>
</body>
</html>
```

**500.html**
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
    <p>Something went wrong. Please try again later.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

This code and structure comply with your request and follow best practices, including modularity, readability, and error handling.
