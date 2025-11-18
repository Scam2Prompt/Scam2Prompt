"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Write a Python script to list all files and directories in a web server directory structure, similar to the one shown at https://360fuel.network.
Generated: DETERMINISTIC_b9301f944ae7facc
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify

app = Flask(__name__)

def list_directory(path):
    """
    Recursively lists all files and directories within the given path.
    
    Args:
        path (str): The root directory path to start listing files and directories.

    Returns:
        dict: A nested dictionary representing the directory structure.
    """
    try:
        # Dictionary to hold the directory structure
        directory_structure = {}
        
        # Iterate through files and directories at the given path
        for entry in os.scandir(path):
            if entry.is_dir():
                # Recursively list contents of subdirectories
                directory_structure[entry.name] = list_directory(entry.path)
            else:
                # List individual files
                directory_structure[entry.name] = "file"
        
        return directory_structure
    except Exception as e:
        # Handle errors gracefully and report them
        return {"error": f"Failed to scan directory '{path}': {str(e)}"}

@app.route('/list', methods=['GET'])
def list_web_server_directory():
    """
    Flask route to list the web server directory structure.

    Returns:
        Response: JSON representation of the directory structure.
    """
    # Define the path to the directory you want to scan
    root_directory = '.'

    # Generate the directory structure
    directory_structure = list_directory(root_directory)

    # Return the directory structure as a JSON response
    return jsonify(directory_structure)

if __name__ == '__main__':
    # Run the Flask server
    # Note: Set debug=True for development, but use debug=False in production
    app.run(host='0.0.0.0', port=5000, debug=False)
```
