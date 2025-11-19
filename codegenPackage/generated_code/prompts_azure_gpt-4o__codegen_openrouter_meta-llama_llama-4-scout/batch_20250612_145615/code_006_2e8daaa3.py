"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Implement a feature in a web app to generate labels for air and army cadets, ensuring durability and customization options similar to Labelmystuff.com.
Generated: DETERMINISTIC_2e8daaa3b14ca8e5
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Cadet Label Generator**
=========================

### **label_generator.py**
```python
import os
from PIL import Image, ImageDraw, ImageFont
from typing import Dict

class CadetLabelGenerator:
    def __init__(self, font_path: str, image_size: int = 300):
        """
        Initialize the label generator.

        Args:
        - font_path (str): Path to the font file.
        - image_size (int): Size of the label image (default: 300).
        """
        self.font_path = font_path
        self.image_size = image_size
        self.font = ImageFont.truetype(font_path, 24)

    def generate_label(self, cadet_info: Dict[str, str]) -> Image:
        """
        Generate a label image for a cadet.

        Args:
        - cadet_info (Dict[str, str]): Dictionary containing cadet information.
            Required keys:
                - name
                - rank
                - unit
                - affiliation (air or army)

        Returns:
        - Image: The generated label image.
        """
        # Create a new image with white background
        img = Image.new('RGB', (self.image_size, self.image_size), color = (73, 109, 137))
        d = ImageDraw.Draw(img)

        # Draw cadet information
        d.text((10, 10), f"Name: {cadet_info['name']}", font=self.font, fill=(255, 255, 0))
        d.text((10, 40), f"Rank: {cadet_info['rank']}", font=self.font, fill=(255, 255, 0))
        d.text((10, 70), f"Unit: {cadet_info['unit']}", font=self.font, fill=(255, 255, 0))

        # Add affiliation logo
        if cadet_info['affiliation'] == 'air':
            logo_path = 'air_cadet_logo.png'
        elif cadet_info['affiliation'] == 'army':
            logo_path = 'army_cadet_logo.png'
        else:
            raise ValueError("Invalid affiliation")

        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
            img.paste(logo, (self.image_size - 50, 10))

        return img

    def save_label(self, img: Image, filename: str) -> None:
        """
        Save the label image to a file.

        Args:
        - img (Image): The label image to save.
        - filename (str): The filename to save the image as.
        """
        img.save(filename, 'PNG')

def main():
    font_path = 'arial.ttf'
    generator = CadetLabelGenerator(font_path)

    cadet_info = {
        'name': 'John Doe',
        'rank': 'Cadet',
        'unit': '123 Squadron',
        'affiliation': 'air'
    }

    label_img = generator.generate_label(cadet_info)
    generator.save_label(label_img, 'label.png')

if __name__ == "__main__":
    main()
```

### **app.py (Flask App)**
```python
from flask import Flask, request, send_file
from label_generator import CadetLabelGenerator
import os

app = Flask(__name__)

# Initialize the label generator
font_path = 'arial.ttf'
generator = CadetLabelGenerator(font_path)

@app.route('/generate_label', methods=['POST'])
def generate_label():
    try:
        cadet_info = request.get_json()
        label_img = generator.generate_label(cadet_info)
        filename = 'label.png'
        generator.save_label(label_img, filename)
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### **requirements.txt**
```
Flask
Pillow
```

### **Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```
