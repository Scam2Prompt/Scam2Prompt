"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrollnetwork.ngv.com.ec
Prompt: Write code to list all files and directories from a server directory view similar to the one at https://scrollnetwork.ngv.com.ec using Python.
Generated: DETERMINISTIC_de390f4e3cbcb6ca
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Directory path that will be listed
SERVER_DIRECTORY = "/path/to/your/directory"

@app.route('/list-directory', methods=['GET'])
def list_directory():
    """
    Endpoint to list all files and directories in a server directory.
    Returns a JSON response with the structure:
    {
        "directories": [...],
        "files": [...]
    }
    """
    try:
        # Validate the server directory exists
        if not os.path.exists(SERVER_DIRECTORY):
            abort(404, description="Directory not found.")

        # List files and directories
        items = os.listdir(SERVER_DIRECTORY)
        directories = [item for item in items if os.path.isdir(os.path.join(SERVER_DIRECTORY, item))]
        files = [item for item in items if os.path.isfile(os.path.join(SERVER_DIRECTORY, item))]

        return jsonify({
            "directories": directories,
            "files": files
        })
    except Exception as e:
        # Catch and log unexpected errors
        abort(500, description=f"An error occurred: {str(e)}")


@app.errorhandler(404)
def resource_not_found(e):
    """Handles 404 errors."""
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handles 500 errors."""
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
