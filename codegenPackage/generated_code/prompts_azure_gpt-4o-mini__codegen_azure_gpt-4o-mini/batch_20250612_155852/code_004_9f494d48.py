"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Provide an example of using the Flask framework to create an index page that displays files and their metadata.
Generated: DETERMINISTIC_9f494d48306c19c1
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

# Configuration for the directory to list files from
UPLOAD_FOLDER = 'uploads'  # Change this to your desired directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    """
    Render the index page displaying files and their metadata.
    """
    try:
        # List all files in the upload folder
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        file_metadata = []

        for file in files:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
            # Gather file metadata
            metadata = {
                'name': file,
                'size': os.path.getsize(file_path),  # Size in bytes
                'last_modified': os.path.getmtime(file_path)  # Last modified time
            }
            file_metadata.append(metadata)

        return render_template('index.html', files=file_metadata)

    except Exception as e:
        # Log the error and return a 500 error page
        app.logger.error(f"Error retrieving files: {e}")
        abort(500)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

**index.html** (Create this file in a `templates` folder):
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
                <th>Size (bytes)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            {% for file in files %}
            <tr>
                <td>{{ file.name }}</td>
                <td>{{ file.size }}</td>
                <td>{{ file.last_modified | to_datetime }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

**Note**: You may need to add a custom filter in your Flask app to format the last modified time. Here’s how you can do that:

```python
from datetime import datetime

@app.template_filter('to_datetime')
def to_datetime(timestamp):
    """
    Convert a timestamp to a human-readable datetime string.
    """
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
```

Make sure to place the `index.html` file in a folder named `templates` in the same directory as your Flask application.
