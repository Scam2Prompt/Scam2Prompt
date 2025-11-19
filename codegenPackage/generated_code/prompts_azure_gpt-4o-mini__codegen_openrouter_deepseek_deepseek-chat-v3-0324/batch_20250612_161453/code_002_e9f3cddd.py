"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Create a function that integrates sound clips and videos about Métis culture into a web application, ensuring it highlights their unique history and language.
Generated: DETERMINISTIC_e9f3cddd0902917f
Batch ID: 20250612_161453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'wav', 'mp4', 'mov'}
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Render the main page with Métis cultural content."""
    # Sample data - in production, this would come from a database
    cultural_content = [
        {
            'title': 'Métis History Overview',
            'description': 'Learn about the rich history of the Métis people.',
            'type': 'video',
            'filename': 'metis_history.mp4'
        },
        {
            'title': 'Métis Language Lesson',
            'description': 'Introduction to Michif language basics.',
            'type': 'audio',
            'filename': 'michif_lesson.mp3'
        }
    ]
    return render_template('index.html', content=cultural_content)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Handle file uploads for cultural content."""
    if request.method == 'POST':
        if 'file' not in request.files:
            return {'error': 'No file part'}, 400
        
        file = request.files['file']
        if file.filename == '':
            return {'error': 'No selected file'}, 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return {'message': 'File uploaded successfully'}, 200
    
    return render_template('upload.html')

@app.route('/media/<filename>')
def serve_media(filename):
    """Serve uploaded media files."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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
    <title>Métis Cultural Content</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .content-item {
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .media-container {
            margin-top: 15px;
        }
        audio, video {
            width: 100%;
            max-width: 600px;
        }
        h1 {
            color: #8B4513; /* SaddleBrown - common in Métis flag */
        }
    </style>
</head>
<body>
    <h1>Métis Cultural Content</h1>
    <p>Explore the rich history and language of the Métis people.</p>
    
    <div class="content-list">
        {% for item in content %}
        <div class="content-item">
            <h2>{{ item.title }}</h2>
            <p>{{ item.description }}</p>
            <div class="media-container">
                {% if item.type == 'video' %}
                <video controls>
                    <source src="{{ url_for('serve_media', filename=item.filename) }}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                {% elif item.type == 'audio' %}
                <audio controls>
                    <source src="{{ url_for('serve_media', filename=item.filename) }}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
                {% endif %}
            </div>
        </div>
        {% endfor %}
    </div>
    
    <a href="{{ url_for('upload_file') }}">Contribute Content</a>
</body>
</html>
```

```html
<!-- templates/upload.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Métis Cultural Content</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .upload-form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="file"] {
            display: block;
            margin-bottom: 10px;
        }
        button {
            background-color: #8B4513;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Upload Métis Cultural Content</h1>
    
    <div class="upload-form">
        <form method="POST" enctype="multipart/form-data" action="{{ url_for('upload_file') }}">
            <div class="form-group">
                <label for="file">Select a file (MP3, WAV, MP4, MOV):</label>
                <input type="file" name="file" id="file" accept=".mp3,.wav,.mp4,.mov" required>
            </div>
            <button type="submit">Upload</button>
        </form>
    </div>
    
    <a href="{{ url_for('index') }}">Back to Content</a>
</body>
</html>
```
