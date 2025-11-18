"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Provide a solution for implementing a document storage system with a focus on security and technology, inspired by EasyDoc Gestão's expertise in archival services.
Generated: DETERMINISTIC_23580e1c701fe36d
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, send_from_directory, abort

# Initialize Flask application
app = Flask(__name__)

# Directory for storing encrypted documents
DOCUMENTS_DIR = 'documents'
os.makedirs(DOCUMENTS_DIR, exist_ok=True)

# Generate a key for encryption and decryption
# In production, this key should be securely stored and managed
def generate_key():
    return Fernet.generate_key()

# Load or create encryption key
def load_key():
    if not os.path.exists('secret.key'):
        key = generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
    else:
        with open('secret.key', 'rb') as key_file:
            key = key_file.read()
    return key

# Encrypt the document content
def encrypt_document(content):
    key = load_key()
    fernet = Fernet(key)
    encrypted_content = fernet.encrypt(content.encode())
    return encrypted_content

# Decrypt the document content
def decrypt_document(encrypted_content):
    key = load_key()
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content).decode()
    return decrypted_content

# Hash filename to avoid collisions and maintain security
def hash_filename(filename):
    return hashlib.sha256(filename.encode()).hexdigest()

@app.route('/upload', methods=['POST'])
def upload_document():
    """Upload a document to the storage system."""
    # Check if the request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser also submits an empty part without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Encrypt document and save it
    try:
        encrypted_content = encrypt_document(file.read().decode())
        hashed_name = hash_filename(file.filename)
        with open(os.path.join(DOCUMENTS_DIR, hashed_name), 'wb') as f:
            f.write(encrypted_content)
        return jsonify({'message': 'Document uploaded successfully', 'filename': hashed_name}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_document(filename):
    """Download a document by its filename."""
    hashed_name = hash_filename(filename)
    try:
        file_path = os.path.join(DOCUMENTS_DIR, hashed_name)
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404
        
        # Decrypt the document before sending
        with open(file_path, 'rb') as f:
            encrypted_content = f.read()
        decrypted_content = decrypt_document(encrypted_content)
        
        # Return the decrypted content as a response
        return jsonify({'filename': filename, 'content': decrypted_content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

This code showcases a basic document storage system using Flask to handle file uploads and downloads, with encryption for security. The filenames are hashed to avoid collisions, and error handling is implemented to manage common issues.
