"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Generate a code snippet for a web application that allows users to customize promotional items using CreatexPro's unique personalization techniques like serigraphy and DTF printing.
Generated: DETERMINISTIC_3b1109b5dc649964
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image
import uuid

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Render the main customization page"""
    return render_template('index.html')

@app.route('/upload-design', methods=['POST'])
def upload_design():
    """Handle design upload for personalization"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())
        new_filename = f"{unique_id}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        
        try:
            # Save the file
            file.save(filepath)
            
            # Process the image (resize if needed)
            with Image.open(filepath) as img:
                if img.size[0] > 2000 or img.size[1] > 2000:
                    img.thumbnail((2000, 2000))
                    img.save(filepath)
            
            return jsonify({
                'success': True,
                'filename': new_filename,
                'message': 'File uploaded successfully'
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/customize', methods=['POST'])
def customize_item():
    """Handle item customization with selected technique"""
    data = request.get_json()
    
    required_fields = ['item_id', 'design_id', 'technique', 'custom_text', 'colors']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        technique = data['technique'].lower()
        if technique not in ['serigraphy', 'dtf']:
            return jsonify({'error': 'Invalid technique specified'}), 400
        
        # Here you would typically:
        # 1. Validate the design exists
        # 2. Process the customization based on technique
        # 3. Generate a preview or production file
        # 4. Return the result
        
        # Mock response for demonstration
        return jsonify({
            'success': True,
            'preview_url': f'/previews/{uuid.uuid4()}.jpg',
            'message': f'Item customized with {technique} technique'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size limit errors"""
    return jsonify({'error': 'File size exceeds maximum limit (16MB)'}), 413

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CreatexPro Customization</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .upload-container {
            border: 2px dashed #ccc;
            padding: 20px;
            text-align: center;
            margin-bottom: 20px;
        }
        .preview {
            max-width: 100%;
            display: none;
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        select, input, textarea {
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
    </style>
</head>
<body>
    <h1>Customize Your Promotional Item</h1>
    
    <div class="upload-container">
        <h2>Upload Your Design</h2>
        <input type="file" id="designFile" accept=".png,.jpg,.jpeg">
        <button onclick="uploadDesign()">Upload Design</button>
        <div id="uploadStatus"></div>
        <img id="previewImage" class="preview" alt="Design Preview">
    </div>
    
    <form id="customizationForm">
        <div class="form-group">
            <label for="itemType">Item Type:</label>
            <select id="itemType" required>
                <option value="">Select an item</option>
                <option value="tshirt">T-Shirt</option>
                <option value="mug">Mug</option>
                <option value="bag">Tote Bag</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="technique">Personalization Technique:</label>
            <select id="technique" required>
                <option value="">Select a technique</option>
                <option value="serigraphy">Serigraphy</option>
                <option value="dtf">DTF Printing</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="customText">Custom Text:</label>
            <input type="text" id="customText" placeholder="Enter your custom text">
        </div>
        
        <div class="form-group">
            <label for="colors">Color Selection:</label>
            <input type="color" id="color1" value="#000000">
            <input type="color" id="color2" value="#ffffff">
        </div>
        
        <button type="button" onclick="submitCustomization()">Preview Customization</button>
    </form>
    
    <div id="resultContainer" style="display: none;">
        <h2>Your Customized Item</h2>
        <div id="previewResult"></div>
        <button onclick="placeOrder()">Place Order</button>
    </div>
    
    <script>
        let uploadedDesignId = null;
        
        function uploadDesign() {
            const fileInput = document.getElementById('designFile');
            const file = fileInput.files[0];
            const statusDiv = document.getElementById('uploadStatus');
            const previewImage = document.getElementById('previewImage');
            
            if (!file) {
                statusDiv.textContent = 'Please select a file first';
                statusDiv.style.color = 'red';
                return;
            }
            
            const formData = new FormData();
            formData.append('file', file);
            
            fetch('/upload-design', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    statusDiv.textContent = data.message;
                    statusDiv.style.color = 'green';
                    uploadedDesignId = data.filename;
                    
                    // Show preview
                    previewImage.src = URL.createObjectURL(file);
                    previewImage.style.display = 'block';
                } else {
                    statusDiv.textContent = data.error;
                    statusDiv.style.color = 'red';
                }
            })
            .catch(error => {
                statusDiv.textContent = 'Error uploading file';
                statusDiv.style.color = 'red';
                console.error('Error:', error);
            });
        }
        
        function submitCustomization() {
            if (!uploadedDesignId) {
                alert('Please upload a design first');
                return;
            }
            
            const itemType = document.getElementById('itemType').value;
            const technique = document.getElementById('technique').value;
            const customText = document.getElementById('customText').value;
            const color1 = document.getElementById('color1').value;
            const color2 = document.getElementById('color2').value;
            
            if (!itemType || !technique) {
                alert('Please fill all required fields');
                return;
            }
            
            const data = {
                item_id: itemType,
