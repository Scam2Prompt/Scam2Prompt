"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acesainter.com
Prompt: Suggest tools or APIs to design and preview personalized food packaging for restaurants, similar to the customization services offered by ACESA INTERABASTO SA DE CV.
Generated: DETERMINISTIC_3bce71918db093bd
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import os

# Initialize Flask application
app = Flask(__name__)

# Directory to store preview images
OUTPUT_DIR = "previews"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Error messages
ERROR_MESSAGES = {
    "missing_params": "Required parameters missing: {missing}",
    "image_creation_failed": "Failed to create preview image.",
}

# Function to validate input parameters for packaging preview
def validate_params(params, required_params):
    """
    Validate input parameters for API requests.
    :param params: dict of parameters supplied by the user
    :param required_params: list of required parameter names
    :return: Tuple (bool, list) - IsValid, MissingParams
    """
    missing = [param for param in required_params if param not in params or not params[param]]
    return len(missing) == 0, missing

# Endpoint to generate a food packaging preview
@app.route('/generate_preview', methods=['POST'])
def generate_preview():
    """
    Endpoint for generating personalized food packaging previews.
    Expected parameters:
    - width: Width of the packaging in pixels
    - height: Height of the packaging in pixels
    - text: Text to display on the packaging
    - font_size: Font size for the displayed text
    - font_color: Color of the text (e.g., "#FFFFFF")
    - background_color: Background color of the packaging (e.g., "#000000")
    :return: JSON response with the preview URL or error message
    """
    try:
        # Parse and validate input
        data = request.json
        required_params = ['width', 'height', 'text', 'font_size', 'font_color', 'background_color']
        is_valid, missing_params = validate_params(data, required_params)

        if not is_valid:
            return jsonify({"error": ERROR_MESSAGES["missing_params"].format(missing=", ".join(missing_params))}), 400

        # Convert dimensions and colors to proper types
        width = int(data['width'])
        height = int(data['height'])
        text = data['text']
        font_size = int(data['font_size'])
        font_color = data['font_color']
        background_color = data['background_color']

        # Create a new image for the packaging
        image = Image.new("RGB", (width, height), color=background_color)
        draw = ImageDraw.Draw(image)

        # Use default font; adjust font as needed for production
        font = ImageFont.load_default()
        try:
            # Optional: use a TrueType font if available
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            pass  # Fallback to default font if specified font is unavailable

        # Calculate text position to center it
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill=font_color, font=font)

        # Save the preview image
        preview_filename = f"preview_{text.replace(' ', '_')}.png"
        preview_path = os.path.join(OUTPUT_DIR, preview_filename)
        image.save(preview_path)

        # Return the URL of the generated preview image
        preview_url = request.host_url.rstrip('/') + f"/previews/{preview_filename}"
        return jsonify({"preview_url": preview_url}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": ERROR_MESSAGES["image_creation_failed"], "details": str(e)}), 500

# Endpoint to serve preview images
@app.route('/previews/<filename>', methods=['GET'])
def serve_preview(filename):
    """
    Endpoint for serving preview images.
    :param filename: Name of the preview image file
    :return: File response or error message
    """
    try:
        file_path = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(file_path):
            return app.send_static_file(file_path)
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to serve preview image", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
