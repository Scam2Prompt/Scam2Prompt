"""
Generated Code Metadata:
========================
Original URL: https://ethershares.blogspot.nl
Prompt: What are the best practices for integrating image uploads in a Blogger-based live blog application?
Generated: DETERMINISTIC_6373aceb8e41e418
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Image Upload Handler for Blogger Live Blog
// This script handles image uploads, resizing, and storage for a Blogger-based live blog

// Configuration
const config = {
  maxFileSize: 5 * 1024 * 1024, // 5MB
  allowedMimeTypes: ['image/jpeg', 'image/png', 'image/gif'],
  thumbnailWidth: 300,
  thumbnailHeight: 200,
  storagePath: 'blogger_images/',
  apiEndpoint: '/_ah/api/upload/v1'
};

// DOM Elements
const uploadForm = document.getElementById('image-upload-form');
const fileInput = document.getElementById('image-file-input');
const uploadProgress = document.getElementById('upload-progress');
const previewContainer = document.getElementById('image-preview');
const errorContainer = document.getElementById('upload-error');

// Initialize the upload form
function initUploadForm() {
  if (!uploadForm || !fileInput) return;

  uploadForm.addEventListener('submit', handleFormSubmit);
  fileInput.addEventListener('change', handleFileSelect);
}

// Handle file selection
function handleFileSelect(event) {
  errorContainer.textContent = '';
  previewContainer.innerHTML = '';
  
  const file = event.target.files[0];
  if (!file) return;

  // Validate file
  if (!validateFile(file)) {
    return;
  }

  // Create preview
  createImagePreview(file);
}

// Validate file before upload
function validateFile(file) {
  if (!file) {
    showError('No file selected');
    return false;
  }

  if (!config.allowedMimeTypes.includes(file.type)) {
    showError('Invalid file type. Only JPEG, PNG, and GIF are allowed.');
    return false;
  }

  if (file.size > config.maxFileSize) {
    showError('File size exceeds maximum limit of 5MB');
    return false;
  }

  return true;
}

// Create image preview
function createImagePreview(file) {
  const reader = new FileReader();
  
  reader.onload = function(e) {
    const img = document.createElement('img');
    img.src = e.target.result;
    img.className = 'upload-preview';
    previewContainer.appendChild(img);
  };
  
  reader.readAsDataURL(file);
}

// Handle form submission
function handleFormSubmit(event) {
  event.preventDefault();
  
  const file = fileInput.files[0];
  if (!file || !validateFile(file)) return;

  uploadImage(file);
}

// Upload image to server
function uploadImage(file) {
  const formData = new FormData();
  formData.append('image', file);
  formData.append('blogId', getBlogId());

  const xhr = new XMLHttpRequest();
  
  xhr.upload.onprogress = function(e) {
    if (e.lengthComputable) {
      const percentComplete = (e.loaded / e.total) * 100;
      uploadProgress.value = percentComplete;
    }
  };

  xhr.onload = function() {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      handleUploadSuccess(response);
    } else {
      handleUploadError(xhr.statusText);
    }
  };

  xhr.onerror = function() {
    handleUploadError('Network error during upload');
  };

  xhr.open('POST', config.apiEndpoint, true);
  xhr.send(formData);
}

// Handle successful upload
function handleUploadSuccess(response) {
  uploadProgress.value = 0;
  fileInput.value = '';
  previewContainer.innerHTML = '';
  
  // Insert image into blog post editor
  if (window.parent && window.parent.insertImageToEditor) {
    window.parent.insertImageToEditor(response.imageUrl, response.thumbnailUrl);
  }
}

// Handle upload error
function handleUploadError(error) {
  showError(`Upload failed: ${error}`);
  uploadProgress.value = 0;
}

// Display error message
function showError(message) {
  errorContainer.textContent = message;
}

// Get current blog ID from Blogger
function getBlogId() {
  try {
    return window.parent.document.getElementById('blogID').value;
  } catch (e) {
    console.error('Could not retrieve blog ID', e);
    return '';
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initUploadForm);
```

```html
<!-- HTML Template for Image Upload -->
<div class="image-upload-container">
  <form id="image-upload-form">
    <div class="form-group">
      <label for="image-file-input">Select Image:</label>
      <input type="file" id="image-file-input" accept="image/jpeg,image/png,image/gif" />
    </div>
    <div id="image-preview" class="image-preview"></div>
    <progress id="upload-progress" value="0" max="100" style="width: 100%;"></progress>
    <div id="upload-error" class="error-message"></div>
    <button type="submit" class="upload-button">Upload Image</button>
  </form>
</div>

<style>
  .image-upload-container {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background: #f9f9f9;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .image-preview {
    margin: 15px 0;
    text-align: center;
  }
  
  .upload-preview {
    max-width: 100%;
    max-height: 300px;
  }
  
  .error-message {
    color: #d32f2f;
    margin: 10px 0;
    min-height: 20px;
  }
  
  .upload-button {
    background: #4285f4;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .upload-button:hover {
    background: #3367d6;
  }
</style>
```

```python
# Backend API for Image Upload (Python Flask example)
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image
import uuid

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/blogger_images'
THUMBNAIL_FOLDER = 'static/blogger_images/thumbnails'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['THUMBNAIL_FOLDER'] = THUMBNAIL_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_thumbnail(image_path, thumbnail_path, size=(300, 200)):
    try:
        img = Image.open(image_path)
        img.thumbnail(size)
        img.save(thumbnail_path)
        return True
    except Exception as e:
        print(f"Error creating thumbnail: {e}")
        return False

@app.route('/_ah/api/upload/v1', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    try:
        # Create directories if they don't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(app.config['THUMBNAIL_FOLDER'], exist_ok=True)
        
        # Generate unique filename
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{ext}"
        secure_name = secure_filename(filename)
        
        # Save original image
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_name)
        file.save(filepath)
        
        # Create thumbnail
        thumbnail_name = f"thumb_{secure_name}"
        thumbnail_path = os.path.join(app.config['THUMBNAIL_FOLDER'], thumbnail_name)
        create_thumbnail(filepath, thumbnail_path)
        
        # Return URLs
        image_url = f"/{app.config['UPLOAD_FOLDER']}/{secure_name}"
        thumbnail_url = f"/{app.config['THUMBNAIL_FOLDER']}/{thumbnail_name}"
        
        return jsonify({
            'success': True,
            'imageUrl': image_url,
            'thumbnailUrl': thumbnail_url
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __
