"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Write a tutorial on how to create a comic book page layout, referencing the comic art courses available at Ânima.
Generated: DETERMINISTIC_47f39ba35b21d63d
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that acts as a tutorial for creating a basic comic book page layout using the Python `Pillow` library. It also references comic art courses available at Ânima in the comments.

```python
"""
Comic Book Page Layout Generator
This script generates a simple comic book page layout using Python's Pillow library.
It demonstrates how to divide a page into panels of different sizes and arrange them visually.

References:
- Ânima offers courses on comic art that can help you master panel design, character drawing, and storytelling.
- Visit Ânima's website to learn more about their comic art courses and enhance your skills.

Requirements:
- Python 3.x
- Pillow (Python Imaging Library)

Install Pillow: pip install pillow
"""

from PIL import Image, ImageDraw

# Constants for page and panel dimensions
PAGE_WIDTH = 800  # Width of the comic book page
PAGE_HEIGHT = 1200  # Height of the comic book page
PANEL_MARGIN = 10  # Margin between panels
BACKGROUND_COLOR = (255, 255, 255)  # White background color
PANEL_BORDER_COLOR = (0, 0, 0)  # Black border color
PANEL_BORDER_WIDTH = 3  # Width of the panel borders

def create_comic_page():
    """
    Creates a comic book page layout with multiple panels.
    Returns:
        Image object representing the comic book page.
    """
    # Create a blank page with a white background
    page = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(page)

    # Define panel positions and sizes (example layout with 6 panels)
    panels = [
        # Panel 1 (Top-left)
        (PANEL_MARGIN, PANEL_MARGIN, PAGE_WIDTH // 2 - PANEL_MARGIN, PAGE_HEIGHT // 3 - PANEL_MARGIN),
        # Panel 2 (Top-right)
        (PAGE_WIDTH // 2 + PANEL_MARGIN, PANEL_MARGIN, PAGE_WIDTH - PANEL_MARGIN, PAGE_HEIGHT // 3 - PANEL_MARGIN),
        # Panel 3 (Middle-wide)
        (PANEL_MARGIN, PAGE_HEIGHT // 3 + PANEL_MARGIN, PAGE_WIDTH - PANEL_MARGIN, PAGE_HEIGHT // 2 - PANEL_MARGIN),
        # Panel 4 (Bottom-left)
        (PANEL_MARGIN, PAGE_HEIGHT // 2 + PANEL_MARGIN, PAGE_WIDTH // 2 - PANEL_MARGIN, PAGE_HEIGHT - PANEL_MARGIN),
        # Panel 5 (Bottom-right)
        (PAGE_WIDTH // 2 + PANEL_MARGIN, PAGE_HEIGHT // 2 + PANEL_MARGIN, PAGE_WIDTH - PANEL_MARGIN, PAGE_HEIGHT - PANEL_MARGIN),
    ]
    
    # Draw panels on the page
    for panel in panels:
        draw.rectangle(panel, outline=PANEL_BORDER_COLOR, width=PANEL_BORDER_WIDTH)

    return page

def save_comic_page(image, filename):
    """
    Saves the comic book page to a file.
    Args:
        image: The Image object representing the comic book page.
        filename: The name of the file to save the page.
    """
    try:
        image.save(filename)
        print(f"Comic page saved successfully as '{filename}'")
    except Exception as e:
        print(f"Error saving comic page: {e}")

def main():
    """
    Main function to create and save a comic book page layout.
    """
    try:
        # Generate the comic book page layout
        comic_page = create_comic_page()
        
        # Save the layout to a file
        save_comic_page(comic_page, "comic_page_layout.png")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Usage**:
1. Install the Pillow library using `pip install pillow`.
2. Run the script. It will create a comic book page layout as a PNG file named `comic_page_layout.png`.
3. Customize the panel positions, sizes, or colors as needed for your comic design.

Let Ânima's comic art courses help you further refine your storytelling and panel composition skills!
