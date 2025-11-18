"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: Write a Python Flask application that serves a directory listing similar to the one shown on https://initia.org.in.
Generated: DETERMINISTIC_340a4d01955c6770
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, send_from_directory, jsonify, request
import os

app = Flask(__name__)

# The directory to serve files from - change this to the desired directory path
SERVE_DIRECTORY = os.path.abspath("your_directory_path_here")

@app.route("/")
def home():
    """
    Home route that displays a simple message.
    """
    return "Welcome to the Directory Listing App!"

@app.route("/list", methods=["GET"])
def list_directory():
    """
    API route to list the contents of a directory.
    Returns a JSON response containing files and directories.
    """
    try:
        # Fetch the contents of the directory
        contents = os.listdir(SERVE_DIRECTORY)
        # Separate files and directories
        files = [item for item in contents if os.path.isfile(os.path.join(SERVE_DIRECTORY, item))]
        directories = [item for item in contents if os.path.isdir(os.path.join(SERVE_DIRECTORY, item))]
        
        # Return JSON response
        return jsonify({
            "success": True,
            "files": files,
            "directories": directories
        })
    except Exception as e:
        # Handle errors gracefully
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/download/<path:filename>", methods=["GET"])
def download_file(filename):
    """
    API route to download a specific file.
    Handles missing files and errors gracefully.
    """
    try:
        # Send the requested file from the directory
        return send_from_directory(SERVE_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        # Handle file not found error
        return jsonify({
            "success": False,
            "error": f"File '{filename}' not found."
        }), 404
    except Exception as e:
        # Handle other errors
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    # Ensure the directory exists
    if not os.path.exists(SERVE_DIRECTORY):
        raise RuntimeError(f"Configured directory '{SERVE_DIRECTORY}' does not exist. Please update the path.")
    
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. Replace `"your_directory_path_here"` with the absolute path to the directory you want to serve.
2. This code assumes you have Flask installed (`pip install flask`).
