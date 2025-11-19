"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benenergie-dz.com
Prompt: What libraries can I use to create a web interface that lists files and directories like the one on benenergie-dz.com?
Generated: DETERMINISTIC_76c6b102fcb14754
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, send_from_directory
import os

# Initialize Flask app
app = Flask(__name__)

# Set a base directory to list files and folders
BASE_DIRECTORY = os.path.abspath("files")  # Specify the directory to serve files from

# Define the route to list files and directories
@app.route('/')
def list_files_and_directories():
    """
    Route to display the list of files and directories
    in the BASE_DIRECTORY.
    """
    try:
        # Get the list of files and directories
        items = os.listdir(BASE_DIRECTORY)
        items = sorted(items)  # Sort items for better organization
        return render_template('index.html', items=items)
    except Exception as e:
        # Handle errors gracefully
        return f"Error occurred: {e}", 500

# Define the route to download files
@app.route('/download/<filename>')
def download_file(filename):
    """
    Route to download a specific file.
    """
    try:
        # Send file from the BASE_DIRECTORY
        return send_from_directory(BASE_DIRECTORY, filename, as_attachment=True)
    except Exception as e:
        # Handle file not found or other errors
        return f"Error occurred: {e}", 404

# Define the route to navigate directories
@app.route('/navigate/<path:subdirectory>')
def navigate_directory(subdirectory):
    """
    Route to navigate into a subdirectory and list its contents.
    """
    try:
        # Construct the full path of the subdirectory
        full_path = os.path.join(BASE_DIRECTORY, subdirectory)

        # Verify the path exists and is a directory
        if not os.path.isdir(full_path):
            return f"Error: Directory '{subdirectory}' not found.", 404

        # Get the list of files and directories within the subdirectory
        items = os.listdir(full_path)
        items = sorted(items)  # Sort items for better organization
        return render_template('index.html', items=items, parent=subdirectory)
    except Exception as e:
        # Handle errors gracefully
        return f"Error occurred: {e}", 500

# HTML Template (index.html)
# Save this as "templates/index.html" in your project directory
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Browser</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
        a {
            text-decoration: none;
            color: blue;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>File Browser</h1>
        <ul>
            {% if parent %}
                <li><a href="/">Back to top</a></li>
            {% endif %}
            {% for item in items %}
                <li>
                    {% if '.' in item %}
                        <a href="/download/{{ item }}">{{ item }}</a>
                    {% else %}
                        <a href="/navigate/{{ item }}">{{ item }}</a>
                    {% endif %}
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

# Start the Flask app
if __name__ == '__main__':
    # Ensure the BASE_DIRECTORY exists
    if not os.path.exists(BASE_DIRECTORY):
        os.makedirs(BASE_DIRECTORY)  # Create it if it doesn't exist
    
    # Run the server on localhost
    app.run(debug=True)
```
