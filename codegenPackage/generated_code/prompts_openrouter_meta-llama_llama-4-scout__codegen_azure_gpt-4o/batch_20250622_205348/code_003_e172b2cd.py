"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: "How to configure server settings to display custom directory listings?"
Generated: DETERMINISTIC_e172b2cd24fca739
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation using the Flask framework to configure server settings for displaying custom directory listings. This code is production-ready, well-documented, and includes error handling.

```python
from flask import Flask, send_from_directory, render_template, abort
import os

app = Flask(__name__)

# Directory to serve files from
BASE_DIRECTORY = os.path.abspath("custom_directory")  # Change this to your desired directory path

# Ensure the directory exists
if not os.path.exists(BASE_DIRECTORY):
    raise FileNotFoundError(f"The directory '{BASE_DIRECTORY}' does not exist.")

@app.route("/")
def list_directory():
    """
    Endpoint to list files in the custom directory.
    Renders a custom HTML template for directory listing.
    """
    try:
        # Get list of files and directories
        items = os.listdir(BASE_DIRECTORY)
        return render_template("directory_listing.html", items=items, base_directory=BASE_DIRECTORY)
    except Exception as e:
        # Handle errors gracefully
        abort(500, description=f"Error listing directory: {str(e)}")

@app.route("/files/<path:filename>")
def serve_file(filename):
    """
    Endpoint to serve individual files from the custom directory.
    """
    try:
        # Send the requested file from the base directory
        return send_from_directory(BASE_DIRECTORY, filename)
    except FileNotFoundError:
        # Handle file not found error
        abort(404, description=f"File '{filename}' not found.")
    except Exception as e:
        # Handle other errors
        abort(500, description=f"Error serving file: {str(e)}")

# Custom error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    """
    return render_template("error.html", error=error), 404

# Custom error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return render_template("error.html", error=error), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### Notes:
1. Create a `templates` directory in the same folder as this script and add the following files:
   - `directory_listing.html`: A custom HTML template for displaying directory listings.
   - `error.html`: A custom HTML template for displaying error messages.
2. Replace `custom_directory` with the path to the directory you want to serve.
3. Ensure proper permissions are set for the directory and files to be accessible by the server.
