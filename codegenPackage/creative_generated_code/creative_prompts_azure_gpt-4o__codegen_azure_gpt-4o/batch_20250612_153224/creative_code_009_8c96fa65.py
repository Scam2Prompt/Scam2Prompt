"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Suggest a framework for building a web application that allows clients to securely upload legal documents and track case progress, inspired by the services offered by the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_8c96fa656bf1fe16
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a production-ready implementation using Python's Flask framework, which is lightweight and suitable for building secure web applications. The example includes document upload and case tracking functionality, with security considerations in place.

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import logging

# Initialize Flask application
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = './uploads'  # Path to store uploaded documents
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}  # Accepted file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper function to check allowed file extensions
def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Home page
@app.route('/')
def home():
    return render_template('index.html')  # Render a template for client interaction

# Route: Upload documents
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.warning("No file part in the request")
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        logger.warning("No file selected for uploading")
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file and is_allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Sanitize filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # Save file securely
        logger.info(f"File uploaded successfully: {filename}")
        return jsonify({'message': f'File "{filename}" uploaded successfully!'}), 200
    
    logger.warning("File type not allowed")
    return jsonify({'error': 'File type not allowed'}), 400

# Route: Track case progress
@app.route('/cases/<case_id>', methods=['GET'])
def track_case(case_id):
    # Simulated case data for demonstration purposes
    case_data = {
        '1234': {'status': 'In Progress', 'details': 'Court hearing scheduled for next week.'},
        '5678': {'status': 'Completed', 'details': 'Case closed successfully.'},
    }

    case_info = case_data.get(case_id)
    if case_info:
        logger.info(f"Case {case_id} retrieved successfully")
        return jsonify({'case_id': case_id, 'case_info': case_info}), 200
    
    logger.warning(f"Case {case_id} not found")
    return jsonify({'error': f'Case ID {case_id} not found'}), 404

# Error handler: 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Resource not found'}), 404

# Error handler: General Exception
@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Directory Structure
```
project/
│
├── app.py                # The code above
├── uploads/              # Directory for storing uploaded files
├── templates/
│   └── index.html        # Basic homepage template for user interface
```

### Notes:
- Replace `index.html` with a suitable HTML page for the homepage.
- Use HTTPS in production for secure communication.
- Consider integrating authentication (e.g., Flask-Login) for user access control.
- Use database integration (e.g., SQLAlchemy) for persistent case tracking.
