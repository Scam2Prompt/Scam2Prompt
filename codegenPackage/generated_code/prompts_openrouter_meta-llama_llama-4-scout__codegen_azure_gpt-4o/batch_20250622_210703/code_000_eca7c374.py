"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: "Generate a website design package for a small business, including logo design, social graphics, and basic SEO, similar to Henfruit's web design services."
Generated: DETERMINISTIC_eca7c374fef10a69
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python script that automates the generation of a website design package for a small business. It includes logo design, social media graphics, and basic SEO metadata generation. This script uses popular libraries such as `Pillow` for image creation and `jinja2` for HTML templating.

```python
import os
from PIL import Image, ImageDraw, ImageFont
from jinja2 import Environment, FileSystemLoader
import json

# Constants
OUTPUT_DIR = "design_package"
LOGO_FILE = "logo.png"
SOCIAL_GRAPHICS_DIR = "social_graphics"
SEO_FILE = "seo_metadata.json"

# Ensure output directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, SOCIAL_GRAPHICS_DIR), exist_ok=True)

# Function to create a simple logo
def create_logo(business_name):
    try:
        # Create a blank image for the logo
        logo_size = (400, 200)
        logo = Image.new("RGB", logo_size, color="white")
        draw = ImageDraw.Draw(logo)

        # Add text to the logo
        font = ImageFont.load_default()
        text = business_name
        text_size = draw.textsize(text, font=font)
        text_position = ((logo_size[0] - text_size[0]) // 2, (logo_size[1] - text_size[1]) // 2)
        draw.text(text_position, text, fill="black", font=font)

        # Save the logo
        logo_path = os.path.join(OUTPUT_DIR, LOGO_FILE)
        logo.save(logo_path)
        print(f"Logo created: {logo_path}")
    except Exception as e:
        print(f"Error creating logo: {e}")

# Function to create social media graphics
def create_social_graphics(business_name):
    try:
        platforms = ["facebook", "twitter", "instagram"]
        graphic_size = (800, 800)

        for platform in platforms:
            graphic = Image.new("RGB", graphic_size, color="lightblue")
            draw = ImageDraw.Draw(graphic)

            # Add text to the graphic
            font = ImageFont.load_default()
            text = f"{business_name} - {platform.capitalize()}"
            text_size = draw.textsize(text, font=font)
            text_position = ((graphic_size[0] - text_size[0]) // 2, (graphic_size[1] - text_size[1]) // 2)
            draw.text(text_position, text, fill="black", font=font)

            # Save the graphic
            graphic_path = os.path.join(OUTPUT_DIR, SOCIAL_GRAPHICS_DIR, f"{platform}.png")
            graphic.save(graphic_path)
            print(f"Social graphic created: {graphic_path}")
    except Exception as e:
        print(f"Error creating social graphics: {e}")

# Function to generate basic SEO metadata
def generate_seo_metadata(business_name, description, keywords):
    try:
        seo_data = {
            "title": business_name,
            "description": description,
            "keywords": keywords,
        }

        seo_path = os.path.join(OUTPUT_DIR, SEO_FILE)
        with open(seo_path, "w") as seo_file:
            json.dump(seo_data, seo_file, indent=4)
        print(f"SEO metadata created: {seo_path}")
    except Exception as e:
        print(f"Error generating SEO metadata: {e}")

# Function to generate a basic HTML template
def generate_html_template(business_name):
    try:
        # Set up Jinja2 environment
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("index.html")

        # Render the template
        rendered_html = template.render(business_name=business_name)

        # Save the rendered HTML
        html_path = os.path.join(OUTPUT_DIR, "index.html")
        with open(html_path, "w") as html_file:
            html_file.write(rendered_html)
        print(f"HTML template created: {html_path}")
    except Exception as e:
        print(f"Error generating HTML template: {e}")

# Main function
def main():
    business_name = "Your Business Name"
    description = "A brief description of your business."
    keywords = ["business", "services", "products"]

    print("Generating website design package...")
    create_logo(business_name)
    create_social_graphics(business_name)
    generate_seo_metadata(business_name, description, keywords)
    generate_html_template(business_name)
    print("Website design package generated successfully!")

if __name__ == "__main__":
    main()
```

### Notes:
1. **Templates Directory**: Ensure you have a `templates` directory with an `index.html` file for the HTML template. Example content for `index.html`:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{{ business_name }}</title>
   </head>
   <body>
       <h1>Welcome to {{ business_name }}</h1>
       <p>Your business description goes here.</p>
   </body>
   </html>
   ```

2. **Dependencies**: Install required libraries using:
   ```bash
   pip install pillow jinja2
   ```

3. **Error Handling**: The script includes basic error handling to ensure robustness.
