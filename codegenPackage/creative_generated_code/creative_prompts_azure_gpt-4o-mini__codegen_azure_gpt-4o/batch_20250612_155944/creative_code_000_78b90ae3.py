"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-7.webflow.io
Prompt: Generate a code snippet for a web application that showcases a portfolio of architectural projects similar to those featured on Linea 7's website, emphasizing user-centric design and functionality.
Generated: DETERMINISTIC_78b90ae3951f3584
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Sample portfolio data for demonstration
portfolio_data = [
    {
        "id": 1,
        "title": "Modern Residential Building",
        "description": "A sleek and modern residential project designed with sustainability in mind.",
        "image_url": "/static/images/residential.jpg",
        "tags": ["Residential", "Modern", "Sustainable"]
    },
    {
        "id": 2,
        "title": "Urban Office Space",
        "description": "An innovative office space that fosters creativity and collaboration.",
        "image_url": "/static/images/office.jpg",
        "tags": ["Commercial", "Urban", "Innovative"]
    },
    {
        "id": 3,
        "title": "Cultural Center",
        "description": "A cultural hub that brings communities together and celebrates the arts.",
        "image_url": "/static/images/cultural_center.jpg",
        "tags": ["Public", "Cultural", "Community"]
    }
]

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Home route - renders the portfolio page
@app.route("/")
def home():
    return render_template("portfolio.html", projects=portfolio_data)

if __name__ == "__main__":
    # Ensure the app runs on the specified port and debug mode is off for production.
    app.run(debug=False)

```

```html
<!-- templates/portfolio.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Architectural Portfolio</h1>
    </header>
    <main>
        <div class="portfolio-grid">
            <!-- Loop through projects passed from Flask -->
            {% for project in projects %}
            <div class="portfolio-item">
                <img src="{{ project.image_url }}" alt="{{ project.title }}">
                <h2>{{ project.title }}</h2>
                <p>{{ project.description }}</p>
                <div class="tags">
                    {% for tag in project.tags %}
                    <span class="tag">{{ tag }}</span>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </main>
    <footer>
        <p>&copy; 2023 Architectural Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* static/styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

main {
    padding: 20px;
}

.portfolio-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.portfolio-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    width: calc(33.333% - 20px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.portfolio-item img {
    width: 100%;
    height: auto;
}

.portfolio-item h2 {
    margin: 10px;
    font-size: 18px;
}

.portfolio-item p {
    margin: 10px;
    font-size: 14px;
    color: #555;
}

.tags {
    margin: 10px;
}

.tag {
    display: inline-block;
    background-color: #333;
    color: #fff;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 12px;
    margin-right: 5px;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
    position: absolute;
    width: 100%;
    bottom: 0;
}
```

### Notes:
1. Place `app.py` in the root directory of your project.
2. Place the HTML file in the `templates` directory.
3. Place the CSS file in the `static` directory.
4. Add sample images to the `static/images` directory with filenames `residential.jpg`, `office.jpg`, and `cultural_center.jpg`. Update paths as needed.
5. Install Flask using `pip install flask` before running the app with `python app.py`.
