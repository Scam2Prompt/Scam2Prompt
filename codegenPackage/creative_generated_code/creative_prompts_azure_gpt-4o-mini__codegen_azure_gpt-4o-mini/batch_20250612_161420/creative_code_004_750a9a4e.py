"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toshowbiz.com
Prompt: Describe the process of uploading a RAR or ZIP file for extraction using an online service that guarantees privacy and speed.
Generated: DETERMINISTIC_750a9a4edf4ad7ef
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
import rarfile
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set the directory where uploaded files will be stored
UPLOAD_DIRECTORY = "uploads"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and extraction."""
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    file.save(file_path)
    
    # Determine file type and extract accordingly
    try:
        if file.filename.endswith('.zip'):
            return extract_zip(file_path)
        elif file.filename.endswith('.rar'):
            return extract_rar(file_path)
        else:
            return jsonify({"error": "Unsupported file type. Only ZIP and RAR files are allowed."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred during extraction: {str(e)}"}), 500
    finally:
        # Clean up: Remove the uploaded file after processing
        if os.path.exists(file_path):
            os.remove(file_path)

def extract_zip(file_path):
    """Extract ZIP file."""
    extraction_path = os.path.join(UPLOAD_DIRECTORY, "extracted", os.path.basename(file_path).replace('.zip', ''))
    os.makedirs(extraction_path, exist_ok=True)
    
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)
    
    return jsonify({"message": "ZIP file extracted successfully", "files": os.listdir(extraction_path)}), 200

def extract_rar(file_path):
    """Extract RAR file."""
    extraction_path = os.path.join(UPLOAD_DIRECTORY, "extracted", os.path.basename(file_path).replace('.rar', ''))
    os.makedirs(extraction_path, exist_ok=True)
    
    with rarfile.RarFile(file_path) as rar_ref:
        rar_ref.extractall(extraction_path)
    
    return jsonify({"message": "RAR file extracted successfully", "files": os.listdir(extraction_path)}), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
