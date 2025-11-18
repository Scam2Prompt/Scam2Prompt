"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Develop a script for photo and graphic editing on a website, utilizing Fantom Internet Dienst's expertise in photo and video processing.
Generated: DETERMINISTIC_6e9c974a14dc36ab
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from PIL import Image, ImageFilter, ImageEnhance

app = Flask(__name__)

# Base path for uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload a file to the server."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': file.filename}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/edit/<filename>', methods=['POST'])
def edit_image(filename):
    """Edit the uploaded image by applying filters and enhancements."""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        # Open the image file
        with Image.open(file_path) as img:
            # Apply a Gaussian blur filter as an example
            img = img.filter(ImageFilter.GaussianBlur(5))
            
            # Enhance the image brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.5)  # Increase brightness by 50%
            
            # Save the edited image
            edited_file_path = os.path.join(UPLOAD_FOLDER, f'edited_{filename}')
            img.save(edited_file_path)
            
            return jsonify({'message': 'Image edited successfully', 'edited_filename': f'edited_{filename}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    """Delete the uploaded file."""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        os.remove(file_path)
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Requirements:
- Ensure you have Flask and Pillow installed. You can install them using:
```bash
pip install Flask Pillow
```

### Note:
- This script sets up a basic Flask server to handle file uploads, image editing (with a Gaussian blur and brightness enhancement), and deletions. Make sure to secure file uploads and handle file types appropriately in a production environment.
