"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elan-life.com
Prompt: Generate a code snippet for a web application that displays image galleries categorized by lifestyle and travel, similar to the structure found on the élán-life website.
Generated: DETERMINISTIC_bd0a2c891451d6bc
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

# Base directory for image storage
BASE_DIR = 'static/images'

# Image categories 
CATEGORIES = ['lifestyle', 'travel']

@app.route('/')
def home():
    """
    Home page that lists available categories.
    """
    return render_template('index.html', categories=CATEGORIES)

@app.route('/gallery/<category>')
def gallery(category):
    """
    Display images for a specific category.
    
    :param category: The category of images to display (lifestyle or travel).
    :raises 404: If the category does not exist.
    """
    
    if category not in CATEGORIES:
        abort(404)

    # List images in category directory
    image_dir = os.path.join(BASE_DIR, category)
    try:
        images = os.listdir(image_dir)
    except FileNotFoundError:
        abort(404)

    images = [img for img in images if img.endswith(('.jpg', '.jpeg', '.png'))]
    
    return render_template('gallery.html', images=images, category=category)

@app.errorhandler(404)
def not_found(error):
    """
    Custom 404 error page.
    
    :param error: The error object.
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

**Templates Required:**

1. **index.html**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Image Gallery Home</title>
   </head>
   <body>
       <h1>Image Galleries</h1>
       <ul>
           {% for category in categories %}
               <li><a href="{{ url_for('gallery', category=category) }}">{{ category.capitalize() }}</a></li>
           {% endfor %}
       </ul>
   </body>
   </html>
   ```

2. **gallery.html**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{{ category.capitalize() }} Gallery</title>
   </head>
   <body>
       <h1>{{ category.capitalize() }} Gallery</h1>
       <div>
           {% for image in images %}
               <img src="{{ url_for('static', filename='images/' + category + '/' + image) }}" alt="{{ image }}">
           {% endfor %}
       </div>
       <a href="{{ url_for('home') }}">Back to Home</a>
   </body>
   </html>
   ```

3. **404.html**
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
       <a href="{{ url_for('home') }}">Back to Home</a>
   </body>
   </html>
   ```

**Directory Structure:**
```
/project_root
    /static
        /images
            /lifestyle
                image1.jpg
                image2.jpg
            /travel
                image1.jpg
                image2.jpg
    app.py
    templates/
        index.html
        gallery.html
        404.html
```

Make sure to create the required directories and images to test the application.
