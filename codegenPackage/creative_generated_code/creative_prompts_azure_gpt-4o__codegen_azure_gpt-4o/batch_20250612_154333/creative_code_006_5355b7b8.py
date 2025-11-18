"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Provide an API recommendation for generating adhesive labels with options for text, color, and size customization, suitable for applications like those mentioned on Etiquettetout.com.
Generated: DETERMINISTIC_5355b7b841ea97f9
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Ensure a directory exists for storing temporary label images
LABELS_DIR = "label_images"
if not os.path.exists(LABELS_DIR):
    os.makedirs(LABELS_DIR)

@app.route('/generate_label', methods=['POST'])
def generate_label():
    """
    API endpoint to generate adhesive labels with customizable text,
    color, and size.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        text = data.get("text", "").strip()
        color = data.get("color", "#000000")  # Default is black
        width = int(data.get("width", 300))  # Default width: 300 pixels
        height = int(data.get("height", 100))  # Default height: 100 pixels
        
        # Validate input
        if not text:
            return jsonify({"error": "Text for label is required"}), 400
        if width <= 0 or height <= 0:
            return jsonify({"error": "Invalid dimensions for label"}), 400
        
        # Generate label image
        label_image = Image.new("RGB", (width, height), color)
        draw = ImageDraw.Draw(label_image)
        
        # Use default font (adjust path if custom font is needed)
        try:
            font = ImageFont.load_default()
        except:
            return jsonify({"error": "Failed to load font"}), 500

        # Center the text in the label
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2
        draw.text((text_x, text_y), text, fill="white", font=font)

        # Save the image to the labels directory
        label_filename = f"{LABELS_DIR}/label_{text.replace(' ', '_')}.png"
        label_image.save(label_filename)
        
        return jsonify({"message": "Label generated successfully", "label_url": label_filename}), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
