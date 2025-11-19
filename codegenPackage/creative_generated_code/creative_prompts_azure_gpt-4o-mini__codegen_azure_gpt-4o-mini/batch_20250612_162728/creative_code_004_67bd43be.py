"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelax.io
Prompt: Create a simple API that mimics the directory listing functionality seen on stelax.io.
Generated: DETERMINISTIC_67bd43be48c46627
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Set the base directory for listing files
BASE_DIRECTORY = "."

# Helper function to list files and directories
def list_directory(path):
    try:
        # List all entries in the given directory
        entries = os.listdir(path)
        return entries
    except PermissionError:
        # Handle permission errors
        return None
    except FileNotFoundError:
        # Handle case where the directory does not exist
        return None

@app.route('/api/list', methods=['GET'])
def get_directory_listing():
    """
    Endpoint to list files and directories in the specified path.
    Defaults to the base directory if no path is provided.
    """
    # Get the 'path' parameter from the query string
    path = request.args.get('path', BASE_DIRECTORY)

    # Normalize the path to prevent directory traversal attacks
    normalized_path = os.path.normpath(os.path.join(BASE_DIRECTORY, path))

    # Ensure the normalized path starts with the base directory
    if not normalized_path.startswith(os.path.abspath(BASE_DIRECTORY)):
        return jsonify({"error": "Invalid path"}), 400

    # List the directory contents
    entries = list_directory(normalized_path)

    # Handle cases when the directory is not accessible or does not exist
    if entries is None:
        return jsonify({"error": "Cannot access the directory"}), 403

    # Return the directory listing as JSON
    return jsonify({"directory": normalized_path, "contents": entries}), 200

if __name__ == '__main__':
    # Start the Flask web server
    app.run(host='0.0.0.0', port=5000)
```
