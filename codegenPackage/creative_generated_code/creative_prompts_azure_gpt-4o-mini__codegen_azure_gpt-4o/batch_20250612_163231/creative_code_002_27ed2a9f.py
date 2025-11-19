"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomslens.com
Prompt: Write a script that dynamically displays a freelance artist's portfolio, inspired by the layout of Dulce Mendes' PhantomsLens.
Generated: DETERMINISTIC_27ed2a9f8c3eccd6
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python Flask application to dynamically display a freelance artist's portfolio.
Inspired by Dulce Mendes' PhantomsLens layout.

Features:
- Dynamic portfolio content
- Responsive image and project layout
- Error handling for missing assets
"""

from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Configuration for portfolio assets folder
PORTFOLIO_FOLDER = 'static/portfolio_assets'

# Ensure portfolio assets folder exists
if not os.path.exists(PORTFOLIO_FOLDER):
    os.makedirs(PORTFOLIO_FOLDER)

# Portfolio Data (Dummy Data for Demonstration)
portfolio_data = [
    {
        'title': 'Oil Painting Artwork',
        'description': 'A landscape painting showcasing vibrant colors and depth.',
        'image': 'oil_painting.jpg'  # Ensure this file exists in PORTFOLIO_FOLDER
    },
    {
        'title': 'Digital Art Series',
        'description': 'A series of digital artworks exploring geometric forms.',
        'image': 'digital_art.jpg'  # Ensure this file exists in PORTFOLIO_FOLDER
    },
    {
        'title': 'Portrait Sketch',
        'description': 'A detailed pencil sketch of a person.',
        'image': 'portrait_sketch.jpg'  # Ensure this file exists in PORTFOLIO_FOLDER
    }
]


@app.route('/')
def portfolio():
    """
    Route to display the artist's portfolio.
    The data is passed dynamically to the template.
    """
    return render_template('portfolio.html', portfolio_data=portfolio_data)


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({'error': 'Page not found'}), 404


@app.errorhandler(500)
def server_error(e):
    """
    Custom error handler for internal server errors (500).
    """
    return jsonify({'error': 'Internal server error'}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

"""
Below is the corresponding HTML file (`templates/portfolio.html`) for this Flask application.
Make sure to place it in a folder named 'templates'.
"""

# portfolio.html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artist Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .portfolio {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 1rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        .portfolio-item {
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .portfolio-item img {
            width: 100%;
            height: auto;
            display: block;
        }
        .portfolio-item .details {
            padding: 1rem;
        }
        .portfolio-item .details h3 {
            margin: 0;
            font-size: 1.5rem;
            color: #333;
        }
        .portfolio-item .details p {
            margin: 0.5rem 0 0;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1 style="text-align: center; padding: 1rem; background-color: #333; color: #fff;">Artist Portfolio</h1>
    </header>
    <main>
        <div class="portfolio">
            {% for item in portfolio_data %}
                <div class="portfolio-item">
                    <img src="{{ url_for('static', filename='portfolio_assets/' + item.image) }}" alt="{{ item.title }}">
                    <div class="details">
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.description }}</p>
                    </div>
                </div>
            {% endfor %}
        </div>
    </main>
</body>
</html>
"""
```
