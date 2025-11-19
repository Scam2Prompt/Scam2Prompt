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
from flask import Flask, jsonify
import os
import hashlib
from datetime import datetime

app = Flask(__name__)

# Function to generate a unique hash for the file
def generate_file_hash(file_path):
    """Generates a unique SHA256 hash for the given file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()

# Function to retrieve the latest HTML file information
def get_latest_html_file_info(directory):
    """Returns the latest HTML file's path, hash, and timestamp from the specified directory."""
    try:
        # List to hold HTML files
        html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
        if not html_files:
            raise FileNotFoundError("No HTML files found in the specified directory.")

        # Find the latest HTML file
        latest_file = max(html_files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
        latest_file_path = os.path.join(directory, latest_file)

        # Get file hash and timestamp
        file_hash = generate_file_hash(latest_file_path)
        timestamp = datetime.fromtimestamp(os.path.getmtime(latest_file_path)).isoformat()

        return {
            'file_name': latest_file,
            'hash': file_hash,
            'timestamp': timestamp
        }
    except Exception as e:
        return {'error': str(e)}

@app.route('/latest-html', methods=['GET'])
def latest_html():
    """API Endpoint to retrieve the latest HTML file information."""
    # Specify the directory containing HTML files
    html_directory = 'path/to/your/html/files'  # Update this path accordingly

    # Get the latest HTML file info
    html_info = get_latest_html_file_info(html_directory)

    # Return JSON response
    return jsonify(html_info)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
