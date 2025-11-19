"""
Generated Code Metadata:
========================
Original URL: https://pugai.me
Prompt: Write a Python script to create a photography portfolio website using a static site generator, inspired by Pugai's documentary photography style.
Generated: DETERMINISTIC_76f5e16d6343a1be
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import datetime
from jinja2 import Template, Environment, FileSystemLoader
from PIL import Image

# Define constants
PORTFOLIO_DIR = 'portfolio'
IMAGES_DIR = 'images'
THUMBNAILS_DIR = 'thumbnails'
INDEX_TEMPLATE = 'index.jinja2'
PHOTO_TEMPLATE = 'photo.jinja2'

# Create directories if they don't exist
def create_directories():
    """Create directories for portfolio, images, and thumbnails if they don't exist"""
    for dir in [PORTFOLIO_DIR, IMAGES_DIR, THUMBNAILS_DIR]:
        if not os.path.exists(dir):
            os.makedirs(dir)

# Load Jinja2 templates
def load_templates():
    """Load Jinja2 templates from the templates directory"""
    template_dir = 'templates'
    env = Environment(loader=FileSystemLoader(template_dir))
    index_template = env.get_template(INDEX_TEMPLATE)
    photo_template = env.get_template(PHOTO_TEMPLATE)
    return index_template, photo_template

# Generate thumbnails for images
def generate_thumbnails(image_path):
    """Generate thumbnails for images"""
    try:
        image = Image.open(image_path)
        image.thumbnail((200, 200))  # Resize to 200x200
        thumbnail_path = os.path.join(THUMBNAILS_DIR, os.path.basename(image_path))
        image.save(thumbnail_path)
        return thumbnail_path
    except Exception as e:
        print(f"Error generating thumbnail for {image_path}: {str(e)}")
        return None

# Create portfolio pages
def create_portfolio_pages(index_template, photo_template):
    """Create portfolio pages"""
    try:
        # Get list of image files
        image_files = [f for f in os.listdir(IMAGES_DIR) if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        # Create index page
        index_data = {
            'title': 'Photography Portfolio',
            'images': image_files
        }
        index_html = index_template.render(index_data)
        with open(os.path.join(PORTFOLIO_DIR, 'index.html'), 'w') as f:
            f.write(index_html)

        # Create photo pages
        for image_file in image_files:
            image_path = os.path.join(IMAGES_DIR, image_file)
            thumbnail_path = generate_thumbnails(image_path)
            if thumbnail_path:
                photo_data = {
                    'title': image_file,
                    'image': image_file,
                    'thumbnail': os.path.basename(thumbnail_path)
                }
                photo_html = photo_template.render(photo_data)
                with open(os.path.join(PORTFOLIO_DIR, f'{os.path.splitext(image_file)[0]}.html'), 'w') as f:
                    f.write(photo_html)
    except Exception as e:
        print(f"Error creating portfolio pages: {str(e)}")

# Main function
def main():
    create_directories()
    index_template, photo_template = load_templates()
    create_portfolio_pages(index_template, photo_template)

if __name__ == '__main__':
    main()
```

**templates/index.jinja2**
```jinja2
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <ul>
    {% for image in images %}
        <li><a href="{{ image | replace('.jpg', '.html') }}">{{ image }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/photo.jinja2**
```jinja2
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <img src="{{ image }}" alt="{{ title }}">
    <p><a href="../index.html">Back to index</a></p>
</body>
</html>
```
