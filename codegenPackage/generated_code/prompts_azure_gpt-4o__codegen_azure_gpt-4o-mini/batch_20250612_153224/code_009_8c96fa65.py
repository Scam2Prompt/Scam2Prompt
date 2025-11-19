"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Suggest a framework for building a web application that allows clients to securely upload legal documents and track case progress, inspired by the services offered by the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_8c96fa656bf1fe16
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for storing legal documents
class LegalDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    case_id = db.Column(db.String(120), nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<LegalDocument {self.filename}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for uploading legal documents
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        logging.error("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Save document info to the database
        new_document = LegalDocument(filename=filename, case_id=request.form.get('case_id'))
        db.session.add(new_document)
        db.session.commit()

        logging.info(f"File uploaded successfully: {filename}")
        return jsonify({'message': 'File uploaded successfully'}), 201

    logging.error("File type not allowed")
    return jsonify({'error': 'File type not allowed'}), 400

# Route for tracking case progress
@app.route('/case/<case_id>', methods=['GET'])
def track_case(case_id):
    documents = LegalDocument.query.filter_by(case_id=case_id).all()
    if not documents:
        logging.warning(f"No documents found for case ID: {case_id}")
        return jsonify({'message': 'No documents found for this case ID'}), 404

    return jsonify([{'id': doc.id, 'filename': doc.filename, 'uploaded_at': doc.uploaded_at} for doc in documents]), 200

# Main entry point for the application
if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```
