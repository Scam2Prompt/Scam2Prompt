"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Generate a code snippet for a web application that allows users to upload and print custom designs for large format printing, similar to the services offered by Ram Digi.
Generated: DETERMINISTIC_26b92b2e30e41e63
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_FILE_SIZE_MB = 50  # Maximum file size in MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_MB * 1024 * 1024  # Convert MB to bytes

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to handle file uploads."""
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # Check if the user selected a file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Validate the file type and save it securely
    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400

@app.route('/print/<filename>', methods=['GET'])
def print_file(filename):
    """Endpoint to simulate printing a file."""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        
        # Check if file exists
        if not os.path.exists(filepath):
            return jsonify({"error": "File not found"}), 404

        # Open and preprocess the file if needed (example: resizing for print)
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            with Image.open(filepath) as img:
                img = img.resize((6000, 4000))  # Example: resizing for large format prints
                print_filepath = filepath.rsplit('.', 1)[0] + "_print_ready." + filepath.rsplit('.', 1)[1]
                img.save(print_filepath)
                return send_file(print_filepath, as_attachment=True)
        else:
            # Directly serve non-image files like PDFs
            return send_file(filepath, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
