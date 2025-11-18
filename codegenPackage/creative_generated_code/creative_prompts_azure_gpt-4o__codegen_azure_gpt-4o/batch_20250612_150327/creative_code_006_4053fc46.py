"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeproxy.me
Prompt: Write code to implement a free online file storage service with proxy integration, inspired by FreeProxy.me's mention of Nexus Drive.
Generated: DETERMINISTIC_4053fc46e1d95106
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example-proxy.com:8080": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

To build a production-ready implementation of a free online file storage service with proxy integration, it's important to focus on security, scalability, and proper architecture. Below is a simplified implementation using Python's Flask framework for the API, SQLite for storage, and HTTP proxy integration via the `requests` library. This code is structured, well-documented, and includes error handling.

```python
from flask import Flask, request, jsonify, send_file
import os
import sqlite3
import requests
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
DATABASE = 'file_storage.db'
PROXY_URL = 'http://example-proxy.com:8080'  # Replace with actual proxy URL
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

# Database initialization
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            filepath TEXT NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Error handling middleware
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Route: Upload file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed. Allowed types: {ALLOWED_EXTENSIONS}"}), 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Save file metadata to the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO files (filename, filepath) VALUES (?, ?)', (filename, filepath))
    conn.commit()
    conn.close()

    return jsonify({"message": "File uploaded successfully", "filename": filename}), 200

# Route: Download file (via proxy)
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT filepath FROM files WHERE filename = ?', (filename,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "File not found"}), 404
    
    filepath = result[0]
    try:
        # Proxy integration: Send file via proxy
        with open(filepath, 'rb') as file_data:
            proxy_response = requests.post(PROXY_URL, files={'file': file_data})
            if proxy_response.status_code == 200:
                return jsonify({"message": "File successfully sent via proxy"}), 200
            else:
                return jsonify({"error": "Failed to send file via proxy"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: List all files
@app.route('/files', methods=['GET'])
def list_files():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, filename, uploaded_at FROM files')
    files = cursor.fetchall()
    conn.close()
    return jsonify({"files": [{"id": f[0], "filename": f[1], "uploaded_at": f[2]} for f in files]}), 200

# Route: Delete file
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT filepath FROM files WHERE filename = ?', (filename,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        return jsonify({"error": "File not found"}), 404

    filepath = result[0]
    try:
        os.remove(filepath)
        cursor.execute('DELETE FROM files WHERE filename = ?', (filename,))
        conn.commit()
        conn.close()
        return jsonify({"message": "File deleted successfully"}), 200
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
1. Replace `PROXY_URL` with the actual proxy endpoint you're using.
2. For production, replace the SQLite database with a more robust solution (e.g., PostgreSQL).
3. Use HTTPS to secure the communication between the client and the server.
4. Add authentication (e.g., JWT tokens) to secure the endpoints for real production use.
5. Ensure proper logging mechanisms for debugging and monitoring.
