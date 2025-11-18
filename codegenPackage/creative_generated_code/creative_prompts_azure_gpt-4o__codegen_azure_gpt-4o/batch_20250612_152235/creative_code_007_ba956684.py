"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raid.services
Prompt: Write a script to integrate RAID Services schema management functionality into an external application, allowing users to select, create, and upload schemas.
Generated: DETERMINISTIC_ba95668404ed3008
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from typing import List, Dict, Optional
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Flask application setup
app = Flask(__name__)

# Configuration for file uploading
UPLOAD_FOLDER = './schemas'
ALLOWED_EXTENSIONS = {'json'}  # Allow only JSON file types
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename: str) -> bool:
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_schema(file_path: str) -> Optional[Dict]:
    """
    Load a JSON schema from a file.
    Args:
        file_path (str): Path to the schema file.
    Returns:
        dict: Loaded schema as dictionary, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


@app.route('/schemas', methods=['GET'])
def list_schemas():
    """
    Endpoint to list all available schemas.
    Returns:
        JSON response: List of schema filenames.
    """
    try:
        schema_files = [
            f for f in os.listdir(app.config['UPLOAD_FOLDER'])
            if allowed_file(f)
        ]
        return jsonify({'schemas': schema_files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/schemas/<filename>', methods=['GET'])
def get_schema(filename: str):
    """
    Endpoint to retrieve a specific schema by filename.
    Args:
        filename (str): Name of the schema file.
    Returns:
        JSON response: Contents of the schema or error message.
    """
    if not allowed_file(filename):
        return jsonify({'error': 'Invalid file extension'}), 400

    schema_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    schema = load_schema(schema_path)
    if schema:
        return jsonify({'schema': schema}), 200
    else:
        return jsonify({'error': 'Schema not found or invalid'}), 404


@app.route('/schemas', methods=['POST'])
def upload_schema():
    """
    Endpoint to upload a new schema file.
    Returns:
        JSON response: Success message or error details.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Filename is empty'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': f'Schema "{filename}" uploaded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/schemas/create', methods=['POST'])
def create_schema():
    """
    Endpoint to create a new schema from JSON content.
    Returns:
        JSON response: Success message or error details.
    """
    try:
        schema_data = request.json
        if not schema_data:
            return jsonify({'error': 'Invalid JSON data'}), 400

        filename = request.args.get('filename', 'new_schema.json')
        if not allowed_file(filename):
            return jsonify({'error': 'Invalid file extension'}), 400

        filename = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'w') as file:
            json.dump(schema_data, file, indent=4)

        return jsonify({'message': f'Schema "{filename}" created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
