"""
Generated Code Metadata:
========================
Original URL: https://marqador.com
Prompt: Generate a code snippet for an online store that allows users to create custom stamps with QR codes for important information, as described on marQadoR.
Generated: DETERMINISTIC_2596235faf5858bd
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import qrcode
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, send_file
from io import BytesIO
import os

# Initialize Flask app
app = Flask(__name__)

# Define function to generate QR code
def generate_qr_code(data):
    """
    Generate a QR code from the provided data.

    Args:
        data (str): The data to encode in the QR code.

    Returns:
        PIL.Image: The generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Define function to generate custom stamp
def generate_custom_stamp(text, qr_code_data, background_color="#FFFFFF", text_color="#000000", font_size=24):
    """
    Generate a custom stamp with a QR code.

    Args:
        text (str): The text to display on the stamp.
        qr_code_data (str): The data to encode in the QR code.
        background_color (str): The background color of the stamp (default: #FFFFFF).
        text_color (str): The text color of the stamp (default: #000000).
        font_size (int): The font size of the text (default: 24).

    Returns:
        PIL.Image: The generated custom stamp image.
    """
    # Generate QR code
    qr_code_img = generate_qr_code(qr_code_data)
    qr_code_img = qr_code_img.resize((150, 150))

    # Create stamp image
    stamp_img = Image.new("RGB", (300, 300), color=background_color)
    draw = ImageDraw.Draw(stamp_img)

    # Add QR code to stamp
    stamp_img.paste(qr_code_img, (75, 75))

    # Add text to stamp
    font = ImageFont.truetype("arial.ttf", font_size)
    text_lines = text.splitlines()
    for i, line in enumerate(text_lines):
        draw.text((50, 250 - (i * font_size)), line, fill=text_color, font=font)

    return stamp_img

# Define route for generating custom stamp
@app.route("/generate_stamp", methods=["POST"])
def generate_stamp():
    try:
        data = request.json
        if not data:
            return {"error": "No data provided"}, 400

        text = data.get("text")
        qr_code_data = data.get("qr_code_data")

        if not text or not qr_code_data:
            return {"error": "Text and QR code data are required"}, 400

        stamp_img = generate_custom_stamp(text, qr_code_data)
        img_io = BytesIO()
        stamp_img.save(img_io, "PNG", quality=90)
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png")
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```
