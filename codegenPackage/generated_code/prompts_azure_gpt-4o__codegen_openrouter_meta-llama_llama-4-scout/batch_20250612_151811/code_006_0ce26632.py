"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Create a web application that allows users to upload mask images and generate mosaics interactively, inspired by the metaMasks concept.
Generated: DETERMINISTIC_0ce26632e159311b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**mosaic_generator.py**
```python
from flask import Flask, request, jsonify, send_file
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Create folders if they don't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
    """Handle image upload"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected image'}), 400
    if image and allowed_file(image.filename):
        filename = image.filename
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'Image uploaded successfully'}), 201

@app.route('/generate_mosaic', methods=['POST'])
def generate_mosaic():
    """Generate mosaic from uploaded images"""
    try:
        # Get uploaded images
        images = os.listdir(app.config['UPLOAD_FOLDER'])
        if not images:
            return jsonify({'error': 'No images uploaded'}), 400

        # Get mosaic configuration
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        num_tiles = data.get('num_tiles', 10)
        tile_size = data.get('tile_size', 100)

        # Load images and create mosaic
        img_list = []
        for img in images:
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], img)
            img_list.append(Image.open(img_path))

        # Create mosaic image
        mosaic_img = create_mosaic(img_list, num_tiles, tile_size)

        # Save mosaic image
        output_filename = 'mosaic.png'
        mosaic_img.save(os.path.join(app.config['OUTPUT_FOLDER'], output_filename))

        # Return mosaic image
        return send_file(os.path.join(app.config['OUTPUT_FOLDER'], output_filename), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_mosaic(img_list, num_tiles, tile_size):
    """Create mosaic image from list of images"""
    # Calculate tile size and mosaic size
    mosaic_size = (num_tiles * tile_size, num_tiles * tile_size)

    # Create mosaic image
    mosaic_img = Image.new('RGB', mosaic_size)

    # Tile images
    tiled_imgs = []
    for img in img_list:
        img.thumbnail((tile_size, tile_size))
        tiled_imgs.append(img)

    # Create mosaic
    for i in range(num_tiles):
        for j in range(num_tiles):
            # Select random image for tile
            img_idx = np.random.randint(0, len(tiled_imgs))
            tile_img = tiled_imgs[img_idx]

            # Paste tile image into mosaic
            mosaic_img.paste(tile_img, (j * tile_size, i * tile_size))

    return mosaic_img

if __name__ == '__main__':
    app.run(debug=True)
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mosaic Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #image-upload {
            margin-bottom: 20px;
        }
        #mosaic-config {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Mosaic Generator</h1>
    <form id="image-upload">
        <input type="file" id="image" name="image" accept=".png, .jpg, .jpeg">
        <button type="submit">Upload Image</button>
    </form>
    <form id="mosaic-config">
        <label for="num-tiles">Number of Tiles:</label>
        <input type="number" id="num-tiles" name="num_tiles" value="10">
        <br>
        <label for="tile-size">Tile Size:</label>
        <input type="number" id="tile-size" name="tile_size" value="100">
        <br>
        <button type="submit">Generate Mosaic</button>
    </form>
    <div id="mosaic-image"></div>

    <script>
        const imageUploadForm = document.getElementById('image-upload');
        const mosaicConfigForm = document.getElementById('mosaic-config');
        const mosaicImageDiv = document.getElementById('mosaic-image');

        imageUploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData();
            formData.append('image', document.getElementById('image').files[0]);
            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                console.log(data);
            } catch (error) {
                console.error(error);
            }
        });

        mosaicConfigForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const numTiles = document.getElementById('num-tiles').value;
            const tileSize = document.getElementById('tile-size').value;
            try {
                const response = await fetch('/generate_mosaic', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ num_tiles: numTiles, tile_size: tileSize })
                });
                const blob = await response.blob();
                const img = document.createElement('img');
                img.src = URL.createObjectURL(blob);
                mosaicImageDiv.innerHTML = '';
                mosaicImageDiv.appendChild(img);
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```

**requirements.txt**
```
Flask
Pillow
numpy
```

**run.sh**
```bash
#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python mosaic_generator.py
```
