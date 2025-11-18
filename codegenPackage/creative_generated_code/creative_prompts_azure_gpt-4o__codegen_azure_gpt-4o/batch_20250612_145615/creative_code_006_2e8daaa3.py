"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Implement a feature in a web app to generate labels for air and army cadets, ensuring durability and customization options similar to Labelmystuff.com.
Generated: DETERMINISTIC_2e8daaa3b14ca8e5
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Directory to save generated labels
LABELS_DIR = "generated_labels"
os.makedirs(LABELS_DIR, exist_ok=True)

# Default font and size
DEFAULT_FONT_PATH = "arial.ttf"  # Make sure this font exists on the server
DEFAULT_FONT_SIZE = 24

@app.route('/generate_label', methods=['POST'])
def generate_label():
    """
    API endpoint to generate a custom label for air and army cadets.
    Expects a JSON payload with 'name', 'rank', and 'options'.
    """
    try:
        # Parse input JSON
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input: JSON payload is required"}), 400

        # Extract label details
        name = data.get("name")
        rank = data.get("rank")
        options = data.get("options", {})  # Customization options (e.g., color, size)

        if not name or not rank:
            return jsonify({"error": "Both 'name' and 'rank' are required"}), 400

        # Set customization options
        background_color = options.get("background_color", "white")
        text_color = options.get("text_color", "black")
        font_size = options.get("font_size", DEFAULT_FONT_SIZE)
        label_width = options.get("width", 300)  # Default width
        label_height = options.get("height", 100)  # Default height

        # Create label image
        label_image = Image.new('RGB', (label_width, label_height), color=background_color)
        draw = ImageDraw.Draw(label_image)

        # Load font
        try:
            font = ImageFont.truetype(DEFAULT_FONT_PATH, font_size)
        except IOError:
            return jsonify({"error": f"Font file '{DEFAULT_FONT_PATH}' not found"}), 500

        # Prepare text (name and rank)
        text = f"{name} ({rank})"

        # Calculate text position for centering
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (label_width - text_width) // 2
        text_y = (label_height - text_height) // 2

        # Draw the text on the label
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the generated label
        label_filename = f"{name.lower().replace(' ', '_')}_{rank.lower().replace(' ', '_')}.png"
        label_path = os.path.join(LABELS_DIR, label_filename)
        label_image.save(label_path)

        return jsonify({
            "message": "Label generated successfully",
            "label_url": f"/labels/{label_filename}"
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/labels/<filename>', methods=['GET'])
def serve_label(filename):
    """
    Serve the generated label image file.
    """
    try:
        return app.send_static_file(os.path.join(LABELS_DIR, filename))
    except Exception as e:
        return jsonify({"error": f"Could not retrieve label: {str(e)}"}), 404


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
