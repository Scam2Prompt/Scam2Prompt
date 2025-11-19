"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavego.dk
Prompt: Develop a web application feature that showcases images of the holiday houses in Thy, Denmark, highlighting the Nordic architectural themes and outdoor living spaces.
Generated: DETERMINISTIC_45a5493c23157c4d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application to showcase holiday houses in Thy, Denmark.
# Highlights Nordic architectural themes and outdoor living spaces.

from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Mocked data: holiday house images and info
# In a production app, this would come from a database or an external API.
holiday_houses = [
    {
        "id": 1,
        "name": "Coastal Retreat",
        "image_url": "/static/images/coastal_retreat.jpg",
        "description": "A modern Nordic coastal house with serene outdoor views.",
    },
    {
        "id": 2,
        "name": "Forest Haven",
        "image_url": "/static/images/forest_haven.jpg",
        "description": "A wooden cabin surrounded by lush greenery.",
    },
    {
        "id": 3,
        "name": "Lakeside Abode",
        "image_url": "/static/images/lakeside_abode.jpg",
        "description": "Minimalist Nordic-style house near a tranquil lake."
    }
]

# Route: Home page showcasing holiday houses
@app.route('/')
def home():
    """
    Renders the homepage with holiday house information.
    """
    return render_template('index.html', houses=holiday_houses)

# Route: API endpoint for holiday house data
@app.route('/api/houses', methods=['GET'])
def get_houses():
    """
    Returns JSON data about holiday houses.
    """
    return jsonify(holiday_houses)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors (Page Not Found).
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles 500 errors (Internal Server Error).
    """
    return render_template('500.html'), 500

# Static files directory
# Ensure the 'static' folder contains holiday house images.
def create_static_directories():
    """
    Ensures required static directories exist.
    """
    os.makedirs('static/images', exist_ok=True)

if __name__ == '__main__':
    create_static_directories()
    # Run the Flask application
    app.run(debug=True)
```

### Directory Structure:
```
- static/
  - images/
    - coastal_retreat.jpg
    - forest_haven.jpg
    - lakeside_abode.jpg
- templates/
  - index.html
  - 404.html
  - 500.html
```

### Template: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Holiday Houses in Thy, Denmark</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Holiday Houses in Thy, Denmark</h1>
    </header>
    <main>
        <section>
            {% for house in houses %}
            <div class="house">
                <h2>{{ house.name }}</h2>
                <img src="{{ house.image_url }}" alt="{{ house.name }}">
                <p>{{ house.description }}</p>
            </div>
            {% endfor %}
        </section>
    </main>
</body>
</html>
```

### Template: `404.html`
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
    <a href="/">Return to Homepage</a>
</body>
</html>
```

### Template: `500.html`
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
    <p>Something went wrong on our end. Please try again later.</p>
    <a href="/">Return to Homepage</a>
</body>
</html>
```
