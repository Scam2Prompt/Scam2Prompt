"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Create an API endpoint that returns the latest HTML file information, including its unique hash and timestamp.
Generated: DETERMINISTIC_f8554849cfa3bed4
Batch ID: 20250612_161520
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
import hashlib
import time

app = Flask(__name__)

# Constants
HTML_FILES_DIRECTORY = "html_files"  # Directory containing HTML files

def get_latest_html_file_info(directory):
    """
    Retrieves the latest HTML file in the specified directory,
    calculates its hash, and returns its metadata.
    """
    try:
        # Get a list of all .html files in the directory
        files = [f for f in os.listdir(directory) if f.endswith('.html')]
        
        if not files:
            return None  # No HTML files found

        # Find the latest modified file
        latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
        latest_file_path = os.path.join(directory, latest_file)

        # Calculate the file's hash (SHA-256)
        with open(latest_file_path, 'rb') as f:
            file_data = f.read()
            file_hash = hashlib.sha256(file_data).hexdigest()

        # Get the last modified timestamp
        timestamp = os.path.getmtime(latest_file_path)

        return {
            "file_name": latest_file,
            "file_hash": file_hash,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        }
    except Exception as e:
        # Log error (optional)
        print(f"Error retrieving latest HTML file: {e}")
        return None

@app.route('/latest-html', methods=['GET'])
def latest_html_endpoint():
    """
    API endpoint to retrieve the latest HTML file information.
    Returns file name, unique hash, and timestamp of the latest HTML file.
    """
    file_info = get_latest_html_file_info(HTML_FILES_DIRECTORY)
    
    if file_info is None:
        return jsonify({"error": "No HTML files found or an error occurred."}), 404

    return jsonify(file_info), 200

if __name__ == '__main__':
    # Ensure the HTML files directory exists
    if not os.path.exists(HTML_FILES_DIRECTORY):
        os.makedirs(HTML_FILES_DIRECTORY)

    # Run the Flask app
    app.run(debug=True)
```
