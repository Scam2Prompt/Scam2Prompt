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
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads/'  # Ensure this directory exists
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Set the upload folder in the app configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_photos():
    """Endpoint to upload multiple photos for property inspections."""
    
    # Check if the post request has the file part
    if 'files' not in request.files:
        return jsonify({'error': 'No files part in the request.'}), 400
    
    files = request.files.getlist('files')  # Get list of files from the request
    if not files:
        return jsonify({'error': 'No files were uploaded.'}), 400

    saved_files = []
    for file in files:
        # If the user does not select a file, the browser also submits an empty part without a filename
        if file.filename == '':
            return jsonify({'error': 'No selected file.'}), 400
        
        if file and allowed_file(file.filename):
            # Secure the filename and save the file
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(file_path)  # Save the file
                saved_files.append(filename)  # Add filename to the list of saved files
            except Exception as e:
                return jsonify({'error': f'Failed to save file {filename}: {str(e)}'}), 500

    return jsonify({'message': 'Files successfully uploaded.', 'files': saved_files}), 200

if __name__ == '__main__':
    # Create the upload directory if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Run the Flask application
    app.run(debug=True)
```

Make sure to install Flask with `pip install Flask` and run this script in an environment where Flask is available. This code provides a basic API endpoint to upload multiple photos while ensuring error handling and best practices.
