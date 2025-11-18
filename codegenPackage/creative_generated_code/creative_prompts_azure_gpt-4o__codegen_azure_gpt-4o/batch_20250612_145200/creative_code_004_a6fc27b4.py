"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jerrybeers.com
Prompt: Suggest a Python library for creating a photo gallery web page that organizes images by travel destinations, inspired by the photography shared on JerryBeers.com.
Generated: DETERMINISTIC_a6fc27b4cd5049c2
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import os

# Define constants
IMAGE_FOLDER = 'static/images'  # Folder to store images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed image formats

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# Helper function to check allowed file extensions
def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to render the homepage
@app.route('/')
def home():
    """
    Main route to load the photo gallery.
    Images are organized into travel destinations.
    """
    destinations = {}  # Dictionary to map destinations to their images
    
    # Traverse the image folder to group images by destination
    for folder in os.listdir(app.config['UPLOAD_FOLDER']):
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder)
        if os.path.isdir(folder_path):  # Check if it's a folder representing a destination
            destinations[folder] = [
                os.path.join(folder, file)
                for file in os.listdir(folder_path)
                if allowed_file(file)
            ]
    
    # Render the HTML template and pass the destinations data
    return render_template('gallery.html', destinations=destinations)

# Route to upload new images
@app.route('/upload', methods=['POST'])
def upload_image():
    """
    Endpoint to handle image uploads.
    Expects a form field 'destination' and a file 'image'.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['image']
    destination = request.form.get('destination', '').strip()
    
    if not file or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format'}), 400
    if not destination:
        return jsonify({'error': 'Destination is required'}), 400
    
    # Create destination folder if it doesn't exist
    destination_path = os.path.join(app.config['UPLOAD_FOLDER'], destination)
    os.makedirs(destination_path, exist_ok=True)
    
    # Save the uploaded file
    file_path = os.path.join(destination_path, file.filename)
    file.save(file_path)
    
    return jsonify({'success': 'Image uploaded successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    # Ensure the image folder exists
    os.makedirs(IMAGE_FOLDER, exist_ok=True)
    app.run(debug=True)
```

**Note**: This code assumes the existence of a `gallery.html` template for rendering the gallery UI. You would need to create proper HTML/CSS for displaying the images in a user-friendly photo gallery format.
