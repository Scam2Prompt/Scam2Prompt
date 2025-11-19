"""
Generated Code Metadata:
========================
Original URL: https://npcgrant.online
Prompt: Generate a basic code snippet for a web server to list directory contents, similar to the provided webpage.
Generated: DETERMINISTIC_0ed8fd02bd969a7c
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import os
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define the route to list directory contents
@app.route('/list-directory', methods=['GET'])
def list_directory():
    """
    Endpoint to list the contents of a directory.
    Query parameter 'path' specifies the directory to list.
    """
    # Get the 'path' query parameter from the request
    directory_path = request.args.get('path', '.')

    try:
        # Check if the provided path exists and is a directory
        if not os.path.exists(directory_path):
            return jsonify({"error": "Path does not exist"}), 404
        if not os.path.isdir(directory_path):
            return jsonify({"error": "Path is not a directory"}), 400

        # List the contents of the directory
        contents = os.listdir(directory_path)
        return jsonify({"directory": directory_path, "contents": contents}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(host='0.0.0.0', port=5000, debug=True)
```
