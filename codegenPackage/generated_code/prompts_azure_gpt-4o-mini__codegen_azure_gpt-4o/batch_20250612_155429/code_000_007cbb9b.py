"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Generate a code snippet for a web application that showcases a portfolio of luxury interior design projects, similar to those highlighted by Zirciulit Design Firm.
Generated: DETERMINISTIC_007cbb9bdb0f67ff
Batch ID: 20250612_155429
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Sample data for portfolio projects
# In a production environment, this data would typically come from a database
portfolio_projects = [
    {
        "id": 1,
        "title": "Modern Penthouse",
        "description": "A luxurious penthouse with modern aesthetics and high-end finishes.",
        "image_url": "/static/images/modern_penthouse.jpg"
    },
    {
        "id": 2,
        "title": "Classic Villa",
        "description": "A timeless villa design with elegant interiors and spacious layouts.",
        "image_url": "/static/images/classic_villa.jpg"
    },
    {
        "id": 3,
        "title": "Urban Loft",
        "description": "A chic urban loft with industrial design elements and open spaces.",
        "image_url": "/static/images/urban_loft.jpg"
    }
]

# Route to serve the homepage
@app.route('/')
def home():
    """
    Render the homepage with the portfolio projects.
    """
    return render_template('index.html', projects=portfolio_projects)

# API route to fetch portfolio projects as JSON
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Return the portfolio projects as JSON data.
    """
    try:
        return jsonify(portfolio_projects), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch projects", "details": str(e)}), 500

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors and return a custom error page.
    """
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Ensure the static folder exists for serving images
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    # Run the Flask application
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxury Interior Design Portfolio</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Luxury Interior Design Portfolio</h1>
    </header>
    <main>
        <section class="portfolio">
            {% for project in projects %}
            <div class="project">
                <img src="{{ project.image_url }}" alt="{{ project.title }}">
                <h2>{{ project.title }}</h2>
                <p>{{ project.description }}</p>
            </div>
            {% endfor %}
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Zirciulit Design Firm</p>
    </footer>
</body>
</html>
```

### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>404 - Page Not Found</h1>
    </header>
    <main>
        <p>Sorry, the page you are looking for does not exist.</p>
        <a href="/">Return to Home</a>
    </main>
</body>
</html>
```

### `static/styles.css`
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 2rem;
}

.portfolio {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
}

.project {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    width: 300px;
    text-align: center;
}

.project img {
    width: 100%;
    height: auto;
}

.project h2 {
    margin: 0.5rem 0;
}

.project p {
    padding: 0 1rem 1rem;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem;
    position: fixed;
    bottom: 0;
    width: 100%;
}
```
