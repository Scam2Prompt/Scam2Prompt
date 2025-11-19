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
from pathlib import Path

# Define the project structure
PROJECT_NAME = "photography_portfolio"
STATIC_DIR = Path(PROJECT_NAME) / "static"
TEMPLATES_DIR = Path(PROJECT_NAME) / "templates"
OUTPUT_DIR = Path(PROJECT_NAME) / "output"

# Create necessary directories
def create_directories():
    """Create the necessary directories for the project."""
    try:
        os.makedirs(STATIC_DIR, exist_ok=True)
        os.makedirs(TEMPLATES_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        print("Directories created successfully.")
    except Exception as e:
        print(f"Error creating directories: {e}")

# Copy static files (like CSS, JS, images)
def copy_static_files():
    """Copy static files to the output directory."""
    try:
        # Example: Copy a CSS file
        css_source = Path("assets/css/style.css")
        if css_source.exists():
            shutil.copy(css_source, STATIC_DIR)
        else:
            print(f"Static file not found: {css_source}")

        # Copy images (assuming they are in 'assets/images')
        images_source = Path("assets/images")
        if images_source.exists():
            for img in images_source.glob("*"):
                shutil.copy(img, STATIC_DIR)
        else:
            print(f"Images directory not found: {images_source}")

        print("Static files copied successfully.")
    except Exception as e:
        print(f"Error copying static files: {e}")

# Create a basic HTML template
def create_template():
    """Create a basic HTML template for the portfolio."""
    template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/style.css">
    <title>Photography Portfolio</title>
</head>
<body>
    <header>
        <h1>My Photography Portfolio</h1>
    </header>
    <main>
        <section id="gallery">
            <!-- Gallery images will be inserted here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 My Photography Portfolio</p>
    </footer>
</body>
</html>
"""
    try:
        with open(TEMPLATES_DIR / "index.html", "w") as f:
            f.write(template_content)
        print("Template created successfully.")
    except Exception as e:
        print(f"Error creating template: {e}")

# Generate the portfolio website
def generate_website():
    """Generate the portfolio website by copying templates and static files."""
    try:
        # Copy static files
        copy_static_files()
        
        # Create HTML template
        create_template()

        # Copy the template to the output directory
        shutil.copy(TEMPLATES_DIR / "index.html", OUTPUT_DIR)
        print("Website generated successfully.")
    except Exception as e:
        print(f"Error generating website: {e}")

if __name__ == "__main__":
    create_directories()
    generate_website()
```

This script sets up a basic structure for a photography portfolio website using a static site generator approach. It creates necessary directories, copies static files, and generates a simple HTML template. Make sure to have the required assets in the specified directories before running the script.
