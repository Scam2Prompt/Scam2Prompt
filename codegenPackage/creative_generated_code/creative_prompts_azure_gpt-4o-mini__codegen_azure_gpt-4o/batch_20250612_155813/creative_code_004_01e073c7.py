"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miles.plumenetworke.com
Prompt: Write a script to list files in a directory on an Apache server, similar to the index at miles.plumenetworke.com.
Generated: DETERMINISTIC_01e073c797a102bd
Batch ID: 20250612_155813
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

# Configuration: Specify the directory to list files from
DIRECTORY_TO_LIST = '/var/www/html'  # Change this to the desired directory path

@app.route('/list-files', methods=['GET'])
def list_files():
    """
    Endpoint to list files in the specified directory.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(DIRECTORY_TO_LIST):
            abort(404, description="Directory does not exist.")

        # Get a list of files and directories in the specified directory
        items = os.listdir(DIRECTORY_TO_LIST)

        # Prepare the response as a JSON object
        response = {
            'directory': DIRECTORY_TO_LIST,
            'files': items
        }

        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({'error': error.description}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=8080)  # Change port if needed
```

This script uses Flask to create a simple web server that lists the files in a directory. Save this script to a file, install Flask (`pip install flask`), and run it. You can access the file listing at `http://<your-server>:8080/list-files`.
