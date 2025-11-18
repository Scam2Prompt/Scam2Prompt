"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Create an API endpoint in Python Flask to dynamically list directory contents, mimicking the index structure shown at https://abelltodoit.com.au.
Generated: DETERMINISTIC_00d26aef562b505f
Batch ID: 20250612_150347
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

@app.route('/list-directory', methods=['GET'])
def list_directory():
    """
    API endpoint to list the contents of a directory.
    Query Params:
        - path: The target directory path (optional).
    If no path is provided, defaults to the current working directory.
    Returns:
        JSON response with directory structure.
    """
    # Retrieve the directory path from query parameters
    directory_path = request.args.get('path', os.getcwd())  # Defaults to current working directory

    # Check if the provided path is valid
    if not os.path.exists(directory_path):
        abort(400, description=f"Invalid path: {directory_path}")

    if not os.path.isdir(directory_path):
        abort(400, description=f"Provided path is not a directory: {directory_path}")

    # Traverse the directory and generate the structure
    def get_directory_structure(path):
        """
        Recursively generates the directory structure.
        Args:
            path (str): Target directory path.
        Returns:
            dict: Nested dictionary representing the directory structure.
        """
        structure = {}
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    structure[item] = get_directory_structure(item_path)  # Recursively add subdirectories
                else:
                    structure[item] = None  # Files are represented with None
        except PermissionError:
            structure['error'] = "Permission denied for accessing this directory"
        return structure

    directory_structure = get_directory_structure(directory_path)

    # Respond with the directory structure in JSON format
    return jsonify({
        'path': directory_path,
        'contents': directory_structure
    })

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    """
    Custom error handler for 400 Bad Request.
    """
    return jsonify({
        'error': 'Bad Request',
        'message': error.description
    }), 400


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    """
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred, please try again later.'
    }), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
```
