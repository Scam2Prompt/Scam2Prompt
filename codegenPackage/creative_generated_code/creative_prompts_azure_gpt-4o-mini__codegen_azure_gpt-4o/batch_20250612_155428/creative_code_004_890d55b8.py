"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idsmac-apple.com
Prompt: Create a script that mimics the functionality of a web server's index page by listing files and their attributes.
Generated: DETERMINISTIC_890d55b8cd8bb1b3
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

# Root directory for file listing
ROOT_DIRECTORY = os.getcwd()

@app.route('/')
def index():
    """
    Lists all files and directories in the root directory.
    Returns a JSON response with file/directory attributes.
    """
    try:
        files = []
        for item in os.listdir(ROOT_DIRECTORY):
            item_path = os.path.join(ROOT_DIRECTORY, item)
            files.append({
                'name': item,
                'type': 'directory' if os.path.isdir(item_path) else 'file',
                'size': os.path.getsize(item_path) if not os.path.isdir(item_path) else None,
                'last_modified': os.path.getmtime(item_path)
            })
        return jsonify(files)
    except Exception as e:
        # Handle any errors that occur during file listing
        return jsonify({'error': str(e)}), 500

@app.route('/<path:filename>')
def serve_file(filename):
    """
    Serves a specific file from the root directory.
    """
    try:
        return send_from_directory(ROOT_DIRECTORY, filename)
    except FileNotFoundError:
        # Handle case where the requested file does not exist
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        # Handle other errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
