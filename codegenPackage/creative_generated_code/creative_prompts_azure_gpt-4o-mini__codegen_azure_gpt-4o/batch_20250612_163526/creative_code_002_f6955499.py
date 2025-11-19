"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Write a script to manage file indexing on a LiteSpeed web server, similar to the structure seen on perurest.com.
Generated: DETERMINISTIC_f6955499556f288a
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuration for the file indexing
BASE_DIRECTORY = '/var/www/html'  # Change this to your LiteSpeed web server's base directory
ALLOWED_EXTENSIONS = {'html', 'php', 'txt', 'css', 'js', 'jpg', 'png', 'gif'}

# Function to check allowed file extensions
def is_valid_extension(filename):
    """Check if the file has a permitted extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to index files in a directory
def index_files(directory):
    """
    Recursively index all files in the given directory.
    Args:
        directory (str): Path to the directory.

    Returns:
        list: List of files with their relative paths.
    """
    indexed_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if is_valid_extension(file):
                relative_path = os.path.relpath(os.path.join(root, file), BASE_DIRECTORY)
                indexed_files.append(relative_path)
    return indexed_files

@app.route('/index', methods=['GET'])
def get_indexed_files():
    """
    Endpoint to get a list of indexed files.
    Query Parameters:
        directory (str): Subdirectory to index (relative to BASE_DIRECTORY).

    Returns:
        JSON: Indexed files or an error message.
    """
    try:
        subdirectory = request.args.get('directory', '')
        target_directory = os.path.join(BASE_DIRECTORY, subdirectory)

        # Ensure the target directory exists
        if not os.path.exists(target_directory) or not os.path.isdir(target_directory):
            return jsonify({'error': 'Directory not found'}), 404

        # Index files and return as JSON
        files = index_files(target_directory)
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint for health checks.
    Returns:
        JSON: Status of the service.
    """
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    # Ensure the BASE_DIRECTORY exists
    if not os.path.exists(BASE_DIRECTORY):
        raise FileNotFoundError(f"The base directory '{BASE_DIRECTORY}' does not exist.")
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
