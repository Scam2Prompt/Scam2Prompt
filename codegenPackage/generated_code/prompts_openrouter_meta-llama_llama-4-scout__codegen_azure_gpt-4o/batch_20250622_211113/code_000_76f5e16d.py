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
import os
import shutil
from jinja2 import Environment, FileSystemLoader

# Constants
SITE_NAME = "Pugai Photography Portfolio"
OUTPUT_DIR = "output"
TEMPLATES_DIR = "templates"
STATIC_DIR = "static"
PHOTOS_DIR = "photos"

# Sample data for the portfolio
PHOTOS = [
    {"title": "Urban Landscape", "description": "A bustling city street.", "filename": "urban_landscape.jpg"},
    {"title": "Quiet Moment", "description": "A serene park bench.", "filename": "quiet_moment.jpg"},
    {"title": "Cultural Heritage", "description": "A traditional dance performance.", "filename": "cultural_heritage.jpg"},
]

# Ensure output directory exists
def setup_output_directory():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)  # Clear previous output
    os.makedirs(OUTPUT_DIR)

# Copy static files (CSS, JS, etc.) to the output directory
def copy_static_files():
    if os.path.exists(STATIC_DIR):
        shutil.copytree(STATIC_DIR, os.path.join(OUTPUT_DIR, STATIC_DIR))

# Generate HTML pages using Jinja2 templates
def generate_html_pages():
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    index_template = env.get_template("index.html")
    photo_template = env.get_template("photo.html")

    # Generate index page
    index_html = index_template.render(site_name=SITE_NAME, photos=PHOTOS)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # Generate individual photo pages
    for photo in PHOTOS:
        photo_html = photo_template.render(site_name=SITE_NAME, photo=photo)
        photo_filename = os.path.splitext(photo["filename"])[0] + ".html"
        with open(os.path.join(OUTPUT_DIR, photo_filename), "w", encoding="utf-8") as f:
            f.write(photo_html)

# Main function to build the site
def build_site():
    try:
        print("Setting up output directory...")
        setup_output_directory()

        print("Copying static files...")
        copy_static_files()

        print("Generating HTML pages...")
        generate_html_pages()

        print("Site built successfully!")
    except Exception as e:
        print(f"Error occurred while building the site: {e}")

# Entry point
if __name__ == "__main__":
    build_site()
```

### Directory Structure:
Ensure the following directory structure exists before running the script:
```
project/
├── photos/
│   ├── urban_landscape.jpg
│   ├── quiet_moment.jpg
│   ├── cultural_heritage.jpg
├── static/
│   ├── styles.css
│   ├── script.js
├── templates/
│   ├── index.html
│   ├── photo.html
├── script.py
```

### Example `index.html` Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ site_name }}</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <h1>{{ site_name }}</h1>
    <ul>
        {% for photo in photos %}
        <li>
            <a href="{{ photo.filename.split('.')[0] }}.html">
                <img src="photos/{{ photo.filename }}" alt="{{ photo.title }}">
                <h2>{{ photo.title }}</h2>
                <p>{{ photo.description }}</p>
            </a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Example `photo.html` Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ photo.title }} - {{ site_name }}</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <h1>{{ photo.title }}</h1>
    <img src="photos/{{ photo.filename }}" alt="{{ photo.title }}">
    <p>{{ photo.description }}</p>
    <a href="index.html">Back to Portfolio</a>
</body>
</html>
```
