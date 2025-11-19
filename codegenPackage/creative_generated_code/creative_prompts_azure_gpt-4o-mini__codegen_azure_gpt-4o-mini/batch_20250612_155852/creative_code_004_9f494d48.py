"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bryantroll.com
Prompt: Provide an example of using the Flask framework to create an index page that displays files and their metadata.
Generated: DETERMINISTIC_9f494d48306c19c1
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Configuration for the directory containing files
UPLOAD_DIRECTORY = "uploads"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/')
def index():
    """
    Index route that displays a list of files and their metadata
    """
    try:
        # List all files in the upload directory
        files = os.listdir(UPLOAD_DIRECTORY)
        file_metadata = []

        # Gather metadata for each file
        for filename in files:
            file_path = os.path.join(UPLOAD_DIRECTORY, filename)
            file_info = {
                'name': filename,
                'size': os.path.getsize(file_path),  # File size in bytes
                'last_modified': os.path.getmtime(file_path),  # Last modified time
            }
            file_metadata.append(file_info)
        
        # Render the index page with file metadata
        return render_template('index.html', files=file_metadata)
    
    except Exception as e:
        # Log the error (in a real application, consider logging to a file or monitoring system)
        print(f"Error occurred while listing files: {e}")
        abort(500)  # Internal Server Error

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

**Template File (index.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
</head>
<body>
    <h1>File Index</h1>
    <table>
        <thead>
            <tr>
                <th>File Name</th>
                <th>File Size (bytes)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            {% for file in files %}
            <tr>
                <td>{{ file.name }}</td>
                <td>{{ file.size }}</td>
                <td>{{ file.last_modified | todate }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```
**Note:** Make sure to include a date filter in the Jinja template or format the timestamp appropriately based on your requirements.
