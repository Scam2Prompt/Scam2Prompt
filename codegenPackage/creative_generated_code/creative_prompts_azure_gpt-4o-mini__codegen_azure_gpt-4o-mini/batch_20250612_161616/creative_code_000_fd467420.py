"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotocheckexpress.com
Prompt: Generate code to create a custom photo ID badge design that aligns with corporate branding, similar to the services offered by Fotocheck Express.
Generated: DETERMINISTIC_fd4674205f2553b2
Batch ID: 20250612_161616
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

class BadgeDesigner:
    def __init__(self, template_path, output_dir):
        """
        Initialize the BadgeDesigner with a template and output directory.
        
        :param template_path: Path to the badge template image.
        :param output_dir: Directory where generated badges will be saved.
        """
        self.template_path = template_path
        self.output_dir = output_dir
        
        # Load the template image
        self.template = self.load_image(template_path)
        
    def load_image(self, path):
        """
        Load an image from the given path.
        
        :param path: Path to the image file.
        :return: PIL Image object.
        """
        try:
            image = Image.open(path)
            return image
        except Exception as e:
            print(f"Error loading image from {path}: {e}")
            raise
            
    def create_badge(self, name, title, photo_path, badge_id):
        """
        Create a badge with the given details.
        
        :param name: Name of the badge holder.
        :param title: Job title of the badge holder.
        :param photo_path: Path to the badge holder's photo.
        :param badge_id: Unique ID for the badge.
        :return: Path to the generated badge image.
        """
        badge = self.template.copy()
        
        try:
            # Load the photo
            photo = self.load_image(photo_path)
            # Resize and paste photo on the badge
            photo = photo.resize((100, 100))  # Resize to fit the badge
            badge.paste(photo, (20, 20))  # Position photo
            
            # Prepare to draw text on the badge
            draw = ImageDraw.Draw(badge)
            font = ImageFont.load_default()

            # Add name, title, and ID to the badge
            draw.text((140, 20), name, fill="black", font=font)
            draw.text((140, 60), title, fill="black", font=font)
            draw.text((140, 100), f"ID: {badge_id}", fill="black", font=font)

            # Save the badge
            badge_path = os.path.join(self.output_dir, f"{badge_id}_badge.png")
            badge.save(badge_path)
            print(f"Badge saved to {badge_path}")
            return badge_path
            
        except Exception as e:
            print(f"Error creating badge: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    template_path = "badge_template.png"  # Path to your template
    output_dir = "badges"  # Directory to save badges

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Initialize BadgeDesigner
    badge_designer = BadgeDesigner(template_path, output_dir)

    # Create a badge
    badge_designer.create_badge(
        name="John Doe",
        title="Software Engineer",
        photo_path="john_doe_photo.jpg",  # Path to the photo
        badge_id="12345"
    )
```

Make sure to have the Python Imaging Library (PIL) installed in your environment. You can install it via pip:

```bash
pip install Pillow
```

Ensure that you replace `"badge_template.png"` and `"john_doe_photo.jpg"` with the actual paths to your badge template and photo respectively.
