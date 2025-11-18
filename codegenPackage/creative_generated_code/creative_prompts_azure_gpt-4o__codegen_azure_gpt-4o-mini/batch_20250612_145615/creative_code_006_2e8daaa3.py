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
from flask_sqlalchemy import SQLAlchemy
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadet_labels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing label information
class CadetLabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<CadetLabel {self.name} - {self.unit}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to generate and save label images
@app.route('/generate_label', methods=['POST'])
def generate_label():
    try:
        # Retrieve data from the request
        data = request.json
        name = data['name']
        unit = data['unit']
        rank = data['rank']
        color = data['color']

        # Validate input data
        if not all([name, unit, rank, color]):
            return jsonify({"error": "All fields are required"}), 400

        # Create an image for the label
        label_image = create_label_image(name, unit, rank, color)

        # Save label information to the database
        new_label = CadetLabel(name=name, unit=unit, rank=rank, color=color)
        db.session.add(new_label)
        db.session.commit()

        # Save image to file
        image_path = f'static/labels/{new_label.id}.png'
        label_image.save(image_path)

        return jsonify({"message": "Label generated successfully", "image_path": image_path}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to create a label image
def create_label_image(name, unit, rank, color):
    # Define dimensions and create a blank image
    width, height = 400, 200
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Draw the text on the image
    draw.text((10, 10), f"Name: {name}", fill=color, font=font)
    draw.text((10, 50), f"Unit: {unit}", fill=color, font=font)
    draw.text((10, 90), f"Rank: {rank}", fill=color, font=font)

    return image

# Main entry point for the Flask web application
if __name__ == '__main__':
    # Ensure the static directory exists
    os.makedirs('static/labels', exist_ok=True)
    app.run(debug=True)
```

### Note:
- Ensure that the `Pillow` library is installed (`pip install Pillow`) to handle image creation.
- The `Flask` library should also be installed (`pip install Flask`).
- This code assumes you have a valid `arial.ttf` font file in your environment or that you will use the default font.
- For production, consider using a robust database system and handling user inputs more securely to prevent injection attacks.
