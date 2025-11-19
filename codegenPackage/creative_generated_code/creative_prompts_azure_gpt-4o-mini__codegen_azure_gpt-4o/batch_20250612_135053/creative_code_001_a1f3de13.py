"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: What API can I use to create an index of files on a web server like the one at elisium.it?
Generated: DETERMINISTIC_a1f3de137b28228c
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script uses Flask to create an index of files on a web server.
It lists all files in a specified directory on the server and provides a simple
HTTP interface to view the file index. Ensure Flask is installed via `pip install flask`.

Production-ready notes:
- Use a web server like Gunicorn for deployment.
- Restrict access to sensitive directories.
- Properly configure logging and security for production use.
"""

import os
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Directory to index files from (modify according to your needs)
INDEX_DIRECTORY = "/path/to/your/files"

@app.route('/files', methods=['GET'])
def list_files():
    """
    Endpoint to list all files in the specified directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(INDEX_DIRECTORY):
            abort(404, description="Directory not found.")

        # Walk through the directory and gather file names
        files = []
        for root, _, file_names in os.walk(INDEX_DIRECTORY):
            for file_name in file_names:
                # Construct relative file path
                relative_path = os.path.relpath(os.path.join(root, file_name), INDEX_DIRECTORY)
                files.append(relative_path)

        # Return the list of files in JSON format
        return jsonify({"files": files})

    except Exception as e:
        # Catch unexpected errors
        abort(500, description=f"An unexpected error occurred: {str(e)}")

@app.errorhandler(404)
def not_found_error(e):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": str(e)}), 404

@app.errorhandler(500)
def internal_error(e):
    """
    Handle internal server errors gracefully.
    """
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    """
    Entry point for running the Flask application.
    """
    # Run the Flask development server (use Gunicorn/WSGI server in production)
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Notes:
- Replace `/path/to/your/files` with the actual directory you want to index.
- Ensure the directory has appropriate permissions to be accessed by the server.
- In production, disable `debug=True` and use a WSGI server like Gunicorn.
