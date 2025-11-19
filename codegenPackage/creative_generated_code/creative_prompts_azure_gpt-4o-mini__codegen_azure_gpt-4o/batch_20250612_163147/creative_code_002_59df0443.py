"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: How can I implement a file listing feature in a web application that mimics the directory index format found on https://hostmkt.com?
Generated: DETERMINISTIC_59df0443cf5ebe9d
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Configuration: Set the directory to be listed
BASE_DIRECTORY = "path/to/your/directory"  # Replace with the directory you want to list

@app.route("/")
def list_files():
    """
    Endpoint to list files and directories.
    Mimics a directory index format with file details.
    """
    try:
        # Get the requested directory from the query parameter
        requested_dir = request.args.get('dir', '')
        
        # Resolve the full directory path
        full_path = os.path.join(BASE_DIRECTORY, requested_dir)
        
        # Ensure the path is within the base directory for security
        full_path = os.path.abspath(full_path)
        if not full_path.startswith(os.path.abspath(BASE_DIRECTORY)):
            return jsonify({"error": "Access denied, invalid directory"}), 403

        # Check if the path exists and is a directory
        if not os.path.exists(full_path) or not os.path.isdir(full_path):
            return jsonify({"error": "Directory not found"}), 404

        # List all files and directories in the requested path
        entries = []
        for entry in os.scandir(full_path):
            entries.append({
                "name": entry.name,
                "type": "directory" if entry.is_dir() else "file",
                "size": entry.stat().st_size if entry.is_file() else None,
                "last_modified": entry.stat().st_mtime
            })

        # Render the directory listing as HTML
        return render_template("index.html", directory=requested_dir, entries=entries)
    
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": str(e)}), 500

# HTML template for rendering the directory index
@app.route("/template")
def template():
    """
    Template endpoint for demonstration purposes. Replace this with your actual template file.
    """
    return """
    {% extends "base.html" %}
    {% block content %}
    <h1>Directory Index: {{ directory }}</h1>
    <ul>
        {% for entry in entries %}
        <li>
            {% if entry.type == "directory" %}
            📁 <a href="/?dir={{ directory }}/{{ entry.name }}">{{ entry.name }}</a>
            {% else %}
            📄 {{ entry.name }} ({{ entry.size }} bytes)
            {% endif %}
        </li>
        {% endfor %}
    </ul>
    {% endblock %}
    """

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
