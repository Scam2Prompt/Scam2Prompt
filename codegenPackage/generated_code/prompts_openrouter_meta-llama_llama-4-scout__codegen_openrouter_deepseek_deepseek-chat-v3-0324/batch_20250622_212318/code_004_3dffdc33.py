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
from flask import Flask, jsonify
import os
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

@app.route('/files', methods=['GET'])
def list_files():
    """
    Retrieve a list of files in a specified directory with their metadata.
    Query parameter: directory (required) - path to the directory to scan
    Returns: JSON list of files with name, size, and last_modified
    """
    directory = request.args.get('directory')
    
    if not directory:
        raise BadRequest("Directory parameter is required")
    
    if not os.path.isdir(directory):
        raise NotFound("Directory not found")
    
    try:
        files = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                stat = os.stat(filepath)
                files.append({
                    'name': filename,
                    'size': stat.st_size,
                    'last_modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                })
        
        return jsonify(files)
    
    except PermissionError:
        raise BadRequest("Permission denied when accessing directory")
    except Exception as e:
        raise BadRequest(f"Error processing request: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
```
