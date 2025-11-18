"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cem-seven.vercel.app
Prompt: Suggest a method to create a user interface for uploading files and generating tokens with custom metadata, referencing the Co-Edition platform's features.
Generated: DETERMINISTIC_8816b9a3f4e5bd95
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
import os
import uuid

app = Flask(__name__)

# Set the directory where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """
    Renders the home page with the file upload interface.
    """
    return render_template('index.html')  # Provide an HTML file with upload and metadata form

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles file uploads and token generation with custom metadata.
    """
    try:
        # Check for a file in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        # Validate file selection
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Save the file securely
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Generate a unique token (UUID)
        token = str(uuid.uuid4())

        # Retrieve custom metadata from the request
        metadata = request.form.get('metadata', '')

        # Create a response object with the token and metadata
        response = {
            'token': token,
            'metadata': metadata,
            'file_name': file.filename,
            'file_path': file_path
        }

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True)
```

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload with Metadata</title>
</head>
<body>
    <h1>Upload a File with Metadata</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <label for="file">Choose file:</label>
        <input type="file" name="file" id="file" required><br><br>
        <label for="metadata">Enter metadata:</label>
        <input type="text" name="metadata" id="metadata"><br><br>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
