"""
Generated Code Metadata:
========================
Original URL: https://www.sgeek-seo.com
Prompt: Write a Python script to generate HTML5 or SVG diagrams using one of the free tools mentioned on the SGeek SEO website.
Generated: DETERMINISTIC_e672b8abf4367c36
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import svgwrite
from svgwrite import cm, mm

def create_svg_diagram(filename, width=210*mm, height=297*mm):
    """
    Create a simple SVG diagram and save it to a file.

    Parameters:
    filename (str): The name of the file to save the SVG diagram.
    width (float): The width of the SVG canvas.
    height (float): The height of the SVG canvas.
    """
    try:
        # Create an SVG drawing object
        dwg = svgwrite.Drawing(filename, profile='tiny', size=(width, height))

        # Add a rectangle to the SVG
        dwg.add(dwg.rect(insert=(10*mm, 10*mm), size=(100*mm, 50*mm), fill='lightblue', stroke='black'))

        # Add a circle to the SVG
        dwg.add(dwg.circle(center=(60*mm, 100*mm), r=20*mm, fill='orange', stroke='black'))

        # Add text to the SVG
        dwg.add(dwg.text('Hello, SVG!', insert=(20*mm, 30*mm), fill='black'))

        # Save the SVG file
        dwg.save()
        print(f"SVG diagram saved as '{filename}'.")

    except Exception as e:
        print(f"An error occurred while creating the SVG diagram: {e}")

if __name__ == "__main__":
    # Define the output filename
    output_filename = "diagram.svg"

    # Check if the output file already exists
    if os.path.exists(output_filename):
        print(f"Error: The file '{output_filename}' already exists. Please choose a different name.")
    else:
        # Create the SVG diagram
        create_svg_diagram(output_filename)
```
