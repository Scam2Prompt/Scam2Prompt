"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Suggest a framework or library to create visually engaging portfolio pages showcasing high-end web design projects, as seen on ByAmed.net.
Generated: DETERMINISTIC_6afeffdbfb332c92
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application using Flask-Static-Digest and Jinja2 for portfolio pages
# This code creates a visually engaging portfolio website for showcasing high-end web design projects

from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__)

# Configuration for static assets digest (useful for cache-busting in production)
app.config['FLASK_STATIC_DIGEST'] = True

# Define the path to portfolio data
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')

# Utility function to load portfolio data from JSON files
def load_portfolio_data():
    try:
        with open(os.path.join(DATA_PATH, 'portfolio.json'), 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Log the error and return an empty list
        print(f"Error loading portfolio data: {e}")
        return []

# Route for the homepage
@app.route('/')
def index():
    # Load portfolio items from JSON data
    portfolio_items = load_portfolio_data()
    return render_template('index.html', items=portfolio_items)

# Route for individual portfolio item pages
@app.route('/portfolio/<int:item_id>')
def portfolio_item(item_id):
    portfolio_items = load_portfolio_data()
    # Find the portfolio item by ID
    item = next((item for item in portfolio_items if item['id'] == item_id), None)
    if not item:
        # Return a 404 error if item not found
        abort(404)
    return render_template('portfolio_item.html', item=item)

# Run the Flask application
if __name__ == '__main__':
    # Ensure the data directory exists
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    # Start the Flask app in debug mode for development
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
    </header>
    <main>
        <section class="portfolio-grid">
            {% for item in items %}
                <div class="portfolio-item">
                    <a href="{{ url_for('portfolio_item', item_id=item.id) }}">
                        <img src="{{ url_for('static', filename='images/' ~ item.image) }}" alt="{{ item.title }}">
                        <h2>{{ item.title }}</h2>
                    </a>
                </div>
            {% endfor %}
        </section>
    </main>
</body>
</html>
```

### `templates/portfolio_item.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ item.title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <a href="{{ url_for('index') }}">Back to Portfolio</a>
        <h1>{{ item.title }}</h1>
    </header>
    <main>
        <img src="{{ url_for('static', filename='images/' ~ item.image) }}" alt="{{ item.title }}">
        <p>{{ item.description }}</p>
    </main>
</body>
</html>
```

### `data/portfolio.json`
```json
[
    {
        "id": 1,
        "title": "Project One",
        "description": "High-end web design project with cutting-edge visuals and interactive elements.",
        "image": "project1.jpg"
    },
    {
        "id": 2,
        "title": "Project Two",
        "description": "An elegant and modern portfolio showcasing creative designs.",
        "image": "project2.jpg"
    }
]
```

### `static/css/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

h1 {
    margin: 0;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
}

.portfolio-item {
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    text-align: center;
}

.portfolio-item img {
    width: 100%;
    height: auto;
}

.portfolio-item h2 {
    margin: 10px 0;
    font-size: 1.2em;
}
```
