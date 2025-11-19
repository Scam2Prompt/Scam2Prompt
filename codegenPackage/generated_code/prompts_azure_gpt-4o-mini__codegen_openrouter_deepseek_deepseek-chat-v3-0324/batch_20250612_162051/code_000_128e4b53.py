"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Generate a code snippet for a web application that displays a list of dining tables made from solid wood, highlighting unique features like the "Гранд Изида" and "Майк" models.
Generated: DETERMINISTIC_128e4b53689a2d52
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template
from typing import List, Dict

app = Flask(__name__)

# Sample data for solid wood dining tables
SOLID_WOOD_TABLES = [
    {
        "name": "Гранд Изида",
        "material": "Solid Oak",
        "dimensions": "200cm x 100cm x 75cm",
        "features": ["Hand-carved details", "Expandable design", "Antique finish"],
        "price": 1200.00,
        "image": "grand_izida.jpg"
    },
    {
        "name": "Майк",
        "material": "Solid Walnut",
        "dimensions": "180cm x 90cm x 74cm",
        "features": ["Minimalist design", "Hidden storage compartment", "Eco-friendly finish"],
        "price": 950.00,
        "image": "mike.jpg"
    },
    {
        "name": "Classic Oak",
        "material": "Solid Oak",
        "dimensions": "160cm x 80cm x 75cm",
        "features": ["Traditional design", "Sturdy construction"],
        "price": 750.00,
        "image": "classic_oak.jpg"
    }
]

@app.route('/')
def display_tables():
    """
    Render the main page displaying solid wood dining tables.
    Highlights special models like 'Гранд Изида' and 'Майк'.
    """
    return render_template('tables.html', tables=SOLID_WOOD_TABLES)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors gracefully"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors gracefully"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/tables.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solid Wood Dining Tables</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .table-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .table-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            transition: transform 0.3s;
        }
        .table-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .table-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 5px;
        }
        .highlight {
            border: 2px solid #d4af37;
            background-color: #fffdf5;
        }
        .price {
            font-weight: bold;
            color: #2a6496;
            font-size: 1.2em;
        }
        .features {
            margin-top: 10px;
        }
        .features li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <h1>Solid Wood Dining Tables</h1>
    <div class="table-container">
        {% for table in tables %}
        <div class="table-card {% if table.name in ['Гранд Изида', 'Майк'] %}highlight{% endif %}">
            <img src="{{ url_for('static', filename='images/' + table.image) }}" alt="{{ table.name }}">
            <h2>{{ table.name }}</h2>
            <p><strong>Material:</strong> {{ table.material }}</p>
            <p><strong>Dimensions:</strong> {{ table.dimensions }}</p>
            <p class="price">${{ "%.2f"|format(table.price) }}</p>
            <div class="features">
                <strong>Features:</strong>
                <ul>
                    {% for feature in table.features %}
                    <li>{{ feature }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for doesn't exist.</p>
    <a href="{{ url_for('display_tables') }}">Return to Home</a>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
    <a href="{{ url_for('display_tables') }}">Return to Home</a>
</body>
</html>
```
