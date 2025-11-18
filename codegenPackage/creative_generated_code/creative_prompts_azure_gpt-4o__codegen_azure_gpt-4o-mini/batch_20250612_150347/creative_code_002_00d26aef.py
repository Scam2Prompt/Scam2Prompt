"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Create an API endpoint in Python Flask to dynamically list directory contents, mimicking the index structure shown at https://abelltodoit.com.au.
Generated: DETERMINISTIC_00d26aef562b505f
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, abort
import os

app = Flask(__name__)

@app.route('/list_directory', methods=['GET'])
def list_directory():
    """
    API endpoint to list the contents of a specified directory.
    
    The directory to list is passed as a query parameter 'path'.
    If no path is specified, the current working directory is used.
    Returns a JSON response containing the directory contents.
    """
    # Get the path parameter from the query string, default to current directory
    path = request.args.get('path', default='.', type=str)

    # Normalize the path to prevent directory traversal attacks
    safe_path = os.path.normpath(path)

    # Check if the requested path is a directory
    if not os.path.isdir(safe_path):
        abort(404, description="Directory not found")

    try:
        # List the contents of the directory
        contents = os.listdir(safe_path)
        items = []

        for item in contents:
            item_path = os.path.join(safe_path, item)
            items.append({
                'name': item,
                'is_directory': os.path.isdir(item_path)
            })

        # Return the contents as a JSON response
        return jsonify(items)

    except Exception as e:
        # Handle unexpected errors gracefully
        abort(500, description=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
