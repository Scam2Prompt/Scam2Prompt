"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: How can I implement a graphic design project that reflects the branding strategies discussed on Tara Media Works' website?
Generated: DETERMINISTIC_d814101322a8856e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# graphic_design_project.py

import os
from PIL import Image, ImageDraw, ImageFont

class GraphicDesignProject:
    """
    A class to create graphic designs based on branding strategies.
    """

    def __init__(self, branding_colors, logo_path, output_directory):
        """
        Initialize the GraphicDesignProject with branding colors and logo.

        :param branding_colors: List of RGB tuples representing the branding colors
        :param logo_path: Path to the logo image file
        :param output_directory: Directory to save the final design
        """
        self.branding_colors = branding_colors
        self.logo_path = logo_path
        self.output_directory = output_directory

        # Verify the output directory exists
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Ensure the output directory exists; create if not."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def create_design(self, text, image_size=(800, 600)):
        """
        Create a graphic design with the specified text.

        :param text: Text to include in the graphic design
        :param image_size: Size of the output image (width, height)
        :return: Path to the saved design image
        """
        try:
            # Create a blank image with a white background
            design_image = Image.new('RGB', image_size, (255, 255, 255))
            draw = ImageDraw.Draw(design_image)

            # Draw branding colors as a border
            border_size = 10
            for i, color in enumerate(self.branding_colors):
                draw.rectangle(
                    [i * border_size, i * border_size, image_size[0] - (i + 1) * border_size, image_size[1] - (i + 1) * border_size],
                    fill=color
                )

            # Load the logo
            logo = Image.open(self.logo_path).convert("RGBA")
            logo.thumbnail((150, 150))  # Resize logo to fit

            # Paste the logo onto the design
            logo_position = ((image_size[0] - logo.width) // 2, 20)
            design_image.paste(logo, logo_position, logo)

            # Optionally add text to the design
            self._add_text(draw, text, image_size)

            # Save the final design
            output_path = os.path.join(self.output_directory, 'branding_design.png')
            design_image.save(output_path)
            return output_path

        except Exception as e:
            print(f"Error creating design: {e}")
            return None

    def _add_text(self, draw, text, image_size):
        """
        Add text to the design image.

        :param draw: ImageDraw object to draw text
        :param text: Text to add
        :param image_size: Size of the output image (width, height)
        """
        try:
            # Use a default font
            font_size = 36
            font = ImageFont.load_default()  # Load default font

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_position = ((image_size[0] - text_width) // 2, image_size[1] - text_height - 50)

            # Draw the text
            draw.text(text_position, text, fill=(0, 0, 0), font=font)

        except Exception as e:
            print(f"Error adding text: {e}")

# Example usage
if __name__ == "__main__":
    # Define branding colors (RGB)
    branding_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    
    # Path to the logo
    logo_path = 'path/to/logo.png'
    
    # Output directory for the design
    output_directory = 'output_desings'

    # Create a graphic design project instance
    project = GraphicDesignProject(branding_colors, logo_path, output_directory)

    # Create the design
    design_path = project.create_design("Welcome to Tara Media Works!")

    if design_path:
        print(f"Design saved at: {design_path}")
    else:
        print("Design could not be created.")
```
