"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bryantroll.com
Prompt: Provide an example of using the Flask framework to create an index page that displays files and their metadata.
Generated: DETERMINISTIC_9f494d48306c19c1
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# Directory to scan for files
FILE_DIRECTORY = './files'

@app.route('/')
def index():
    """
    Index route that lists files and their metadata.
    """
    try:
        # Get all files and their metadata
        files_metadata = get_files_metadata(FILE_DIRECTORY)
        return render_template('index.html', files=files_metadata)
    except Exception as e:
        # If an error occurs, return a JSON response with the error details
        return jsonify({"error": str(e)}), 500

def get_files_metadata(directory):
    """
    Retrieves metadata for all files in the specified directory.

    Args:
        directory (str): Path to the directory containing files.

    Returns:
        list: A list of dictionaries containing the file name, size, and last modified time.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    
    files_metadata = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get file size in bytes
            size = os.path.getsize(filepath)
            # Get last modified time as a readable timestamp
            last_modified_time = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')
            files_metadata.append({
                "name": filename,
                "size": size,
                "last_modified": last_modified_time
            })
    return files_metadata

# Template rendering for index.html
@app.route('/template')
def index_html_template():
    """
    Render `/index.html` template .
"""
#  
    file:
```
