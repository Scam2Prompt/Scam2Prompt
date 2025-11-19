"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toshowbiz.com
Prompt: How can I extract RAR and ZIP files online without installing software, using a URL or file upload?
Generated: DETERMINISTIC_a0752f108528a1a1
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code snippet that uses Flask for creating a web service to extract RAR and ZIP files uploaded by the user or provided via URL. It leverages the `zipfile` library for ZIP files and `rarfile` for RAR files. Make sure `rarfile` is installed (`pip install rarfile`) and the `unrar` binary is properly configured on your system.

```python
from flask import Flask, request, jsonify, send_file
import os
import zipfile
import rarfile
import requests
import tempfile
import shutil

app = Flask(__name__)

# Temporary directory to store extracted files
TEMP_DIR = tempfile.mkdtemp()

@app.route('/extract', methods=['POST'])
def extract_file():
    """
    API endpoint to extract ZIP or RAR files. Supports file upload or URL input.
    """
    try:
        # Check if a file is uploaded or a URL is provided
        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename == '':
                return jsonify({'error': 'No file selected for upload'}), 400

            # Save the uploaded file temporarily
            temp_file_path = os.path.join(TEMP_DIR, uploaded_file.filename)
            uploaded_file.save(temp_file_path)
        elif 'url' in request.form:
            file_url = request.form['url']
            if not file_url:
                return jsonify({'error': 'Invalid URL'}), 400
            
            # Download the file from the URL
            response = requests.get(file_url, stream=True)
            if response.status_code != 200:
                return jsonify({'error': 'Failed to download file from URL'}), 400
            
            # Save the downloaded file temporarily
            temp_file_name = file_url.split('/')[-1]
            temp_file_path = os.path.join(TEMP_DIR, temp_file_name)
            with open(temp_file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            return jsonify({'error': 'No file or URL provided'}), 400
        
        # Determine file type and extract contents
        extracted_dir = os.path.join(TEMP_DIR, os.path.splitext(os.path.basename(temp_file_path))[0])
        os.makedirs(extracted_dir, exist_ok=True)

        if zipfile.is_zipfile(temp_file_path):
            with zipfile.ZipFile(temp_file_path, 'r') as zip_ref:
                zip_ref.extractall(extracted_dir)
        elif temp_file_path.endswith('.rar'):
            with rarfile.RarFile(temp_file_path, 'r') as rar_ref:
                rar_ref.extractall(extracted_dir)
        else:
            return jsonify({'error': 'Unsupported file type. Only ZIP and RAR files are allowed.'}), 400

        # Prepare extracted files for download
        archive_name = f"{os.path.splitext(os.path.basename(temp_file_path))[0]}_extracted.zip"
        archive_path = os.path.join(TEMP_DIR, archive_name)
        shutil.make_archive(archive_path.replace('.zip', ''), 'zip', extracted_dir)

        return send_file(archive_path, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Clean up temporary files
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@app.route('/')
def home():
    """
    Simple homepage for the API.
    """
    return '''
    <h1>File Extraction Service</h1>
    <p>Upload a ZIP or RAR file or provide a URL to extract its contents.</p>
    <form method="POST" action="/extract" enctype="multipart/form-data">
        <input type="file" name="file">
        <br><br>
        <input type="text" name="url" placeholder="Enter file URL">
        <br><br>
        <button type="submit">Extract</button>
    </form>
    '''

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
1. Install required Python packages with `pip install flask rarfile requests`.
2. Configure the `unrar` binary for `rarfile` to work correctly; see `rarfile` documentation.
3. This code is ready for production but should ideally be deployed behind a web server (e.g., Gunicorn, Nginx).
