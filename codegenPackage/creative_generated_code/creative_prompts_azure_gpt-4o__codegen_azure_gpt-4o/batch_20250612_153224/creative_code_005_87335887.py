"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Provide a step-by-step guide to integrate video podcast production into a website, referencing MoOve Marketing's expertise in video podcast creation.
Generated: DETERMINISTIC_87335887d05406e0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Step-by-Step Guide: Integrating Video Podcast Production into a Website
This script outlines a process for integrating video podcast production into a website,
leveraging MoOve Marketing's expertise. This includes embedding video podcasts and
managing related content. The script uses Flask (a Python web framework) to demonstrate
the integration.
"""

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configure the folder to store uploaded podcasts
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed video file extensions for podcast uploads
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'wmv', 'avi', 'mkv'}

def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
    """
    Render the homepage for the website that lists all video podcasts.
    """
    try:
        # List all video files in the upload folder
        video_podcasts = [
            os.path.join(app.config['UPLOAD_FOLDER'], f)
            for f in os.listdir(app.config['UPLOAD_FOLDER'])
            if allowed_file(f)
        ]
        return render_template('homepage.html', video_podcasts=video_podcasts)
    except Exception as e:
        return f"Error loading homepage: {e}", 500

@app.route('/upload', methods=['GET', 'POST'])
def upload_podcast():
    """
    Handle podcast video uploads.
    """
    if request.method == 'POST':
        # Check if the post request has the file
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            # Securely save the file
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({"success": f"File {filename} uploaded successfully!"}), 200
        else:
            return jsonify({"error": "File type not allowed"}), 400
    return render_template('upload.html')

@app.route('/podcast/<filename>')
def view_podcast(filename):
    """
    Render a page to view a specific video podcast.
    """
    try:
        # Check if the requested file exists
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return "Podcast not found", 404
        return render_template('view_podcast.html', video_path=filepath)
    except Exception as e:
        return f"Error loading podcast: {e}", 500

# Error handling for 404 and 500 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors (Page Not Found).
    """
    return render_template('404.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors (Internal Server Error).
    """
    return render_template('500.html', error=e), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Template: homepage.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Video Podcasts</title>
</head>
<body>
    <h1>Welcome to MoOve Marketing Video Podcast Platform</h1>
    <h2>Available Podcasts:</h2>
    <ul>
        {% for video in video_podcasts %}
            <li><a href="/podcast/{{ video.split('/')[-1] }}">{{ video.split('/')[-1] }}</a></li>
        {% endfor %}
    </ul>
    <a href="/upload">Upload a New Podcast</a>
</body>
</html>
```

```html
<!-- Template: upload.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload Video Podcast</title>
</head>
<body>
    <h1>Upload a Video Podcast</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <label for="file">Select a video file:</label>
        <input type="file" id="file" name="file" accept="video/*">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

```html
<!-- Template: view_podcast.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Podcast</title>
</head>
<body>
    <h1>Watch Video Podcast</h1>
    <video controls width="800">
        <source src="{{ video_path }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <a href="/">Go Back to Homepage</a>
</body>
</html>
```

```html
<!-- Template: 404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>{{ error }}</p>
    <a href="/">Go Back to Homepage</a>
</body>
</html>
```

```html
<!-- Template: 500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>500 - Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>{{ error }}</p>
    <a href="/">Go Back to Homepage</a>
</body>
</html>
```

- Install dependencies: `Flask` and `werkzeug` (for `secure_filename`).
- Save HTML files in a `templates/` folder alongside the Python script.
- Ensure `static/uploads` is created for video uploads.
