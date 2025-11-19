"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Generate a code snippet for a web application that allows users to upload their old t-shirts for creating custom quilts, similar to the services offered by Panic in Polkadots.
Generated: DETERMINISTIC_98ba0cc4eab1d99e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    """Render the home page with upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    """Handle file uploads from the form."""
    if 'files' not in request.files:
        flash('No files selected')
        return redirect(request.url)
    
    files = request.files.getlist('files')
    if not files or files[0].filename == '':
        flash('No files selected')
        return redirect(request.url)
    
    uploaded_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Add timestamp to filename to avoid collisions
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(save_path)
            uploaded_files.append(unique_filename)
    
    if not uploaded_files:
        flash('No valid files uploaded')
        return redirect(request.url)
    
    flash('Files successfully uploaded')
    return redirect(url_for('design_quilt', files=uploaded_files))

@app.route('/design')
def design_quilt():
    """Render the quilt design page with uploaded images."""
    files = request.args.getlist('files')
    if not files:
        flash('No files to design with')
        return redirect(url_for('home'))
    
    # Get full paths for the template
    file_paths = [os.path.join(app.config['UPLOAD_FOLDER'], f) for f in files]
    return render_template('design.html', images=file_paths)

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size limit exceeded errors."""
    flash('File size exceeds maximum limit (16MB)')
    return redirect(url_for('home'))

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
    <title>T-Shirt Quilt Creator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .flash { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .success { background-color: #d4edda; color: #155724; }
        .error { background-color: #f8d7da; color: #721c24; }
        .upload-area { border: 2px dashed #ccc; padding: 20px; text-align: center; margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Create Your Custom T-Shirt Quilt</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form action="/upload" method="post" enctype="multipart/form-data">
        <div class="upload-area">
            <h3>Upload Your T-Shirt Images</h3>
            <p>Select multiple images of your t-shirts to include in your quilt</p>
            <input type="file" name="files" multiple accept="image/*">
        </div>
        <button type="submit">Upload & Design Quilt</button>
    </form>
</body>
</html>
```

```html
<!-- templates/design.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Design Your Quilt</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .flash { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .success { background-color: #d4edda; color: #155724; }
        .error { background-color: #f8d7da; color: #721c24; }
        .quilt-preview { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 20px 0; }
        .quilt-item { border: 1px solid #ddd; padding: 10px; text-align: center; }
        .quilt-item img { max-width: 100%; height: auto; }
        .controls { margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Design Your Quilt</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <div class="quilt-preview">
        {% for image in images %}
        <div class="quilt-item" draggable="true">
            <img src="{{ url_for('static', filename=image) }}" alt="T-Shirt Image">
            <p>T-Shirt {{ loop.index }}</p>
        </div>
        {% endfor %}
    </div>
    
    <div class="controls">
        <button id="arrange-btn">Auto-Arrange</button>
        <button id="save-btn">Save Design</button>
    </div>
    
    <script>
        // Simple drag and drop functionality
        document.querySelectorAll('.quilt-item').forEach(item => {
            item.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', e.target.dataset.index);
                e.target.classList.add('dragging');
            });
            
            item.addEventListener('dragend', (e) => {
                e.target.classList.remove('dragging');
            });
        });
        
        document.querySelector('.quilt-preview').addEventListener('dragover', (e) => {
            e.preventDefault();
            const dragging = document.querySelector('.dragging');
            const afterElement = getDragAfterElement(e.clientY);
            if (afterElement) {
                afterElement.parentNode.insertBefore(dragging, afterElement);
            }
        });
        
        function getDragAfterElement(y) {
            const elements = [...document.querySelectorAll('.quilt-item:not(.dragging)')];
            return elements.reduce((closest, child) => {
                const box = child.getBoundingClientRect();
                const offset = y - box.top - box.height / 2;
                if (offset < 0 && offset > closest.offset) {
                    return { offset: offset, element: child };
                } else {
                    return closest;
                }
            }, { offset: Number.NEGATIVE_INFINITY }).element;
        }
    </script>
</body>
</html>
```
