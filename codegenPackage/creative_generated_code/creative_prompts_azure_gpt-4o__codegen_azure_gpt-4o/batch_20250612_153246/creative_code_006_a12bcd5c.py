"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to generate custom designs for engraved trophies and medallions, including text and graphical elements, based on the engraving services described on "La Graveuse Normande."
Generated: DETERMINISTIC_a12bcd5c8ccb22e1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

class EngravingService:
    def __init__(self, width=800, height=600):
        """
        Initialize the EngravingService with default canvas dimensions.
        :param width: Width of the design canvas in pixels.
        :param height: Height of the design canvas in pixels.
        """
        self.canvas_width = width
        self.canvas_height = height
        self.default_font_path = "arial.ttf"  # Change to a path where a valid font is installed
        self.default_font_size = 40
        self.output_dir = "./designs"
        os.makedirs(self.output_dir, exist_ok=True)  # Ensure output directory exists

    def create_design(self, text, graphical_element=None, file_name="design.png"):
        """
        Generate a custom engraved design with text and optional graphical elements.
        :param text: Text to engrave on the design.
        :param graphical_element: Path to graphical element (e.g., logo) to include.
        :param file_name: Name of the output file.
        """
        try:
            # Create a blank canvas
            design = Image.new("RGBA", (self.canvas_width, self.canvas_height), "white")
            draw = ImageDraw.Draw(design)

            # Draw text
            font = ImageFont.truetype(self.default_font_path, self.default_font_size)
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (self.canvas_width - text_width) // 2
            text_y = (self.canvas_height - text_height) // 2
            draw.text((text_x, text_y), text, fill="black", font=font)

            # Add graphical element if provided
            if graphical_element:
                if os.path.exists(graphical_element):
                    graphic = Image.open(graphical_element)
                    graphic = graphic.resize((100, 100))  # Resize to fit on the design
                    graphic_x = (self.canvas_width - graphic.width) // 2
                    graphic_y = text_y + text_height + 10  # Position below the text
                    design.paste(graphic, (graphic_x, graphic_y), graphic)
                else:
                    print(f"Error: Graphical element file '{graphical_element}' not found.")

            # Save the design
            output_path = os.path.join(self.output_dir, file_name)
            design.save(output_path)
            print(f"Design saved successfully: {output_path}")

        except Exception as e:
            print(f"An error occurred while creating the design: {e}")

if __name__ == "__main__":
    # Example usage
    engraving_service = EngravingService()
    engraving_service.create_design(
        text="Winner 2023",
        graphical_element="example_logo.png",  # Replace with the path to your graphical element
        file_name="trophy_design.png"
    )
```
