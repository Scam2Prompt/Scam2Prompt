"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet0732127-exodus-ssl48.shimi.com.au
Prompt: Write a script to list all files and directories from a web server directory listing, similar to the one served by LiteSpeed Web Server.
Generated: DETERMINISTIC_2964cb9c2498bb53
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, send_from_directory, abort, render_template_string

app = Flask(__name__)

# HTML template to display directory contents
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Directory Listing</title>
    <style>
        body { font-family: Arial, sans-serif; }
        a { text-decoration: none; color: blue; }
        a:hover { text-decoration: underline; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 5px; }
    </style>
</head>
<body>
    <h1>Directory listing for {{ path }}</h1>
    <ul>
        {% for item in items %}
            <li>
                <a href="{{ item['link'] }}">{{ item['name'] }}</a> {% if item['is_dir'] %} (Directory) {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/files/<path:subpath>', methods=['GET'])
def list_files(subpath):
    """List files and directories in the given subpath."""
    # Define the root directory for listing
    root_dir = '/path/to/your/web/server/directory'  # Change to your directory

    # Construct the full path
    full_path = os.path.join(root_dir, subpath)

    try:
        # Check if the path exists and is a directory
        if not os.path.exists(full_path) or not os.path.isdir(full_path):
            abort(404)  # Return 404 if the path is not found

        # List all files and directories in the given path
        items = []
        for item in os.listdir(full_path):
            item_path = os.path.join(subpath, item)
            is_dir = os.path.isdir(os.path.join(full_path, item))
            items.append({'name': item, 'link': item_path, 'is_dir': is_dir})

        # Render the directory listing using the HTML template
        return render_template_string(HTML_TEMPLATE, path=subpath, items=items)

    except Exception as e:
        # Log the exception (could be logged to a file or monitoring system)
        print(f"Error: {e}")
        abort(500)  # Return a 500 Internal Server Error on exceptions

if __name__ == '__main__':
    # Run the Flask application on debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to change `'/path/to/your/web/server/directory'` to the actual path you want to serve. This code uses Flask, so you need to have Flask installed in your environment. You can install it using pip:

```bash
pip install Flask
```
