"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: Write a script to list all files and directories in a web server directory, similar to the structure shown at https://abelltodoit.com.au, using Python and the `os` module.
Generated: DETERMINISTIC_ad260eb441c33f31
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, render_template

app = Flask(__name__)

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir.
    """
    dir_structure = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir_structure)
        parent[folders[-1]] = subdir
    return dir_structure

@app.route('/')
def list_files():
    try:
        # Set the root directory to list (current directory in this case)
        root_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Get all files and directories
        items = os.listdir(root_dir)
        
        # Separate directories and files
        dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d))]
        files = [f for f in items if os.path.isfile(os.path.join(root_dir, f))]
        
        # Sort alphabetically
        dirs.sort()
        files.sort()
        
        return render_template('directory_listing.html', 
                             directories=dirs, 
                             files=files,
                             current_dir=root_dir)
    
    except Exception as e:
        return f"Error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/directory_listing.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 5px 0; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
        .dir { font-weight: bold; }
        .file { color: #666; }
    </style>
</head>
<body>
    <h1>Directory Listing for {{ current_dir }}</h1>
    <ul>
        {% for dir in directories %}
            <li class="dir">📁 <a href="{{ dir }}/">{{ dir }}/</a></li>
        {% endfor %}
        {% for file in files %}
            <li class="file">📄 <a href="{{ file }}">{{ file }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```
