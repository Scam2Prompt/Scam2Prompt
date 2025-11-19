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
# Import required libraries
from flask import Flask, jsonify
import os
import datetime

# Create a Flask application instance
app = Flask(__name__)

# Define a function to get file information
def get_file_info(directory):
    """
    Retrieves a list of files in a directory along with their last modified dates and sizes.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of dictionaries containing file information.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    file_info_list = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get file stats
            stats = os.stat(filepath)
            # Calculate file size in bytes
            file_size = stats.st_size
            # Convert file size to KB, MB, GB, etc.
            if file_size < 1024:
                file_size_str = f"{file_size} B"
            elif file_size < 1024**2:
                file_size_str = f"{file_size / 1024:.2f} KB"
            elif file_size < 1024**3:
                file_size_str = f"{file_size / 1024**2:.2f} MB"
            else:
                file_size_str = f"{file_size / 1024**3:.2f} GB"

            # Get last modified date
            modified_date = datetime.datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

            # Create a dictionary to store file information
            file_info = {
                "filename": filename,
                "modified_date": modified_date,
                "size": file_size_str
            }
            file_info_list.append(file_info)

    return file_info_list

# Define a route to retrieve file information
@app.route('/files', methods=['GET'])
def retrieve_files():
    directory = '.'  # Current working directory
    try:
        file_info_list = get_file_info(directory)
        return jsonify(file_info_list)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
