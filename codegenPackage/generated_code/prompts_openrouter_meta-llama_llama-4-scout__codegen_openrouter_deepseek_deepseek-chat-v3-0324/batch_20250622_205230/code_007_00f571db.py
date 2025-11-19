"""
Generated Code Metadata:
========================
Original URL: https://vsdlkvsl.sbs
Prompt: Design an API for a browser-based file manager, allowing users to upload, download, and manage files securely, and incorporating features similar to those discussed in the context of ES File Explorer on this webpage.
Generated: DETERMINISTIC_00f571dbf28495c7
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
File Manager API for browser-based file operations.
Supports secure upload, download, and file management.
"""

from flask import Flask, request, jsonify, send_file, abort
from werkzeug.utils import secure_filename
import os
import uuid
import hashlib
from functools import wraps
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx'}

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_file_hash(content):
    return hashlib.sha256(content).hexdigest()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token.split()[1], app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated

# API Routes
@app.route('/api/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401
    
    # In a real app, verify username/password against database
    if auth.username == 'admin' and auth.password == 'password':
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'message': 'Could not verify'}), 401

@app.route('/api/files', methods=['GET'])
@token_required
def list_files():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(path):
            files.append({
                'name': filename,
                'size': os.path.getsize(path),
                'modified': datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
            })
    return jsonify({'files': files})

@app.route('/api/files/upload', methods=['POST'])
@token_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Handle duplicate files
        if os.path.exists(filepath):
            base, ext = os.path.splitext(filename)
            filename = f"{base}_{uuid.uuid4().hex[:8]}{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(filepath)
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'filehash': generate_file_hash(open(filepath, 'rb').read())
        }), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/api/files/download/<filename>', methods=['GET'])
@token_required
def download_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    return send_file(filepath, as_attachment=True)

@app.route('/api/files/delete/<filename>', methods=['DELETE'])
@token_required
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        os.remove(filepath)
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/files/rename', methods=['POST'])
@token_required
def rename_file():
    data = request.get_json()
    if not data or 'old_name' not in data or 'new_name' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    
    old_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(data['old_name']))
    new_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(data['new_name']))
    
    if not os.path.exists(old_path):
        return jsonify({'error': 'File not found'}), 404
    
    if os.path.exists(new_path):
        return jsonify({'error': 'New filename already exists'}), 400
    
    try:
        os.rename(old_path, new_path)
        return jsonify({'message': 'File renamed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File too large'}), 413

if __name__ == '__main__':
    app.run(debug=True)
```
