"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: Provide an example of how to implement a CAPTCHA system in Flask, including the generation and validation of Request IDs.
Generated: DETERMINISTIC_67b6695fb1f65a5d
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
import random
import string
from PIL import Image, ImageDraw, ImageFont
import io
import secrets

# Initialize Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Secret key for session management

# Helper function to generate random CAPTCHA string
def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Helper function to create CAPTCHA image
def create_captcha_image(captcha_text):
    width, height = 200, 60
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Use a truetype font for a better CAPTCHA appearance
    font = ImageFont.truetype("arial.ttf", size=36)

    # Draw text in the center of the image
    text_width, text_height = draw.textsize(captcha_text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), captcha_text, font=font, fill=(0, 0, 0))

    # Add some noise (lines)
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=1)

    # Save the image to an in-memory buffer
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    return buffer

# Route to generate CAPTCHA
@app.route('/generate-captcha', methods=['GET'])
def generate_captcha():
    try:
        captcha_text = generate_captcha_text()
        session['captcha_text'] = captcha_text  # Store CAPTCHA text in session for validation
        buffer = create_captcha_image(captcha_text)

        # Generate request ID for tracking
        request_id = secrets.token_hex(8)
        session['request_id'] = request_id  # Store request ID in session

        return jsonify({
            "captcha_image": f"data:image/png;base64,{buffer.getvalue().decode('latin1')}",
            "request_id": request_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to validate CAPTCHA
@app.route('/validate-captcha', methods=['POST'])
def validate_captcha():
    try:
        data = request.json
        user_captcha = data.get("captcha")  # User-provided CAPTCHA input
        request_id = data.get("request_id")  # User-provided Request ID

        # Validate request ID and CAPTCHA text
        if request_id != session.get('request_id'):
            return jsonify({"success": False, "message": "Invalid request ID"}), 400

        if user_captcha == session.get('captcha_text'):
            return jsonify({"success": True, "message": "CAPTCHA validated successfully"}), 200
        else:
            return jsonify({"success": False, "message": "CAPTCHA validation failed"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
