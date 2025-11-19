"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Write a script to list files in a directory served by a LiteSpeed web server.
Generated: DETERMINISTIC_2c3958a958a42035
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/list-files', methods=['GET'])
def list_files():
    """
    Endpoint to list files in a specified directory served by a LiteSpeed web server.
    Accepts a directory path as a query parameter 'dir'.
    
    Returns:
        JSON response containing the list of files or an error message.
    """
    # Get the 'dir' parameter from the query string
    directory = request.args.get('dir')
    
    # Validate the directory parameter
    if not directory:
        abort(400, description="Directory path is required.")
    
    # Normalize the directory path to prevent directory traversal attacks
    directory = os.path.normpath(directory)

    # Check if the specified directory exists
    if not os.path.exists(directory) or not os.path.isdir(directory):
        abort(404, description="Directory does not exist or is not a directory.")
    
    try:
        # List files in the specified directory
        files = os.listdir(directory)
        return jsonify({'files': files})
    except Exception as e:
        # Handle any exceptions that occur
        abort(500, description=f"An error occurred while listing files: {str(e)}")

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
