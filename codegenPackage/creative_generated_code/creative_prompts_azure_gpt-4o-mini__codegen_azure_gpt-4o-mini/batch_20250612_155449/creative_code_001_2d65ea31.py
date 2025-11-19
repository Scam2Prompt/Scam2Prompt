"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.world
Prompt: "How can I create an API endpoint that returns a directory listing like the one found at https://symbioticfi.world?"
Generated: DETERMINISTIC_2d65ea31a5765134
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, send_from_directory, abort
import os

app = Flask(__name__)

# Set the directory to list files from
DIRECTORY_TO_LIST = 'your_directory_path_here'  # Change this to your desired directory

@app.route('/api/directory', methods=['GET'])
def list_directory():
    """
    API endpoint to list the files in the specified directory.

    Returns:
        JSON response with a list of files and directories.
        If the directory does not exist, returns a 404 error.
    """
    if not os.path.exists(DIRECTORY_TO_LIST):
        abort(404, description="Directory not found")

    try:
        # List all files and directories in the specified path
        items = os.listdir(DIRECTORY_TO_LIST)
        files = [{
            'name': item,
            'path': os.path.join(DIRECTORY_TO_LIST, item),
            'is_directory': os.path.isdir(os.path.join(DIRECTORY_TO_LIST, item))
        } for item in items]

        return jsonify(files), 200

    except OSError as e:
        # Handle any OS-related errors (e.g., permissions issues)
        abort(500, description=str(e))

@app.route('/api/directory/<path:filename>', methods=['GET'])
def serve_file(filename):
    """
    API endpoint to serve a file from the specified directory.

    Args:
        filename (str): The name of the file to serve.

    Returns:
        The file response if found, otherwise a 404 error.
    """
    try:
        return send_from_directory(DIRECTORY_TO_LIST, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, description="File not found")
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    # Run the application on the default port 5000
    app.run(debug=True)
```

Make sure to replace `'your_directory_path_here'` with the actual path of the directory you want to list.
