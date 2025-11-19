"""
Generated Code Metadata:
========================
Original URL: https://stelax.io
Prompt: Create a simple API that mimics the directory listing functionality seen on stelax.io.
Generated: DETERMINISTIC_67bd43be48c46627
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, abort, request
import os
from pathlib import Path

app = Flask(__name__)

def get_directory_listing(path):
    """
    Returns a list of files and directories in the specified path.
    
    Args:
        path (str): The directory path to list.
        
    Returns:
        list: A list of dictionaries containing file/directory info.
    """
    try:
        entries = []
        for entry in os.scandir(path):
            entry_info = {
                'name': entry.name,
                'is_file': entry.is_file(),
                'is_dir': entry.is_dir(),
                'size': entry.stat().st_size if entry.is_file() else 0,
                'modified': entry.stat().st_mtime
            }
            entries.append(entry_info)
        return sorted(entries, key=lambda x: (not x['is_dir'], x['name'].lower()))
    except (PermissionError, FileNotFoundError) as e:
        raise e

@app.route('/list', methods=['GET'])
def list_directory():
    """
    API endpoint to list directory contents.
    
    Query Parameters:
        path (str): The directory path to list (relative to root).
        
    Returns:
        JSON: Directory listing or error message.
    """
    try:
        # Get path from query parameters
        rel_path = request.args.get('path', '').strip('/')
        
        # Security: Prevent directory traversal
        root_dir = Path.cwd() / 'data'  # Base directory
        abs_path = (root_dir / rel_path).resolve()
        
        # Verify the path is within the allowed directory
        if not abs_path.is_relative_to(root_dir):
            abort(403, description="Access denied")
            
        # Get directory listing
        entries = get_directory_listing(str(abs_path))
        
        # Convert to relative paths for the response
        for entry in entries:
            entry['path'] = str(Path(rel_path) / entry['name'])
            
        return jsonify({
            'path': rel_path,
            'contents': entries
        })
        
    except FileNotFoundError:
        abort(404, description="Directory not found")
    except PermissionError:
        abort(403, description="Permission denied")
    except Exception as e:
        app.logger.error(f"Error listing directory: {str(e)}")
        abort(500, description="Internal server error")

@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(e):
    """
    Error handler for API endpoints.
    """
    return jsonify({
        'error': e.description,
        'status_code': e.code
    }), e.code

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    data_dir = Path.cwd() / 'data'
    data_dir.mkdir(exist_ok=True)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
```
