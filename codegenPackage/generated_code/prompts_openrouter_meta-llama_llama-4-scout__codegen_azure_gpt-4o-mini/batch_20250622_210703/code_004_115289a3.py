"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: How would you implement a simple document management system for a public communal enterprise like "ЦРНИЦА" in Параћин using a library or framework of your choice?
Generated: DETERMINISTIC_115289a3606b7a18
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx', 'txt'}

# Initialize the database
db = SQLAlchemy(app)

# Define the Document model
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Document {self.filename}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to upload a document
@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Save document info to the database
        new_document = Document(filename=filename, filepath=filepath)
        db.session.add(new_document)
        db.session.commit()
        
        return jsonify({'message': 'File uploaded successfully', 'document_id': new_document.id}), 201
    return jsonify({'error': 'File type not allowed'}), 400

# Route to retrieve a document
@app.route('/documents/<int:document_id>', methods=['GET'])
def get_document(document_id):
    document = Document.query.get(document_id)
    if document is None:
        return jsonify({'error': 'Document not found'}), 404
    return send_from_directory(app.config['UPLOAD_FOLDER'], document.filename)

# Route to list all documents
@app.route('/documents', methods=['GET'])
def list_documents():
    documents = Document.query.all()
    return jsonify([{'id': doc.id, 'filename': doc.filename} for doc in documents]), 200

# Main entry point
if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Run the application
    app.run(debug=True)
```
