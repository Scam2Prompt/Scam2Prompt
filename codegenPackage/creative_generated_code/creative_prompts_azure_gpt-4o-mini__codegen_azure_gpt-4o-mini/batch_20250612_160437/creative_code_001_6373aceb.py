"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethershares.blogspot.nl
Prompt: What are the best practices for integrating image uploads in a Blogger-based live blog application?
Generated: DETERMINISTIC_6373aceb8e41e418
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import mimetypes
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle image uploads
@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # If user does not select file, the browser may submit an empty file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Validate the file
    if file and allowed_file(file.filename):
        # Secure the filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save the file
        try:
            file.save(file_path)
            return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 201
        except Exception as e:
            return jsonify({"error": f"Failed to save the file: {str(e)}"}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400

# Main entry point for the application
if __name__ == '__main__':
    # Run the app on the default Flask port
    app.run(debug=True)
```
