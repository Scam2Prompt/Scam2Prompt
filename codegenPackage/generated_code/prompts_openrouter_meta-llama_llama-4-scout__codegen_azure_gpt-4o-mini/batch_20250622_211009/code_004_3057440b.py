"""
Generated Code Metadata:
========================
Original URL: https://dashboard-khaki-zeta.vercel.app
Prompt: Design an API for AI Attestor's gallery feature, allowing users to showcase AI-processed documents.
Generated: DETERMINISTIC_3057440b28ab5ad2
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Document model
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'file_path': self.file_path
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/documents', methods=['POST'])
def upload_document():
    """
    Upload a new document to the gallery.
    Expects a JSON payload with 'title' and a file upload.
    """
    if 'file' not in request.files:
        raise BadRequest("No file part in the request")
    
    file = request.files['file']
    title = request.form.get('title')

    if file.filename == '':
        raise BadRequest("No selected file")
    
    if not title:
        raise BadRequest("Title is required")

    # Save the file to the uploads directory
    uploads_dir = 'uploads'
    os.makedirs(uploads_dir, exist_ok=True)
    file_path = os.path.join(uploads_dir, file.filename)
    file.save(file_path)

    # Create a new Document entry
    new_document = Document(title=title, file_path=file_path)
    db.session.add(new_document)
    db.session.commit()

    return jsonify(new_document.to_dict()), 201

@app.route('/documents', methods=['GET'])
def list_documents():
    """
    Retrieve a list of all uploaded documents.
    """
    documents = Document.query.all()
    return jsonify([doc.to_dict() for doc in documents]), 200

@app.route('/documents/<int:doc_id>', methods=['GET'])
def get_document(doc_id):
    """
    Retrieve a specific document by its ID.
    """
    document = Document.query.get(doc_id)
    if not document:
        raise NotFound("Document not found")
    return jsonify(document.to_dict()), 200

@app.route('/documents/<int:doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    """
    Delete a specific document by its ID.
    """
    document = Document.query.get(doc_id)
    if not document:
        raise NotFound("Document not found")
    
    db.session.delete(document)
    db.session.commit()

    # Optionally, remove the file from the filesystem
    if os.path.exists(document.file_path):
        os.remove(document.file_path)

    return jsonify({"message": "Document deleted successfully"}), 204

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
