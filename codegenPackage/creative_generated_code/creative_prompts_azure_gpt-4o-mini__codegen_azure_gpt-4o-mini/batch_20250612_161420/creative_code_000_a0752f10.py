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

```python
from flask import Flask, request, jsonify
import os
import zipfile
import rarfile
import requests
from io import BytesIO
import tempfile

app = Flask(__name__)

# Ensure the temporary folder exists
TEMP_FOLDER = 'temp_extraction'
os.makedirs(TEMP_FOLDER, exist_ok=True)

@app.route('/extract', methods=['POST'])
def extract_files():
    """
    Extract ZIP or RAR files from a URL or uploaded file.

    Request should contain either:
    - 'file': the uploaded file (ZIP or RAR)
    - 'url': the URL of the file (ZIP or RAR)

    Returns:
        JSON response with extraction results or error message.
    """
    try:
        # Check if the request contains a file upload or a URL
        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename.endswith(('.zip', '.rar')):
                extracted_files = extract_from_file(uploaded_file)
                return jsonify({'status': 'success', 'files': extracted_files}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Invalid file type. Only ZIP and RAR files are allowed.'}), 400

        elif 'url' in request.json:
            file_url = request.json['url']
            response = requests.get(file_url)
            response.raise_for_status()  # Raise an error for bad responses
            if file_url.endswith(('.zip', '.rar')):
                file_like_object = BytesIO(response.content)
                extracted_files = extract_from_file(file_like_object)
                return jsonify({'status': 'success', 'files': extracted_files}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Invalid file type. Only ZIP and RAR files are allowed.'}), 400

        else:
            return jsonify({'status': 'error', 'message': 'No file or URL provided.'}), 400

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


def extract_from_file(file_object):
    """
    Extract contents from a given file object (ZIP or RAR).

    :param file_object: The file object (uploaded file or BytesIO)
    :return: List of extracted file names
    """
    extracted_files = []

    # Determine the file type based on the extension
    if file_object.filename.endswith('.zip'):
        with zipfile.ZipFile(file_object, 'r') as zip_ref:
            zip_ref.extractall(TEMP_FOLDER)
            extracted_files = zip_ref.namelist()

    elif file_object.filename.endswith('.rar'):
        with rarfile.RarFile(file_object, 'r') as rar_ref:
            rar_ref.extractall(TEMP_FOLDER)
            extracted_files = rar_ref.namelist()

    # Return the list of extracted files
    return extracted_files


@app.route('/cleanup', methods=['DELETE'])
def cleanup():
    """
    Cleanup temporary extraction files.
    """
    try:
        for filename in os.listdir(TEMP_FOLDER):
            file_path = os.path.join(TEMP_FOLDER, filename)
            os.remove(file_path)
        return jsonify({'status': 'success', 'message': 'Temporary files cleaned up.'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
```

Make sure to install the required packages using:

```bash
pip install Flask rarfile requests
```

This code snippet creates a Flask application that provides an endpoint for extracting ZIP and RAR files from uploaded files or URLs while handling errors and ensuring proper cleanup of temporary files.
