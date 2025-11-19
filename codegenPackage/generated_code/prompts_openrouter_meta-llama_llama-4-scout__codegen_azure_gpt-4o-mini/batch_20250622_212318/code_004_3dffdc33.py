"""
Generated Code Metadata:
========================
Original URL: https://murtilla.cl
Prompt: Create a RESTful API using Flask to retrieve a list of files in a directory along with their last modified dates and sizes.
Generated: DETERMINISTIC_3dffdc33a2b31120
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# Define the directory to list files from
DIRECTORY_PATH = '/path/to/your/directory'  # Change this to your target directory

@app.route('/files', methods=['GET'])
def list_files():
    """
    Retrieve a list of files in the specified directory along with their
    last modified dates and sizes.

    Returns:
        JSON response containing a list of files with their details.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(DIRECTORY_PATH):
            return jsonify({"error": "Directory not found"}), 404

        # List to hold file details
        files_list = []

        # Iterate over the files in the directory
        for filename in os.listdir(DIRECTORY_PATH):
            file_path = os.path.join(DIRECTORY_PATH, filename)
            if os.path.isfile(file_path):  # Ensure it's a file
                # Get file details
                file_info = {
                    "name": filename,
                    "size": os.path.getsize(file_path),  # Size in bytes
                    "last_modified": datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
                }
                files_list.append(file_info)

        return jsonify(files_list), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```
