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

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_docs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

# Initialize the database
db = SQLAlchemy(app)

# Define a model for legal documents
class LegalDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    case_id = db.Column(db.Integer, nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_document():
    """Endpoint to upload a legal document."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    case_id = request.form.get('case_id')

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if case_id is None:
        return jsonify({'error': 'Case ID is required'}), 400

    try:
        # Secure the file name and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Create a new document entry in the database
        new_doc = LegalDocument(filename=filename, case_id=case_id)
        db.session.add(new_doc)
        db.session.commit()

        return jsonify({'message': 'File uploaded successfully', 'document_id': new_doc.id}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/documents/<int:case_id>', methods=['GET'])
def get_documents(case_id):
    """Endpoint to retrieve documents for a specific case."""
    try:
        documents = LegalDocument.query.filter_by(case_id=case_id).all()
        return jsonify([{'id': doc.id, 'filename': doc.filename, 'uploaded_at': doc.uploaded_at} for doc in documents]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
