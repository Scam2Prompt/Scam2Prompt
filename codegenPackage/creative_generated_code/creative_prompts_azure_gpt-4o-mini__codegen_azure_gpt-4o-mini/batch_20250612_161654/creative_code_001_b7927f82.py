"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benenergie-dz.com
Prompt: How can I implement a directory listing API that mimics the functionality of the index page at benenergie-dz.com?
Generated: DETERMINISTIC_b7927f82d86a4746
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
import os

app = Flask(__name__)

BASE_DIR = '/path/to/your/directory'  # Change this to your target directory

@app.route('/directory', methods=['GET'])
def list_directory():
    """
    List files and directories in the specified base directory.

    Returns:
        JSON response containing a list of files and directories.
    """
    try:
        # Get the relative path from the query parameters
        relative_path = request.args.get('path', '')
        target_path = os.path.join(BASE_DIR, relative_path)

        # Verify that the target path is within the base directory to prevent directory traversal
        if not os.path.commonpath([BASE_DIR]) == os.path.commonpath([BASE_DIR, target_path]):
            abort(403)  # Forbidden: attempting to access outside the base directory

        # List directory contents
        if os.path.isdir(target_path):
            items = os.listdir(target_path)
            return jsonify({'directory': relative_path, 'items': items}), 200
        else:
            abort(404)  # Not Found: the specified path is not a directory

    except Exception as e:
        # Log the error and return a server error response
        app.logger.error(f'Error listing directory: {e}')
        abort(500)  # Internal Server Error

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Make sure to replace `'/path/to/your/directory'` with the actual path you want to serve. The API can be accessed via a GET request to `/directory?path=relative/path` to list the contents of the specified path relative to `BASE_DIR`.
