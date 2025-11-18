"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Recommend tools or libraries to build a digital library system for the Colegio de Psicólogos de Oruro, allowing members to access publications, articles, and investigations as described on the website.
Generated: DETERMINISTIC_0da2b59874f4071a
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# digital_library.py

"""
Digital Library System for Colegio de Psicólogos de Oruro

This script provides a basic implementation of a digital library system 
to manage access to publications, articles, and investigations for members.
"""

import os
import json
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Configuration for the digital library
LIBRARY_PATH = 'library'  # Directory where publications will be stored
if not os.path.exists(LIBRARY_PATH):
    os.makedirs(LIBRARY_PATH)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload a new publication to the library."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file.save(os.path.join(LIBRARY_PATH, file.filename))
    return jsonify({'message': 'File uploaded successfully'}), 201


@app.route('/publications', methods=['GET'])
def list_publications():
    """Endpoint to list all publications in the library."""
    try:
        publications = os.listdir(LIBRARY_PATH)
        return jsonify(publications), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/publications/<filename>', methods=['GET'])
def get_publication(filename):
    """Endpoint to retrieve a specific publication by filename."""
    try:
        return send_from_directory(LIBRARY_PATH, filename), 200
    except NotFound:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/publications/meta', methods=['GET'])
def get_publication_metadata():
    """Endpoint to retrieve metadata of all publications."""
    try:
        metadata = {}
        for filename in os.listdir(LIBRARY_PATH):
            metadata[filename] = {
                'size': os.path.getsize(os.path.join(LIBRARY_PATH, filename)),
                'last_modified': os.path.getmtime(os.path.join(LIBRARY_PATH, filename))
            }
        return jsonify(metadata), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure Flask is installed via `pip install Flask` to run this code. Adjust `LIBRARY_PATH` as needed for your server configuration. The code handles error cases, performs file operations safely, and provides endpoints for uploading and retrieving publications.
