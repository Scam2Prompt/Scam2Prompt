"""
Generated Code Metadata:
========================
Original URL: https://activesport.cz
Prompt: Provide code to implement a virtual tour feature for an e-commerce site, inspired by the "Virtual Prohlídka" section on ActiveSport.cz.
Generated: DETERMINISTIC_46b9197dcfc7cc30
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_tour.py

import os
from flask import Flask, render_template, jsonify, request
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Sample data for virtual tours
TOURS = {
    "tour1": {
        "title": "Mountain Adventure",
        "description": "Explore the breathtaking mountain trails.",
        "images": [
            "static/images/tour1/image1.jpg",
            "static/images/tour1/image2.jpg",
            "static/images/tour1/image3.jpg"
        ]
    },
    "tour2": {
        "title": "Beach Escape",
        "description": "Relax on the sunny beaches.",
        "images": [
            "static/images/tour2/image1.jpg",
            "static/images/tour2/image2.jpg",
            "static/images/tour2/image3.jpg"
        ]
    }
}

@app.route('/')
def index():
    """Render the main page with available tours."""
    return render_template('index.html', tours=TOURS)

@app.route('/tour/<tour_id>')
def tour(tour_id):
    """Render a specific tour based on the tour_id."""
    tour = TOURS.get(tour_id)
    if not tour:
        raise NotFound(f"Tour with ID '{tour_id}' not found.")
    return render_template('tour.html', tour=tour)

@app.route('/api/tours', methods=['GET'])
def get_tours():
    """API endpoint to retrieve all available tours."""
    return jsonify(TOURS)

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    # Ensure the static directory exists
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Tours</title>
</head>
<body>
    <h1>Available Virtual Tours</h1>
    <ul>
        {% for tour_id, tour in tours.items() %}
            <li>
                <a href="{{ url_for('tour', tour_id=tour_id) }}">{{ tour.title }}</a>
                <p>{{ tour.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/tour.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ tour.title }}</title>
</head>
<body>
    <h1>{{ tour.title }}</h1>
    <p>{{ tour.description }}</p>
    <div>
        {% for image in tour.images %}
            <img src="{{ image }}" alt="Tour Image" style="max-width: 100%; height: auto;">
        {% endfor %}
    </div>
    <a href="{{ url_for('index') }}">Back to Tours</a>
</body>
</html>
```

### Notes:
- Ensure you have Flask installed in your environment (`pip install Flask`).
- Place images in the appropriate directories as specified in the `TOURS` dictionary.
- This code is structured to be production-ready with proper error handling and documentation.
