"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: Generate code for a feature that allows users to upload photos of their vehicle for trade-in purposes, inspired by the Cid Autos "Recibimos tu Vehículo" functionality.
Generated: DETERMINISTIC_b8f1b67f2e037bb5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import uuid

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads/vehicles'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def validate_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False

@app.route('/')
def index():
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_vehicle_photo():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    # Generate unique filename
    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        file.save(save_path)
        
        # Validate the image is not corrupted
        if not validate_image(save_path):
            os.remove(save_path)
            return jsonify({'error': 'Invalid image file'}), 400
        
        # Process additional form data if needed
        vehicle_data = {
            'make': request.form.get('make'),
            'model': request.form.get('model'),
            'year': request.form.get('year'),
            'mileage': request.form.get('mileage')
        }
        
        # Here you would typically save to database or process further
        # For demo, we just return the filename and form data
        
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'vehicle_data': vehicle_data
        }), 200
        
    except Exception as e:
        if os.path.exists(save_path):
            os.remove(save_path)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/upload_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle Trade-In Photo Upload</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #preview {
            max-width: 100%;
            margin-top: 10px;
            display: none;
        }
        #status {
            margin-top: 15px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        .success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        .error {
            background-color: #f2dede;
            color: #a94442;
        }
    </style>
</head>
<body>
    <h1>Vehicle Trade-In Photo Upload</h1>
    <form id="uploadForm" enctype="multipart/form-data">
        <div class="form-group">
            <label for="make">Vehicle Make:</label>
            <input type="text" id="make" name="make" required>
        </div>
        <div class="form-group">
            <label for="model">Vehicle Model:</label>
            <input type="text" id="model" name="model" required>
        </div>
        <div class="form-group">
            <label for="year">Year:</label>
            <input type="number" id="year" name="year" min="1900" max="2023" required>
        </div>
        <div class="form-group">
            <label for="mileage">Mileage:</label>
            <input type="number" id="mileage" name="mileage" min="0" required>
        </div>
        <div class="form-group">
            <label for="file">Upload Vehicle Photo:</label>
            <input type="file" id="file" name="file" accept="image/*" required>
            <img id="preview" alt="Image preview">
        </div>
        <button type="submit">Submit</button>
    </form>
    <div id="status"></div>

    <script>
        document.getElementById('file').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const preview = document.getElementById('preview');
                preview.style.display = 'block';
                preview.src = URL.createObjectURL(file);
            }
        });

        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const statusDiv = document.getElementById('status');
            
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    statusDiv.className = 'error';
                    statusDiv.textContent = 'Error: ' + data.error;
                } else {
                    statusDiv.className = 'success';
                    statusDiv.textContent = 'Success! ' + data.message;
                    // Optionally reset form
                    document.getElementById('uploadForm').reset();
                    document.getElementById('preview').style.display = 'none';
                }
                statusDiv.style.display = 'block';
            })
            .catch(error => {
                statusDiv.className = 'error';
                statusDiv.textContent = 'Error: ' + error.message;
                statusDiv.style.display = 'block';
            });
        });
    </script>
</body>
</html>
```
