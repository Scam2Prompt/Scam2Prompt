"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synerex-bo.com
Prompt: How can I create a web application that displays an index of files, like the one on synerex-bo.com, using Flask?
Generated: DETERMINISTIC_7c84cc471dffe7a8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, send_from_directory, abort
import os

# Initialize the Flask app
app = Flask(__name__)

# Directory to serve files from
BASE_DIRECTORY = os.path.abspath("files")  # Change "files" to your desired directory

# Route to list all files in the directory
@app.route("/")
def index():
    try:
        # Get a list of all files in the directory
        files = os.listdir(BASE_DIRECTORY)
    except FileNotFoundError:
        abort(404)  # Return a 404 error if the directory does not exist
    except PermissionError:
        abort(403)  # Return a 403 error if permission is denied

    # Render a template listing the files
    return render_template("index.html", files=files)

# Route to download or view files
@app.route("/files/<filename>")
def serve_file(filename):
    try:
        # Serve the file from the directory
        return send_from_directory(BASE_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)  # Return a 404 error if the file does not exist
    except PermissionError:
        abort(403)  # Return a 403 error if permission is denied

if __name__ == "__main__":
    # Ensure the BASE_DIRECTORY exists
    if not os.path.exists(BASE_DIRECTORY):
        os.makedirs(BASE_DIRECTORY)  # Create the directory if it doesn't exist

    # Run the application
    app.run(debug=True)

# HTML Template (index.html)
# Save the following content in a file named 'templates/index.html'
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
</head>
<body>
    <h1>File Index</h1>
    <ul>
        {% for file in files %}
        <li><a href="/files/{{ file }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""
```
