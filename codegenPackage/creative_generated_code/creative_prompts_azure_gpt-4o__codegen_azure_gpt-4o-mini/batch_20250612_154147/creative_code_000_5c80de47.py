"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abset.org
Prompt: Write a script to list all files in a directory served by an Apache server, including their last modified date and size, similar to the directory listing at https://abset.org.
Generated: DETERMINISTIC_5c80de47b6718201
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route('/list-files/<path:directory>', methods=['GET'])
def list_files(directory):
    """
    Lists all files in the specified directory served by the Apache server,
    including their last modified date and size.

    Args:
        directory (str): The path to the directory to list files from.

    Returns:
        JSON: A list of files with their names, size, and last modified date.
    """
    # Ensure the directory is safe and exists
    if not os.path.exists(directory) or not os.path.isdir(directory):
        return jsonify({"error": "Directory not found"}), 404

    try:
        files_info = []
        # List all files in the given directory
        for entry in os.listdir(directory):
            file_path = os.path.join(directory, entry)
            # Only process files, skip directories
            if os.path.isfile(file_path):
                file_stats = os.stat(file_path)
                files_info.append({
                    "name": entry,
                    "size": file_stats.st_size,  # Size in bytes
                    "last_modified": datetime.datetime.fromtimestamp(file_stats.st_mtime).isoformat()
                })

        return jsonify(files_info), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    """
    Renders the home page with basic instructions.
    """
    return render_template_string('''
        <h1>File Listing Service</h1>
        <p>Use the endpoint <code>/list-files/<path:directory></code> to list files in a directory.</p>
        <p>Example: <code>/list-files/path/to/directory</code></p>
    ''')

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Note**: Ensure you have Flask installed (`pip install Flask`) to run this script. Adjust the directory path and the server configurations as needed for production deployment.
