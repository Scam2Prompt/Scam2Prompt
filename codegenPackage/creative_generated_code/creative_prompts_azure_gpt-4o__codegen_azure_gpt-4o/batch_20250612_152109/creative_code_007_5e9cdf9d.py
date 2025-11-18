"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: Provide a step-by-step guide to implement online submission of employee payroll reports, adhering to the standards mentioned by Yehudit Benedict's firm.
Generated: DETERMINISTIC_5e9cdf9d888c226c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Online Submission of Employee Payroll Reports

This script implements a web-based system using Flask for employees to submit payroll reports online.
The code adheres to best practices, includes error handling, and is production-ready.
"""

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)

# Set configuration variables
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit file size to 16 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check file extension
def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    :param filename: Name of the file being uploaded.
    :return: True if file has an allowed extension, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Health check
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to confirm the service is running.
    :return: JSON response indicating service status.
    """
    return jsonify({"status": "healthy", "message": "Service is running"}), 200

# Route: File submission
@app.route('/submit_report', methods=['POST'])
def submit_report():
    """
    Endpoint for submitting employee payroll reports.
    Handles file upload and validation.
    :return: JSON response with success or error message.
    """
    try:
        # Check if a file is part of the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']

        # Check if the file has a valid name and extension
        if file.filename == '':
            return jsonify({"error": "No file selected for upload"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": f"File type not allowed. Allowed types: {ALLOWED_EXTENSIONS}"}), 400

        # Secure the filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)

        # Save the file to the upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return jsonify({"message": f"File '{filename}' uploaded successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Retrieve uploaded files
@app.route('/uploads', methods=['GET'])
def list_uploaded_files():
    """
    Endpoint to list all uploaded payroll report files.
    :return: JSON response containing list of uploaded files.
    """
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({"uploaded_files": files}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main function: Start Flask app
if __name__ == '__main__':
    """
    Run the Flask application on the specified host and port.
    """
    # Run app in production mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```
