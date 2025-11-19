"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bryantroll.com
Prompt: What libraries can I use to build a file index system similar to the one found on bryantroll.com?
Generated: DETERMINISTIC_b9561a8c564dd37b
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Define a class to represent a File Index
class FileIndex:
    def __init__(self, directory):
        """
        Initialize the FileIndex with a directory to index files from.
        """
        self.directory = directory
        self.index = self.build_index()

    def build_index(self):
        """
        Build an index of files in the specified directory.
        
        Returns:
            dict: A dictionary where the keys are file names and values are file paths.
        """
        index = {}
        try:
            for root, _, files in os.walk(self.directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    index[file] = file_path
        except Exception as e:
            print(f"Error while building index: {e}")
        return index

    def get_file_path(self, file_name):
        """
        Retrieve the file path for a given file name from the index.
        
        Args:
            file_name (str): The name of the file to look up.

        Returns:
            str: The path of the file.

        Raises:
            NotFound: If the file is not found in the index.
        """
        if file_name in self.index:
            return self.index[file_name]
        else:
            raise NotFound(f"File '{file_name}' not found in the index.")

# Initialize the FileIndex with the directory to be indexed
INDEX_DIRECTORY = '/path/to/your/files'  # Change to your target directory
file_index = FileIndex(INDEX_DIRECTORY)

@app.route('/files', methods=['GET'])
def list_files():
    """
    API endpoint to list all indexed files.
    
    Returns:
        JSON: A list of indexed file names.
    """
    return jsonify(list(file_index.index.keys())), 200

@app.route('/files/<file_name>', methods=['GET'])
def get_file(file_name):
    """
    API endpoint to retrieve the path of a specific file.
    
    Args:
        file_name (str): The name of the file to retrieve.

    Returns:
        JSON: The file path.
    
    Raises:
        NotFound: If the file is not found.
    """
    try:
        file_path = file_index.get_file_path(file_name)
        return jsonify({"file_name": file_name, "file_path": file_path}), 200
    except NotFound as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

This code creates a Flask web application that serves as a file index system, allowing users to list indexed files and retrieve their paths. Modify the `INDEX_DIRECTORY` variable to point to the directory you want to index. Make sure to install Flask and any dependencies required to run this code in your environment.
