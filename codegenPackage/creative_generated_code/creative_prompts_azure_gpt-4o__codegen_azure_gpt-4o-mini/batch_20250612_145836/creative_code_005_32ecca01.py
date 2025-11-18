"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Create a Python script to generate edible printing product labels dynamically based on customer input, such as name and design preferences.
Generated: DETERMINISTIC_32ecca019468008a
Batch ID: 20250612_145836
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
import textwrap

class LabelGenerator:
    def __init__(self, width=800, height=400, background_color=(255, 255, 255)):
        """
        Initialize the label generator with the given dimensions and background color.

        :param width: Width of the label in pixels
        :param height: Height of the label in pixels
        :param background_color: Background color of the label in RGB tuple
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.font_path = self.get_default_font()
        self.font_size = 30
        self.font = ImageFont.truetype(self.font_path, self.font_size)

    def get_default_font(self):
        """
        Get the default font path. Adjust based on the environment.

        :return: Path to a TrueType font file
        """
        return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust for Windows or macOS as necessary

    def create_label(self, customer_name, design_pref):
        """
        Create a label with the customer's name and design preference.

        :param customer_name: Name of the customer to display on the label
        :param design_pref: Design preferences (e.g., color, graphics)
        :return: Path to the created label image
        """
        try:
            # Create a new blank image
            label_image = Image.new("RGB", (self.width, self.height), self.background_color)
            draw = ImageDraw.Draw(label_image)

            # Prepare text
            wrapped_text = textwrap.fill(customer_name, width=20)  # Wrap text if too long
            text_size = draw.textsize(wrapped_text, font=self.font)
            text_x = (self.width - text_size[0]) / 2
            text_y = (self.height - text_size[1]) / 2

            # Draw the text on the label
            draw.text((text_x, text_y), wrapped_text, fill="black", font=self.font)

            # Apply design preferences (placeholder for future designs)
            if design_pref.lower() == 'fancy':
                self._add_fancy_design(draw)
            elif design_pref.lower() == 'simple':
                self._add_simple_design(draw)

            # Save the image to a file
            label_path = f"label_{customer_name.replace(' ', '_')}.png"
            label_image.save(label_path)
            return label_path

        except Exception as e:
            print(f"Error creating label: {e}")
            return None

    def _add_fancy_design(self, draw):
        """Add a fancy design to the label (placeholder for custom graphics)."""
        draw.rectangle([0, 0, self.width, self.height], outline="purple", width=5)

    def _add_simple_design(self, draw):
        """Add a simple design to the label (placeholder for custom graphics)."""
        draw.line([(0, 0), (self.width, self.height)], fill="blue", width=5)
        draw.line([(0, self.height), (self.width, 0)], fill="blue", width=5)

def main():
    """
    Main function to execute the label generator.
    Prompts user for input and generates a label based on their preferences.
    """
    customer_name = input("Enter the customer's name: ")
    design_pref = input("Enter design preference (fancy/simple): ")

    label_generator = LabelGenerator()
    label_path = label_generator.create_label(customer_name, design_pref)

    if label_path:
        print(f"Label created successfully: {label_path}")
    else:
        print("Failed to create the label.")

if __name__ == "__main__":
    main()
```
