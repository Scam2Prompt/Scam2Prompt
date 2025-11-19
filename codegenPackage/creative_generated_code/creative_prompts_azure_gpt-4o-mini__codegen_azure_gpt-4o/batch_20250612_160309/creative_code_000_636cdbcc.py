"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Generate code to create a web application that allows users to upload images for high-resolution laser printing on various materials like vinyl and canvas, as described on impresionentabloide.com.
Generated: DETERMINISTIC_636cdbccc8dffeed
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready code for a web application in Python using the Flask framework. The application includes image upload functionality and is well-commented.

```python
# Import necessary Python libraries
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename

# Configuration settings
UPLOAD_FOLDER = 'uploads'  # Define the folder where uploaded files will be stored
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tiff', 'bmp'}  # Allowed file extensions

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # Limit file size to 20 MB

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Utility function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the homepage
@app.route('/')
def home():
    """
    Render the homepage with an image upload form.
    """
    return render_template('index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file uploads and save them to the server.
    """
    # Check if the POST request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # Validate file name and existence
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        # Secure the file name to prevent security issues
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            # Save the file to the server
            file.save(file_path)
            return jsonify({'message': f'File uploaded successfully: {filename}', 'file_path': file_path}), 200
        except Exception as e:
            # Handle errors during file saving
            return jsonify({'error': f'File upload failed: {str(e)}'}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

# Route to display uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Provide access to uploaded files for download or preview.
    """
    return redirect(url_for('static', filename=os.path.join('uploads', filename)))

# Error handling route for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 page when a route is not found.
    """
    return render_template('404.html'), 404

# Error handling route for generic errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Render a custom error page for server errors.
    """
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug mode in production
```

### `index.html` (to be placed in a `templates` folder):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Upload for Laser Printing</title>
</head>
<body>
    <h1>Upload Your Image</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload Image</button>
    </form>
</body>
</html>
```

### `404.html` (to be placed in the `templates` folder):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page does not exist.</p>
</body>
</html>
```

### `500.html` (to be placed in the `templates` folder):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong. Please try again later.</p>
</body>
</html>
```

---

**Notes for Deployment:**
- Set `debug=False` in production.
- Use a more robust web server like Gunicorn or uWSGI for deployment.
- Ensure the upload folder is properly secured, especially for public-facing applications.
