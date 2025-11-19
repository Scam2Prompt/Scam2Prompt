"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: How can I implement a private label service in my apparel business similar to the one offered by Bern Wears? Provide a code example for managing custom labels.
Generated: DETERMINISTIC_77e386d39079ad1d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import uuid
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file upload
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Endpoint to upload a custom label design
@app.route('/upload-label', methods=['POST'])
def upload_label():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    # Check if a file was provided
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Validate file type
    if file and allowed_file(file.filename):
        try:
            # Secure the filename and generate a unique ID to avoid overwriting
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            
            # Save the file
            file.save(file_path)
            return jsonify({"message": "File uploaded successfully", "file_name": unique_filename}), 200
        except Exception as e:
            return jsonify({"error": f"File upload failed: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid file type"}), 400

# Endpoint to retrieve uploaded custom labels
@app.route('/labels', methods=['GET'])
def list_labels():
    try:
        # List all files in the upload directory
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({"labels": files}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve labels: {str(e)}"}), 500

# Endpoint to delete a specific label
@app.route('/delete-label/<string:filename>', methods=['DELETE'])
def delete_label(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Check if the file exists
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        
        # Delete the file
        os.remove(file_path)
        return jsonify({"message": "File deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to delete label: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic implementation for managing custom label designs in an apparel business using Flask, including functionality to upload, list, and delete custom label files.
