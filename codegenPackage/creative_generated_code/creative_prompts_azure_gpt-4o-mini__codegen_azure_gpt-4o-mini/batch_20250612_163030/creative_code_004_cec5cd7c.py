"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulmagic.live
Prompt: What are the best practices for setting up permissions to avoid "403 Forbidden" errors in web development?
Generated: DETERMINISTIC_cec5cd7c868b19ed
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, abort, request

app = Flask(__name__)

# Define the path to the files or directories you want to serve
BASE_DIRECTORY = '/path/to/your/directory'

def is_file_accessible(file_path):
    """
    Check if the given file path is accessible for reading.
    
    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is accessible, False otherwise.
    """
    return os.path.isfile(file_path) and os.access(file_path, os.R_OK)

@app.route('/files/<path:filename>', methods=['GET'])
def serve_file(filename):
    """
    Serve a file from the server.

    Args:
        filename (str): The name of the file to serve.

    Returns:
        Response: The contents of the file if accessible, or a 403 error.
    """
    # Create the full file path
    file_path = os.path.join(BASE_DIRECTORY, filename)

    # Check if the file is accessible
    if not is_file_accessible(file_path):
        # Log the attempt to access a forbidden file
        app.logger.error(f'Access denied for: {file_path}')
        abort(403)  # Forbidden

    try:
        # Open and read the file
        with open(file_path, 'rb') as file:
            content = file.read()
            return content, 200  # Return the file contents
    except Exception as e:
        # Log any unexpected errors
        app.logger.error(f'Error accessing {file_path}: {e}')
        abort(500)  # Internal Server Error

if __name__ == '__main__':
    # Set the logging level
    app.logger.setLevel('DEBUG')
    
    # Start the Flask application
    app.run(debug=True)
```

### Important Notes:
- Change `/path/to/your/directory` to your actual file directory.
- Ensure you handle logging appropriately for your production environment.
- Use environment variables or configuration files to manage sensitive settings.
