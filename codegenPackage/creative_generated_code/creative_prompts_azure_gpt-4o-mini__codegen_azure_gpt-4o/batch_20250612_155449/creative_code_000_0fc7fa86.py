"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.world
Prompt: "Generate a Python script to list all files in a directory, similar to the index view at https://symbioticfi.world."
Generated: DETERMINISTIC_0fc7fa861e7c1783
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# Configuration
DIRECTORY_TO_LIST = "./files"  # Change this to the directory you want to list
PORT = 5000  # Port number for Flask app

@app.route("/")
def list_files():
    """
    Endpoint to list all files in the specified directory.
    Renders an HTML page with the list of files.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(DIRECTORY_TO_LIST):
            abort(404, description="Directory not found.")
        
        # List all files in the directory
        files = [
            file for file in os.listdir(DIRECTORY_TO_LIST)
            if os.path.isfile(os.path.join(DIRECTORY_TO_LIST, file))
        ]

        # Render the list of files in an HTML page
        return render_template("index.html", files=files, directory=DIRECTORY_TO_LIST)
    except Exception as e:
        # Return a generic error message if something goes wrong
        abort(500, description=f"An error occurred: {str(e)}")

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 Not Found.
    """
    return f"<h1>404 Not Found</h1><p>{error.description}</p>", 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 Internal Server Error.
    """
    return f"<h1>500 Internal Server Error</h1><p>{error.description}</p>", 500

if __name__ == "__main__":
    # Ensure the directory exists before starting the server
    if not os.path.exists(DIRECTORY_TO_LIST):
        print(f"Error: The directory '{DIRECTORY_TO_LIST}' does not exist.")
        exit(1)

    # Start the Flask application
    app.run(host="0.0.0.0", port=PORT, debug=False)
```

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h1 {
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Files in {{ directory }}</h1>
    <ul>
        {% for file in files %}
            <li><a href="/files/{{ file }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### Notes:
- Save the HTML file as `index.html` inside a `templates` folder.
- The script assumes the directory to list (`files`) exists and is accessible. You can change `DIRECTORY_TO_LIST` to any valid directory path.
- For production use, make sure to properly secure the directory listing logic and sanitize inputs.
