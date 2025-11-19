"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Develop a RESTful API specification for a service that supports artists in uploading and managing their digital content, inspired by the comprehensive management services provided by VIP Management.
Generated: DETERMINISTIC_75b028d658e9b72d
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file storage
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to validate file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Endpoint: Health Check
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify API status.
    """
    return jsonify({"status": "API is running"}), 200

# Endpoint: Upload Content
@app.route('/api/content/upload', methods=['POST'])
def upload_content():
    """
    Endpoint to upload digital content.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 201
    
    return jsonify({"error": f"Invalid file type. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

# Endpoint: List Uploaded Content
@app.route('/api/content', methods=['GET'])
def list_content():
    """
    Endpoint to list all uploaded digital content.
    """
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Delete Content
@app.route('/api/content/<filename>', methods=['DELETE'])
def delete_content(filename):
    """
    Endpoint to delete a specific file.
    """
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(file_path):
            os.remove(file_path)
            return jsonify({"message": f"File '{filename}' deleted successfully"}), 200
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Artist Information (Example for extensibility)
@app.route('/api/artists/<artist_id>', methods=['GET'])
def get_artist_info(artist_id):
    """
    Endpoint to retrieve artist information. 
    For now, this endpoint returns mock data.
    """
    mock_artist_data = {
        "artist_id": artist_id,
        "name": "John Doe",
        "genres": ["Pop", "Jazz"],
        "bio": "An up-and-coming artist with a passion for digital creativity."
    }
    return jsonify(mock_artist_data), 200

# Error handling for invalid endpoints
@app.errorhandler(404)
def page_not_found(error):
    """
    Error handler for invalid routes.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
