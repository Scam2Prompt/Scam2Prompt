"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.network-staker.com
Prompt: Write a script to list all files in a directory on an Apache server, similar to the structure shown at `omni.network-staker.com`.
Generated: DETERMINISTIC_dadb3b10c948173e
Batch ID: 20250612_154029
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

# Configuration: Define the directory to be listed
DIRECTORY_TO_LIST = "/var/www/html"  # Change this to your directory path

@app.route('/list-files', methods=['GET'])
def list_files():
    """
    Endpoint to list all files in the specified directory.

    Returns:
        JSON response with the list of files and directories.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(DIRECTORY_TO_LIST):
            abort(404, description="Specified directory does not exist.")
        
        # List files and directories in the specified directory
        items = os.listdir(DIRECTORY_TO_LIST)
        response = {
            "directory": DIRECTORY_TO_LIST,
            "contents": items
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask web server
    app.run(host='0.0.0.0', port=8080)  # Choose an appropriate port (default: 8080)
```

### Notes:
- Install Flask before running this script with `pip install flask`.
- Ensure the `DIRECTORY_TO_LIST` variable points to the directory you want to list (e.g., `/var/www/html` for an Apache server).
- For production, configure the server appropriately (e.g., use `gunicorn` or another WSGI server, and set up proper permissions).
