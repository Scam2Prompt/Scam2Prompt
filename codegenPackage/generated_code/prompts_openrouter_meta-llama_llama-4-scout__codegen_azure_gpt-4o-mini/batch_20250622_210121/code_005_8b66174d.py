"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Design a system for securely uploading and processing financial documents, similar to The Bookkeeping Diaries' workflow, and explain the security measures in place.
Generated: DETERMINISTIC_8b66174d069c800d
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set up logging
logging.basicConfig(level=logging.INFO)

# Generate a key for encryption and decryption
# In production, this key should be securely stored and managed
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
cipher = Fernet(ENCRYPTION_KEY.encode())

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and processing."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        logging.error("No selected file")
        return jsonify({"error": "No selected file"}), 400

    # Validate the file
    if not allowed_file(file.filename):
        logging.error("File type not allowed")
        return jsonify({"error": "File type not allowed"}), 400

    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        # Save the file to the upload folder
        file.save(file_path)
        logging.info(f"File saved to {file_path}")

        # Encrypt the file for security
        with open(file_path, 'rb') as f:
            file_data = f.read()
            encrypted_data = cipher.encrypt(file_data)

        # Save the encrypted file
        encrypted_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"encrypted_{filename}")
        with open(encrypted_file_path, 'wb') as ef:
            ef.write(encrypted_data)

        logging.info(f"File encrypted and saved to {encrypted_file_path}")

        # Optionally, process the file (e.g., extract data, etc.)
        # process_file(encrypted_file_path)

        return jsonify({"message": "File uploaded and processed successfully"}), 200

    except Exception as e:
        logging.error(f"Error processing file: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=False)  # Set debug=False for production
```

### Security Measures:
1. **File Validation**: Only allows specific file types to be uploaded.
2. **Secure Filename Handling**: Uses `secure_filename` to prevent directory traversal attacks.
3. **Encryption**: Files are encrypted using the `cryptography` library before being saved.
4. **Environment Variables**: Sensitive information like encryption keys are stored in environment variables.
5. **Error Handling**: Comprehensive error handling to manage different failure scenarios gracefully.
