"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdixchange.com
Prompt: Provide an example of how to use the ID card photolook PSD files from fdixchange.com in a graphic design project.
Generated: DETERMINISTIC_9027dc0c7850184f
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image

class IDCardDesigner:
    """
    A class to handle the creation of ID cards using PSD templates.
    Utilizes the Pillow library for image manipulation.
    """

    def __init__(self, template_path):
        """
        Initializes the IDCardDesigner with the path to the PSD template.

        Args:
            template_path (str): The file path to the PSD template.
        """
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template file not found: {template_path}")
        
        self.template_path = template_path

    def load_template(self):
        """
        Loads the PSD template for editing.
        
        Returns:
            Image: Loaded PSD image as a PIL Image object.
        """
        try:
            # Load PSD file using Pillow
            template_image = Image.open(self.template_path)
            return template_image
        except Exception as e:
            raise RuntimeError(f"Failed to load template: {str(e)}")

    def add_photo(self, image_path, position, size):
        """
        Adds a photo to the ID card at a specified position and size.

        Args:
            image_path (str): The file path to the photo image.
            position (tuple): The (x, y) position to place the photo on the ID card.
            size (tuple): The (width, height) size to resize the photo to.

        Returns:
            Image: The ID card image with the photo added.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Photo file not found: {image_path}")

        try:
            # Load the photo to be added
            photo_image = Image.open(image_path).resize(size)
            id_card = self.load_template()
            id_card.paste(photo_image, position)
            return id_card
        except Exception as e:
            raise RuntimeError(f"Failed to add photo: {str(e)}")

    def save_id_card(self, id_card_image, output_path):
        """
        Saves the final ID card image to the specified output path.

        Args:
            id_card_image (Image): The final ID card image to save.
            output_path (str): The file path to save the image.
        """
        try:
            id_card_image.save(output_path)
            print(f"ID card saved successfully at: {output_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to save ID card: {str(e)}")

# Example usage of IDCardDesigner
if __name__ == "__main__":
    try:
        designer = IDCardDesigner("path/to/template.psd")
        id_card_with_photo = designer.add_photo("path/to/photo.jpg", (50, 50), (100, 100))
        designer.save_id_card(id_card_with_photo, "path/to/output_id_card.png")
    except Exception as e:
        print(f"Error: {e}")
```

**Note:** Ensure you have Pillow installed. You can install it via pip:

```bash
pip install Pillow
```
