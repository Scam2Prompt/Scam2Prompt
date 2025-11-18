"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puroworldclub.com
Prompt: Suggest an API for managing franchisee applications for the Puro World Club, including features for securely uploading documents and tracking application statuses.
Generated: DETERMINISTIC_e8722bbfd049818e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: franchisee_application_api.py

from flask import Flask, request, jsonify
import os
import uuid
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB file size limit
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx', 'png', 'jpg', 'jpeg'}

# In-memory database simulation for applications
applications = {}  # Dictionary to store applications {application_id: {status, documents}}

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route: Upload document for franchisee application
@app.route('/api/upload_document', methods=['POST'])
def upload_document():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        
        # Check if file is selected and valid
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        if not allowed_file(file.filename):
            return jsonify({'error': f'File type not allowed. Allowed types: {app.config["ALLOWED_EXTENSIONS"]}'}), 400
        
        # Secure filename and save file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
        return jsonify({'message': 'File uploaded successfully', 'filename': unique_filename}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during file upload', 'details': str(e)}), 500

# Route: Submit new franchisee application
@app.route('/api/submit_application', methods=['POST'])
def submit_application():
    try:
        data = request.json
        
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required'}), 400
        
        application_id = str(uuid.uuid4())  # Generate unique application ID
        applications[application_id] = {
            'name': data['name'],
            'email': data['email'],
            'status': 'Submitted',
            'documents': [],
        }
        
        return jsonify({'message': 'Application submitted successfully', 'application_id': application_id}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred during application submission', 'details': str(e)}), 500

# Route: Update application status
@app.route('/api/update_status/<application_id>', methods=['PUT'])
def update_status(application_id):
    try:
        data = request.json
        if not data or 'status' not in data:
            return jsonify({'error': 'Status is required'}), 400

        if application_id not in applications:
            return jsonify({'error': 'Application not found'}), 404
        
        applications[application_id]['status'] = data['status']
        return jsonify({'message': 'Application status updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during status update', 'details': str(e)}), 500

# Route: Attach document to franchisee application
@app.route('/api/attach_document/<application_id>', methods=['POST'])
def attach_document(application_id):
    try:
        data = request.json
        if not data or 'filename' not in data:
            return jsonify({'error': 'Filename is required'}), 400

        if application_id not in applications:
            return jsonify({'error': 'Application not found'}), 404
        
        # Simulate attaching document by adding filename to the application
        applications[application_id]['documents'].append(data['filename'])
        return jsonify({'message': 'Document attached successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during document attachment', 'details': str(e)}), 500

# Route: Get application details
@app.route('/api/get_application/<application_id>', methods=['GET'])
def get_application(application_id):
    try:
        if application_id not in applications:
            return jsonify({'error': 'Application not found'}), 404
        
        return jsonify(applications[application_id]), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during fetching application details', 'details': str(e)}), 500

# Entry point: Run Flask application
if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Run the application
    app.run(debug=True)
```
