"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: How would you implement a secure and organized system for storing and retrieving legal documents for a firm like Sardagna Poeta Advogados, considering data protection laws in Brazil?
Generated: DETERMINISTIC_4517139e291194be
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_documents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from an environment variable or generate a new one
encryption_key = os.environ.get('ENCRYPTION_KEY', generate_key())
cipher = Fernet(encryption_key)

# Define the Document model
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    content = db.Column(db.LargeBinary, nullable=False)
    hash = db.Column(db.String(64), nullable=False, unique=True)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.hash = hashlib.sha256(content).hexdigest()

# Create the database
with app.app_context():
    db.create_all()

@app.route('/documents', methods=['POST'])
def upload_document():
    """Upload a new legal document."""
    data = request.json
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        abort(400, 'Title and content are required.')

    # Encrypt the document content
    encrypted_content = cipher.encrypt(content.encode())

    # Create a new Document instance
    new_document = Document(title=title, content=encrypted_content)

    try:
        db.session.add(new_document)
        db.session.commit()
        return jsonify({'message': 'Document uploaded successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, 'Document with this title already exists.')

@app.route('/documents/<int:doc_id>', methods=['GET'])
def retrieve_document(doc_id):
    """Retrieve a legal document by its ID."""
    document = Document.query.get(doc_id)

    if not document:
        abort(404, 'Document not found.')

    # Decrypt the document content
    decrypted_content = cipher.decrypt(document.content).decode()

    return jsonify({
        'title': document.title,
        'content': decrypted_content
    })

@app.route('/documents', methods=['GET'])
def list_documents():
    """List all legal documents."""
    documents = Document.query.all()
    return jsonify([{'id': doc.id, 'title': doc.title} for doc in documents])

if __name__ == '__main__':
    # Run the application
    app.run(debug=False)
```

### Notes:
- Ensure that the `cryptography` and `Flask` packages are installed in your environment.
- Set the `ENCRYPTION_KEY` environment variable for production use to maintain security.
- This code uses SQLite for simplicity; consider using a more robust database for production.
- Error handling is included for common issues such as missing fields and duplicate titles.
