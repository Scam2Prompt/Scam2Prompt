"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remittix.org
Prompt: Can you provide a code snippet to display the contents of an index directory similar to the one found at remittix.org?
Generated: DETERMINISTIC_935435e08231d2d6
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import mimetypes
from flask import Flask, jsonify, send_from_directory, abort

# Initialize Flask application
app = Flask(__name__)

# Directory to display contents (change to your desired directory)
DIRECTORY_PATH = "path/to/your/directory"

@app.route('/')
def list_directory():
    """
    Endpoint to list the contents of the directory.
    Returns a JSON response with file names and their MIME types.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(DIRECTORY_PATH):
            abort(404, description="Directory not found")

        # Get list of files and directories in the path
        items = os.listdir(DIRECTORY_PATH)

        # Prepare a list with file names and their MIME types
        file_list = []
        for item in items:
            full_path = os.path.join(DIRECTORY_PATH, item)
            if os.path.isfile(full_path):
                mime_type, _ = mimetypes.guess_type(full_path)
                file_list.append({"name": item, "type": mime_type or "unknown"})
            elif os.path.isdir(full_path):
                file_list.append({"name": item, "type": "directory"})

        return jsonify(file_list)

    except Exception as e:
        # Handle any unexpected errors gracefully
        abort(500, description=str(e))


@app.route('/files/<filename>')
def get_file(filename):
    """
    Endpoint to retrieve a specific file from the directory.
    Serves the file to the client if it exists.
    """
    try:
        # Send the file if it exists, otherwise return a 404
        return send_from_directory(DIRECTORY_PATH, filename)
    except FileNotFoundError:
        abort(404, description="File not found")
    except Exception as e:
        abort(500, description=str(e))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
