"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Provide code examples for implementing account verification through document uploads, as required for identity verification on the Parimatch platform.
Generated: DETERMINISTIC_0969143dc627ecdd
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

# Configurations for file uploads
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'jpg', 'jpeg', 'png'}
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB limit

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_document', methods=['POST'])
def upload_document():
    """Endpoint for uploading identity verification documents."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        # Secure the filename and generate a unique identifier
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        
        # Save the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))

        # Here you would typically save the file info to a database
        # For demonstration, we return the filename
        return jsonify({'status': 'success', 'filename': unique_filename}), 201

    except Exception as e:
        # Handle any exceptions that occur during file saving
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure to install Flask using `pip install Flask` if you haven't already.
- This code assumes you are running a Flask application.
- Modify the `UPLOAD_FOLDER` as needed for your environment.
- The application is set to run in debug mode; remember to set `debug=False` in production.
