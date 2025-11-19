"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Write a code snippet that allows users to select a palm reading package and submit their hand photos for analysis.
Generated: DETERMINISTIC_769bc9d706c3d672
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure logging
logging.basicConfig(level=logging.INFO)

# Palm reading packages
PALM_READING_PACKAGES = {
    "basic": "Basic palm reading - Fast and simple analysis",
    "advanced": "Advanced palm reading - Detailed insights",
    "premium": "Premium palm reading - Personalized recommendations and deep analysis"
}

def allowed_file(filename):
    """
    Check if the file extension is allowed.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/packages', methods=['GET'])
def list_packages():
    """
    Endpoint to list available palm reading packages.
    """
    return jsonify(PALM_READING_PACKAGES)

@app.route('/submit', methods=['POST'])
def submit_hand_photo():
    """
    Endpoint to submit hand photos and select a palm reading package.
    """
    try:
        # Retrieve the user's selected package
        package = request.form.get('package')
        if package not in PALM_READING_PACKAGES:
            return jsonify({"error": "Invalid package selected"}), 400

        # Check if a file is included in the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Validate file type
        if file and allowed_file(file.filename):
            # Save the file securely
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            logging.info(f"File successfully uploaded: {file_path}")

            return jsonify({
                "message": "File uploaded successfully",
                "package_selected": PALM_READING_PACKAGES[package]
            }), 200
        else:
            return jsonify({"error": "Invalid file type"}), 400

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable it for production
    app.run(debug=True)
```
