"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Suggest a method to secure a public directory listing, like the one on https://refconegypt.net, using server-side configurations or scripts.
Generated: DETERMINISTIC_da827fef99a76e32
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, abort, send_from_directory

app = Flask(__name__)

# Configuration: Set the path to the public directory
PUBLIC_DIRECTORY = '/path/to/public/directory'

# Ensure the public directory exists
if not os.path.exists(PUBLIC_DIRECTORY):
    raise FileNotFoundError(f"The public directory {PUBLIC_DIRECTORY} does not exist.")

@app.route('/files/<path:filename>', methods=['GET'])
def secure_listing(filename):
    """
    Serve a file from the public directory with security checks.
    
    Args:
        filename (str): The name of the file to retrieve.
    
    Returns:
        A file response from the server if found, otherwise a 404 error.
    """
    # Check for directory traversal attempts
    if '..' in filename or filename.startswith('/'):
        abort(403)  # Forbidden access

    # Securely serve the requested file if it exists
    try:
        return send_from_directory(PUBLIC_DIRECTORY, filename)
    except FileNotFoundError:
        abort(404)  # File not found

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Replace `'/path/to/public/directory'` with the actual path to your directory.
- This code utilizes Flask for serving files securely.
- Error handling is included for file access and directory traversal attempts.
- Ensure you have Flask installed (`pip install Flask`) before running the application.
