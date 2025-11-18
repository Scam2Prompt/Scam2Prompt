"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Suggest an API or library to automate the creation of branded merchandise, such as "Pita Sablon" and "Custom Bags," with options for material and design customization.
Generated: DETERMINISTIC_e471678ba0cc05fc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont

# Initialize Flask application
app = Flask(__name__)

# Endpoint: Generate branded merchandise preview
@app.route('/generate-merch-preview', methods=['POST'])
def generate_merch_preview():
    """
    Generate a branded merchandise preview based on user input.
    Accepts JSON payload with design details.
    Returns a preview image as base64.
    """
    try:
        # Parse request data
        data = request.get_json()
        product_type = data.get('product_type', 'Custom Bag')  # Default product type
        material = data.get('material', 'Cotton')  # Default material
        design_text = data.get('design_text', 'Your Design Here')  # Default design text
        font_size = data.get('font_size', 40)  # Default font size

        # Validate input
        if not design_text:
            return jsonify({"error": "Design text is required"}), 400

        # Create a blank product canvas
        canvas_width, canvas_height = 500, 500
        canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
        draw = ImageDraw.Draw(canvas)

        # Load font (using a default font for simplicity)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            # Fallback to default PIL font if specified font not found
            font = ImageFont.load_default()

        # Add design text to the canvas
        text_width, text_height = draw.textsize(design_text, font=font)
        text_x = (canvas_width - text_width) // 2
        text_y = (canvas_height - text_height) // 2
        draw.text((text_x, text_y), design_text, fill="black", font=font)

        # Save the canvas as a preview image
        preview_path = f"{product_type}_preview.png"
        canvas.save(preview_path)

        return jsonify({
            "message": "Merchandise preview generated successfully",
            "preview_path": preview_path,
            "product_type": product_type,
            "material": material
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Endpoint: List available product types and materials
@app.route('/available-options', methods=['GET'])
def available_options():
    """
    Returns the available product types and materials for customization.
    """
    try:
        options = {
            "product_types": ["Pita Sablon", "Custom Bags", "T-Shirts", "Mugs"],
            "materials": ["Cotton", "Polyester", "Paper", "Plastic"]
        }
        return jsonify(options), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
