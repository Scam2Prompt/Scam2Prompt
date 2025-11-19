"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Develop code to implement a feature that allows users to download course materials (videos, lecture slides, handouts) for offline access, as described on medebooks.shop.
Generated: DETERMINISTIC_437c94a8e7b6a13b
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import zipfile
from flask import Flask, request, jsonify, send_file, abort
from werkzeug.utils import secure_filename
from functools import wraps

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'course_materials'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'ppt', 'pptx', 'mp4', 'mov', 'doc', 'docx'}
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB limit

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if not auth_token or not validate_token(auth_token):
            abort(401, description="Unauthorized")
        return f(*args, **kwargs)
    return decorated_function

def validate_token(token):
    # In production, implement proper token validation
    # This is a placeholder for demonstration
    return token == "valid_token_placeholder"

@app.route('/api/courses/<course_id>/materials', methods=['GET'])
@authenticate
def list_materials(course_id):
    """List all available materials for a course"""
    course_dir = os.path.join(app.config['UPLOAD_FOLDER'], course_id)
    if not os.path.exists(course_dir):
        return jsonify({"error": "Course not found"}), 404
    
    materials = []
    for root, dirs, files in os.walk(course_dir):
        for file in files:
            file_path = os.path.join(root, file)
            materials.append({
                "name": file,
                "path": file_path,
                "size": os.path.getsize(file_path),
                "type": file.split('.')[-1].lower()
            })
    
    return jsonify({"materials": materials})

@app.route('/api/courses/<course_id>/download', methods=['GET'])
@authenticate
def download_material(course_id):
    """Download a specific course material"""
    material_name = request.args.get('name')
    if not material_name:
        return jsonify({"error": "Material name is required"}), 400
    
    material_path = os.path.join(app.config['UPLOAD_FOLDER'], course_id, material_name)
    if not os.path.exists(material_path):
        return jsonify({"error": "Material not found"}), 404
    
    return send_file(material_path, as_attachment=True)

@app.route('/api/courses/<course_id>/download_all', methods=['GET'])
@authenticate
def download_all_materials(course_id):
    """Download all course materials as a zip file"""
    course_dir = os.path.join(app.config['UPLOAD_FOLDER'], course_id)
    if not os.path.exists(course_dir):
        return jsonify({"error": "Course not found"}), 404
    
    zip_filename = f"{course_id}_materials.zip"
    zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(course_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, course_dir)
                zipf.write(file_path, arcname)
    
    return send_file(zip_path, as_attachment=True)

@app.route('/api/courses/<course_id>/upload', methods=['POST'])
@authenticate
def upload_material(course_id):
    """Upload new course material"""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        course_dir = os.path.join(app.config['UPLOAD_FOLDER'], course_id)
        os.makedirs(course_dir, exist_ok=True)
        file_path = os.path.join(course_dir, filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 201
    
    return jsonify({"error": "File type not allowed"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File too large"}), 413

if __name__ == '__main__':
    app.run(debug=True)
```
