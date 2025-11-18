"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Create a web application that allows users to upload mask images and generate mosaics interactively, inspired by the metaMasks concept.
Generated: DETERMINISTIC_0ce26632e159311b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw
import numpy as np

# Initialize Flask Application
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
MOSAIC_FOLDER = 'mosaics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MOSAIC_FOLDER'] = MOSAIC_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MOSAIC_FOLDER, exist_ok=True)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Home Page
@app.route('/')
def index():
    # Render HTML template for uploading mask images and interactive mosaic generation
    return render_template('index.html')

# Route: Upload Mask Image
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    
    return jsonify({'error': 'File type not supported'}), 400

# Route: Generate Mosaic
@app.route('/generate_mosaic', methods=['POST'])
def generate_mosaic():
    data = request.json
    mask_filename = data.get('mask_filename')
    if not mask_filename:
        return jsonify({'error': 'Mask filename is required'}), 400
    
    mask_path = os.path.join(app.config['UPLOAD_FOLDER'], mask_filename)
    if not os.path.exists(mask_path):
        return jsonify({'error': 'Mask file not found'}), 404

    try:
        # Load mask image and generate mosaic
        mask_image = Image.open(mask_path).convert('L')  # Convert to grayscale
        mask_array = np.array(mask_image)

        # Create mosaic based on mask shape
        mosaic_size = 10  # Size of mosaic blocks
        mosaic_image = Image.new('RGB', mask_image.size, (255, 255, 255))
        draw = ImageDraw.Draw(mosaic_image)

        for y in range(0, mask_image.height, mosaic_size):
            for x in range(0, mask_image.width, mosaic_size):
                # Compute average color of the mask in the current block
                block = mask_array[y:y + mosaic_size, x:x + mosaic_size]
                avg_intensity = np.mean(block) if block.size > 0 else 255
                color = (int(avg_intensity), int(avg_intensity), int(avg_intensity))

                # Draw block
                draw.rectangle(
                    [x, y, x + mosaic_size, y + mosaic_size],
                    fill=color
                )

        # Save mosaic to file
        mosaic_filename = f'mosaic_{mask_filename}'
        mosaic_path = os.path.join(app.config['MOSAIC_FOLDER'], mosaic_filename)
        mosaic_image.save(mosaic_path)

        return jsonify({'message': 'Mosaic generated successfully', 'mosaic_filename': mosaic_filename}), 200

    except Exception as e:
        return jsonify({'error': 'Error generating mosaic', 'details': str(e)}), 500

# Route: Serve Mosaic Images
@app.route('/mosaics/<filename>')
def serve_mosaic(filename):
    mosaic_path = os.path.join(app.config['MOSAIC_FOLDER'], filename)
    if os.path.exists(mosaic_path):
        return app.send_static_file(mosaic_path)
    return jsonify({'error': 'Mosaic file not found'}), 404

# Main Entry Point
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (`templates/index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mosaic Generator</title>
</head>
<body>
    <h1>Mosaic Generator</h1>
    <form id="upload-form" method="POST" enctype="multipart/form-data" action="/upload">
        <label for="file">Upload Mask Image:</label>
        <input type="file" id="file" name="file" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
    <h2>Generate Mosaic</h2>
    <input type="text" id="mask-filename" placeholder="Enter uploaded mask filename">
    <button id="generate-button">Generate Mosaic</button>
    <div id="result"></div>
</body>
<script>
    document.getElementById('generate-button').addEventListener('click', async function() {
        const maskFilename = document.getElementById('mask-filename').value.trim();
        if (!maskFilename) {
            alert('Please enter a mask filename.');
            return;
        }
        const response = await fetch('/generate_mosaic', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mask_filename: maskFilename })
        });
        const result = await response.json();
        if (result.mosaic_filename) {
            const imgElement = document.createElement('img');
            imgElement.src = `/mosaics/${result.mosaic_filename}`;
            document.getElementById('result').innerHTML = '';
            document.getElementById('result').appendChild(imgElement);
        } else {
            alert(result.error || 'Failed to generate mosaic.');
        }
    });
</script>
</html>
```
