"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Create a function that checks for the last modified date of files in a directory accessed via a web API.
Generated: DETERMINISTIC_4e7063fdcd93e83d
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_last_modified_dates(directory_path):
    """
    Get the last modified dates of all files in the specified directory.

    Args:
        directory_path (str): Path to the directory.

    Returns:
        dict: A dictionary where keys are filenames and values are last modified dates.
    """
    try:
        # Ensure the directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

        # Ensure the path is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a directory.")

        # Collect last modified dates for files in the directory
        file_dates = {}
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):  # Only process files
                last_modified_timestamp = os.path.getmtime(file_path)
                last_modified_date = datetime.fromtimestamp(last_modified_timestamp).isoformat()
                file_dates[filename] = last_modified_date

        return file_dates
    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

@app.route('/last-modified', methods=['GET'])
def last_modified_api():
    """
    API endpoint to get the last modified dates of files in a directory.

    Query Parameters:
        directory (str): Path to the directory.

    Returns:
        JSON response containing filenames and their last modified dates, or an error message.
    """
    try:
        # Get the directory path from query parameters
        directory_path = request.args.get('directory')
        if not directory_path:
            return jsonify({"error": "Missing 'directory' query parameter."}), 400

        # Get last modified dates
        result = get_last_modified_dates(directory_path)
        if "error" in result:
            return jsonify(result), 400

        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
