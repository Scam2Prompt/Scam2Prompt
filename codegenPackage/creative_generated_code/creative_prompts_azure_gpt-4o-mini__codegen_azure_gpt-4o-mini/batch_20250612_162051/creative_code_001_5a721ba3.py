"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoriojustiniano.com.br
Prompt: How can I create a digital form for clients to submit documents for authentication at Cartório Justiniano?
Generated: DETERMINISTIC_5a721ba31b7d069a
Batch ID: 20250612_162051
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

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}  # Allowed document types

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for uploading documents
@app.route('/upload', methods=['POST'])
def upload_document():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # If user does not select a file, browser also submits an empty part without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Check if the file is allowed
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# Start the Flask application
if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)  # Run the app on port 5000
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Instructions to Run:
1. Ensure you have Flask installed: `pip install Flask`
2. Save the code to a file named `app.py`.
3. Run the application: `python app.py`
4. Use a tool like Postman or cURL to test the `/upload` endpoint by sending a POST request with a file.
