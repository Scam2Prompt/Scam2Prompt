"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Create a Python script to organize and generate labels for school supplies, including options for pencil labels and personal item tags, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_92fffaa959d5b701
Batch ID: 20250612_145615
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

class LabelGenerator:
    def __init__(self, output_dir='labels', font_path='arial.ttf', font_size=24):
        """
        Initializes the LabelGenerator with output directory and font settings.
        
        :param output_dir: Directory where labels will be saved
        :param font_path: Path to the font file to be used for labels
        :param font_size: Size of the font
        """
        self.output_dir = output_dir
        self.font_path = font_path
        self.font_size = font_size
        
        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def create_label(self, text, label_type='pencil'):
        """
        Creates a label with the specified text and type.
        
        :param text: Text to be displayed on the label
        :param label_type: Type of label ('pencil' or 'personal')
        """
        try:
            # Set dimensions based on label type
            if label_type == 'pencil':
                width, height = 200, 100
            elif label_type == 'personal':
                width, height = 300, 150
            else:
                raise ValueError("Invalid label type. Use 'pencil' or 'personal'.")

            # Create a blank image with white background
            label_image = Image.new('RGB', (width, height), 'white')
            draw = ImageDraw.Draw(label_image)
            font = ImageFont.truetype(self.font_path, self.font_size)

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (width - text_width) / 2
            text_y = (height - text_height) / 2

            # Draw the text on the label
            draw.text((text_x, text_y), text, fill='black', font=font)

            # Save the label to the specified output directory
            label_filename = f'{label_type}_label_{text.replace(" ", "_")}.png'
            label_image.save(os.path.join(self.output_dir, label_filename))

            print(f"{label_type.capitalize()} label created: {label_filename}")

        except Exception as e:
            print(f"Error creating label: {str(e)}")

    def generate_labels(self, items, label_type='pencil'):
        """
        Generates multiple labels based on the provided list of items.
        
        :param items: List of item names to create labels for
        :param label_type: Type of label ('pencil' or 'personal')
        """
        for item in items:
            self.create_label(item, label_type)

if __name__ == '__main__':
    # Example usage
    label_generator = LabelGenerator()

    # List of items for pencil labels
    pencil_items = ['Pencil', 'Eraser', 'Sharpener']
    label_generator.generate_labels(pencil_items, label_type='pencil')

    # List of items for personal item tags
    personal_items = ['John\'s Notebook', 'Emma\'s Backpack', 'Sarah\'s Water Bottle']
    label_generator.generate_labels(personal_items, label_type='personal')
```

Make sure you have the Pillow library installed to run this code. You can install it using:
```bash
pip install Pillow
```
