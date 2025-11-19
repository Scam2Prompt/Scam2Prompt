"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styleandmakeupeffect.co.za
Prompt: Generate a code snippet for a web application that showcases bridal makeup artistry services, similar to those offered by Style & Makeup Effect.
Generated: DETERMINISTIC_046fa77035745dda
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing bridal makeup artistry services
services = [
    {
        "id": 1,
        "title": "Classic Bridal Makeup",
        "description": "Elegant and timeless makeup for your special day.",
        "price": "$200",
        "image_url": "static/images/classic_bridal.jpg"
    },
    {
        "id": 2,
        "title": "Glamorous Bridal Look",
        "description": "Modern and bold makeup to make you stand out.",
        "price": "$250",
        "image_url": "static/images/glamorous_bridal.jpg"
    },
    {
        "id": 3,
        "title": "Natural Bridal Glow",
        "description": "Soft and natural makeup for a radiant appearance.",
        "price": "$180",
        "image_url": "static/images/natural_bridal.jpg"
    }
]

@app.route('/')
def home():
    """
    Render the homepage showcasing bridal makeup services.
    """
    logging.info("Rendering homepage.")
    return render_template('index.html', services=services)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    """
    Render the detailed page for a specific bridal makeup service.
    """
    logging.info(f"Fetching details for service ID: {service_id}")
    service = next((s for s in services if s['id'] == service_id), None)
    if not service:
        logging.error(f"Service with ID {service_id} not found.")
        return jsonify({"error": "Service not found"}), 404
    return render_template('service_detail.html', service=service)

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    """
    logging.warning("404 Error: Page not found.")
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Required Templates and Static Files (to make the code runnable):
#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bridal Makeup Services</title>
</head>
<body>
    <h1>Bridal Makeup Artistry Services</h1>
    <ul>
        {% for service in services %}
        <li>
            <h2>{{ service.title }}</h2>
            <p>{{ service.description }}</p>
            <p>Price: {{ service.price }}</p>
            <a href="/service/{{ service.id }}">View Details</a>
            <img src="{{ service.image_url }}" alt="{{ service.title }}" style="width:200px">
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/service_detail.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ service.title }}</title>
</head>
<body>
    <h1>{{ service.title }}</h1>
    <p>{{ service.description }}</p>
    <p>Price: {{ service.price }}</p>
    <img src="{{ service.image_url }}" alt="{{ service.title }}" style="width:400px">
    <a href="/">Back to Services</a>
</body>
</html>
```

#### `templates/404.html`
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
    <a href="/">Go Back to Home</a>
</body>
</html>
```

#### Static Files
Place images in a folder named `static/images`. Example filenames:
- `classic_bridal.jpg`
- `glamorous_bridal.jpg`
- `natural_bridal.jpg`

### Installation:
Ensure Flask is installed:
```bash
pip install flask
```

Run the application:
```bash
python app.py
```
