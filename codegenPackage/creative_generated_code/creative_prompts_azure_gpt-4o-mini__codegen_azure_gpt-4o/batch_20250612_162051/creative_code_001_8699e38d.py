"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Write a code snippet for a web application that displays the amenities of a luxury villa, specifically highlighting features like smart TVs, WiFi, and a fully equipped kitchen, similar to those offered at Diamond Villa Corfu.
Generated: DETERMINISTIC_8699e38d4b72cc60
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Define villa amenities data structure
villa_amenities = {
    "name": "Diamond Villa Corfu",
    "features": [
        {"title": "Smart TVs", "description": "Luxury Smart TVs in all rooms with streaming services enabled."},
        {"title": "WiFi", "description": "High-speed fiber optic WiFi covering the entire villa."},
        {"title": "Fully Equipped Kitchen", "description": "Modern kitchen with premium appliances including oven, dishwasher, and coffee machine."},
    ]
}

@app.route("/")
def home():
    """
    Render the homepage displaying villa amenities.
    """
    return render_template("index.html", villa_amenities=villa_amenities)

@app.route("/api/amenities")
def get_amenities():
    """
    API endpoint to return villa amenities as JSON.
    """
    return jsonify(villa_amenities)

# Handle errors gracefully
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)
```

**HTML Template (`templates/index.html`)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ villa_amenities.name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .amenity {
            margin-bottom: 20px;
        }
        .amenity-title {
            font-size: 1.2em;
            font-weight: bold;
        }
        .amenity-description {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Welcome to {{ villa_amenities.name }}</h1>
    <h2>Amenities:</h2>
    <div>
        {% for feature in villa_amenities.features %}
        <div class="amenity">
            <div class="amenity-title">{{ feature.title }}</div>
            <div class="amenity-description">{{ feature.description }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```
