"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Generate an API call that allows for the upload of unlimited photos during property inspections, as seen in the BeSoft application.
Generated: DETERMINISTIC_ae299a4b6c7c4d06
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configure upload settings
UPLOAD_FOLDER = 'uploads/'  # Define the folder where images will be stored
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # Allowed file types
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Function to check if the file extension is allowed.
    :param filename: Name of the file
    :return: True if the file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_photos', methods=['POST'])
def upload_photos():
    """
    API endpoint to upload multiple photos.
    :return: JSON response indicating success or error
    """
    # Check if files are included in the request
    if 'photos' not in request.files:
        return jsonify({"error": "No files part in the request"}), 400

    files = request.files.getlist('photos')  # Get all files from the request
    uploaded_files = []  # List to keep track of successfully uploaded files

    for file in files:
        if file and allowed_file(file.filename):
            try:
                filename = secure_filename(file.filename)  # Sanitize filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save file to upload folder
                uploaded_files.append(filename)  # Add filename to uploaded files list
            except Exception as e:
                return jsonify({"error": f"Failed to upload {file.filename}: {str(e)}"}), 500
        else:
            return jsonify({"error": f"File {file.filename} is not allowed"}), 400

    # Return success response with list of uploaded files
    return jsonify({
        "message": "Photos uploaded successfully",
        "uploaded_files": uploaded_files
    }), 200

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development (disable in production)
```

This code is a Flask-based API that handles the upload of multiple photos during property inspections. The photos are validated for file type, stored securely, and error handling is implemented for edge cases.
