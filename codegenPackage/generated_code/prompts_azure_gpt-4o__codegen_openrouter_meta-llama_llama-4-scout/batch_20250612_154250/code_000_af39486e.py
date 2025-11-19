"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Write a Python script to create a webpage showcasing the amenities of Dens Haven villas, including features like a swimming pool, clubhouse, landscaped garden, and CCTV monitoring system.
Generated: DETERMINISTIC_af39486e0fd1bb50
Batch ID: 20250612_154250
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
from jinja2 import Template

# Define a class for Amenities
class Amenities:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define amenities of Dens Haven villas
amenities = [
    Amenities("Swimming Pool", "A serene and refreshing pool for relaxation and recreation"),
    Amenities("Clubhouse", "A spacious and well-appointed clubhouse for social gatherings and events"),
    Amenities("Landscaped Garden", "A beautifully landscaped garden for a peaceful and calming ambiance"),
    Amenities("CCTV Monitoring System", "A state-of-the-art CCTV monitoring system for enhanced security and safety")
]

# Define HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dens Haven Villas Amenities</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .amenity {
            margin-bottom: 20px;
        }
        .amenity h2 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <h1>Dens Haven Villas Amenities</h1>
    {% for amenity in amenities %}
    <div class="amenity">
        <h2>{{ amenity.name }}</h2>
        <p>{{ amenity.description }}</p>
    </div>
    {% endfor %}
</body>
</html>
"""

# Render HTML template with amenities data
def render_html(amenities):
    try:
        template = Template(html_template)
        html = template.render(amenities=amenities)
        return html
    except Exception as e:
        print(f"Error rendering HTML: {str(e)}")
        return None

# Save HTML to file
def save_html(html, filename):
    try:
        with open(filename, "w") as f:
            f.write(html)
        print(f"HTML saved to {filename}")
    except Exception as e:
        print(f"Error saving HTML to file: {str(e)}")

# Main function
def main():
    html = render_html(amenities)
    if html:
        filename = "dens_haven_amenities.html"
        save_html(html, filename)

if __name__ == "__main__":
    main()
```
