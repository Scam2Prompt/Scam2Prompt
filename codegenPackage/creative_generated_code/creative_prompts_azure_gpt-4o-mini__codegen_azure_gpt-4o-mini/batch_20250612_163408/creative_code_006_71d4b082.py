"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Create a web application that showcases interactive media, leveraging the skills of Brendan Whitfield from the FOSS@RIT profiles.
Generated: DETERMINISTIC_71d4b0822da8193b
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a simple web application using Flask (a Python web framework) to showcase interactive media. This application can serve images or videos and allows users to interact with the content. 

Please ensure you have Flask installed in your environment (`pip install Flask`) before running the code.

```python
from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for production

# Set the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render the home page with media content."""
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', media_files=media_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(url_for('home'))
    
    flash('File type not allowed')
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to create a folder named `templates` in the same directory as this script and add an `index.html` file inside it with the following content for the HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Media Showcase</title>
</head>
<body>
    <h1>Interactive Media Showcase</h1>
    
    <!-- Upload Form -->
    <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    
    <!-- Display Uploaded Media -->
    <h2>Uploaded Media</h2>
    <ul>
        {% for media in media_files %}
            <li>
                {% if media.endswith(('png', 'jpg', 'jpeg', 'gif')) %}
                    <img src="{{ url_for('static', filename='uploads/' + media) }}" alt="{{ media }}" style="max-width: 200px;">
                {% elif media.endswith(('mp4', 'avi')) %}
                    <video controls style="max-width: 200px;">
                        <source src="{{ url_for('static', filename='uploads/' + media) }}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

This code provides a basic web application where users can upload images and videos, which are then displayed on the homepage. Remember to implement security measures and optimize the application further for production use.
