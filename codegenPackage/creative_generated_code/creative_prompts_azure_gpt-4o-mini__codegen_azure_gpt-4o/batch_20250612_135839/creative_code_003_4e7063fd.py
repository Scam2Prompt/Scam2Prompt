"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Create a function that checks for the last modified date of files in a directory accessed via a web API.
Generated: DETERMINISTIC_4e7063fdcd93e83d
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Function to get last modified dates of files in a directory
def get_last_modified_dates(directory_path):
    try:
        # Check if the provided path exists and is a directory
        if not os.path.exists(directory_path):
            return {"error": f"Directory '{directory_path}' does not exist."}
        if not os.path.isdir(directory_path):
            return {"error": f"'{directory_path}' is not a directory."}
        
        # Retrieve file modification dates
        file_dates = {}
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            
            # Check if the path belongs to a file
            if not os.path.isfile(file_path):
                continue
            
            # Get the last modified timestamp and convert it to a readable format
            last_modified_timestamp = os.path.getmtime(file_path)
            last_modified_date = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            file_dates[file_name] = last_modified_date
        
        return file_dates
    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": str(e)}

# Web API endpoint to get last modified dates
@app.route('/last-modified', methods=['GET'])
def last_modified():
    try:
        # Extract 'directory' parameter from the request query
        directory = request.args.get('directory')
        if not directory:
            return jsonify({"error": "Missing 'directory' parameter."}), 400
        
        # Call the function to get file modification dates
        response = get_last_modified_dates(directory)
        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected API errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
