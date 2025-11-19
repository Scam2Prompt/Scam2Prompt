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
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Base directory to list files and directories
BASE_DIRECTORY = "/path/to/your/base/directory"  # Change this to your target directory

@app.route('/directory', methods=['GET'])
def list_directory():
    """
    API Endpoint to list files and directories in the specified directory.
    Mimics functionality similar to an index page of a directory.
    Query Parameters:
      - path: (optional) Relative path from the base directory to list.
    Returns:
      - JSON response containing the list of files and directories.
    """
    # Get the 'path' query parameter from the request
    relative_path = request.args.get('path', '')

    # Construct the absolute path
    directory_path = os.path.join(BASE_DIRECTORY, relative_path)

    try:
        # Validate if directory exists
        if not os.path.exists(directory_path):
            return jsonify({"error": "Directory not found"}), 404

        # Validate if the path is indeed a directory
        if not os.path.isdir(directory_path):
            return jsonify({"error": "Path is not a directory"}), 400

        # List files and directories in the specified path
        entries = os.listdir(directory_path)
        response = []
        for entry in entries:
            entry_path = os.path.join(directory_path, entry)
            response.append({
                "name": entry,
                "type": "directory" if os.path.isdir(entry_path) else "file",
                "size": os.path.getsize(entry_path) if os.path.isfile(entry_path) else None
            })

        return jsonify(response)

    except Exception as e:
        # Return a generic error message in case of an unexpected issue
        return jsonify({"error": "An error occurred while listing the directory", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- Replace `/path/to/your/base/directory` with the actual path to the directory you want to serve.
- This code uses Flask as the web framework. Install it by running `pip install flask`.
- Ensure proper permissions for accessing the specified directory.
