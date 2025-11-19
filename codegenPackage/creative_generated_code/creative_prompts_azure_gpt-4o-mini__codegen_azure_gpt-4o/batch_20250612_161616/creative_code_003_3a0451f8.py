"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotocheckexpress.com
Prompt: Create a function that allows users to upload their logo and generate a professional-quality ID badge, reflecting the high standards of Fotocheck Express.
Generated: DETERMINISTIC_3a0451f87f6df3ab
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
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
ID_BADGE_FOLDER = 'badges'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ID_BADGE_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_id_badge(logo_path, user_name, user_title):
    """
    Create an ID badge with the uploaded logo, user name, and title.

    Args:
        logo_path (str): Path to the uploaded logo image.
        user_name (str): Name of the user.
        user_title (str): Title/Role of the user.

    Returns:
        str: Path to the generated ID badge.
    """
    try:
        # Badge dimensions and setup
        badge_width, badge_height = 400, 200
        badge = Image.new('RGB', (badge_width, badge_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(badge)

        # Font settings
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_name = ImageFont.truetype("arial.ttf", 25)

        # Insert logo
        logo = Image.open(logo_path).convert("RGBA")
        logo.thumbnail((80, 80))  # Resize logo to fit
        badge.paste(logo, (20, 60), logo)

        # Add user name and title
        draw.text((120, 60), f"Name: {user_name}", fill="black", font=font_name)
        draw.text((120, 100), f"Title: {user_title}", fill="black", font=font_title)

        # Save badge
        badge_path = os.path.join(ID_BADGE_FOLDER, f"{user_name}_badge.png")
        badge.save(badge_path)

        return badge_path
    except Exception as e:
        raise RuntimeError(f"Error generating ID badge: {e}")

@app.route('/upload_logo', methods=['POST'])
def upload_logo():
    """
    Endpoint to upload a logo and generate an ID badge.

    Expected form data:
        - logo: File upload of the user logo.
        - name: User's name.
        - title: User's title/role.
    """
    try:
        # Ensure required data is present
        if 'logo' not in request.files or 'name' not in request.form or 'title' not in request.form:
            return jsonify({"error": "Missing required fields: logo, name, or title"}), 400
        
        logo = request.files['logo']
        user_name = request.form['name']
        user_title = request.form['title']

        # Validate uploaded file
        if logo.filename == '':
            return jsonify({"error": "No file selected"}), 400
        if not logo.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({"error": "Invalid file type. Please upload a PNG or JPG image"}), 400

        # Save uploaded logo
        logo_path = os.path.join(app.config['UPLOAD_FOLDER'], logo.filename)
        logo.save(logo_path)

        # Generate ID badge
        badge_path = create_id_badge(logo_path, user_name, user_title)

        return jsonify({"message": "ID badge created successfully", "badge_path": badge_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
