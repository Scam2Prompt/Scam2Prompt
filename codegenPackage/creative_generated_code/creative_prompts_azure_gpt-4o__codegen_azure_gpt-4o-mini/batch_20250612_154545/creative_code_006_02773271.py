"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write code to display a gallery of airbrush nail art designs, including categories like "Fantasy Nails" and "Geometric Space," using images from AirstyleArt.
Generated: DETERMINISTIC_02773271577f4767
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the directory where images are stored
IMAGE_DIR = 'static/images/airbrush_nails'

# Define categories and their corresponding image files
GALLERY_CATEGORIES = {
    "Fantasy Nails": [
        "fantasy1.jpg",
        "fantasy2.jpg",
        "fantasy3.jpg"
    ],
    "Geometric Space": [
        "geometric1.jpg",
        "geometric2.jpg",
        "geometric3.jpg"
    ]
}

@app.route('/')
def gallery():
    """
    Render the main gallery page with all categories and images.
    """
    return render_template('gallery.html', categories=GALLERY_CATEGORIES)

@app.route('/view/<category_name>')
def view_category(category_name):
    """
    Render a specific category page displaying images.
    
    Args:
        category_name (str): The name of the category to display.

    Returns:
        Rendered HTML template or redirect if category is invalid.
    """
    if category_name not in GALLERY_CATEGORIES:
        # Redirect to the main gallery if the category is invalid
        return redirect(url_for('gallery'))
    
    images = GALLERY_CATEGORIES[category_name]
    return render_template('category.html', category=category_name, images=images)

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

```html
<!-- templates/gallery.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Airbrush Nail Art Gallery</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Airbrush Nail Art Gallery</h1>
    <div class="gallery">
        {% for category, images in categories.items() %}
            <div class="category">
                <h2>{{ category }}</h2>
                <a href="{{ url_for('view_category', category_name=category) }}">
                    <img src="{{ url_for('static', filename='images/airbrush_nails/' + images[0]) }}" alt="{{ category }}">
                </a>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- templates/category.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ category }} - Airbrush Nail Art Gallery</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>{{ category }}</h1>
    <div class="image-gallery">
        {% for image in images %}
            <img src="{{ url_for('static', filename='images/airbrush_nails/' + image) }}" alt="{{ category }} design">
        {% endfor %}
    </div>
    <a href="{{ url_for('gallery') }}">Back to Gallery</a>
</body>
</html>
```

```css
/* static/style.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

h1 {
    text-align: center;
    margin-top: 20px;
}

.gallery, .image-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
}

.category, .image-gallery img {
    margin: 10px;
    border: 2px solid #ccc;
    border-radius: 5px;
}

.category img {
    height: 150px;
    width: auto;
}

.image-gallery img {
    height: 200px;
    width: auto;
}
```

Make sure to create the directories and place your images as required for the application to run correctly.
