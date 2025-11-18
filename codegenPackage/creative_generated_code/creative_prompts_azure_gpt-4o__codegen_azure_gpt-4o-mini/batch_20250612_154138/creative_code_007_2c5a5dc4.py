"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Recommend tools or libraries for managing and visualizing directory structures on a web server, similar to the one at https://360fuel.network.
Generated: DETERMINISTIC_2c5a5dc4f8478993
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# DirectoryVisualizer.py

import os
import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/directory', methods=['GET'])
def get_directory_structure():
    """API endpoint to return the directory structure in JSON format."""
    try:
        path = request.args.get('path', os.getcwd())
        if not os.path.exists(path):
            return jsonify({"error": "Path does not exist"}), 404
        
        directory_structure = build_directory_structure(path)
        return jsonify(directory_structure), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def build_directory_structure(path):
    """Build a nested dictionary representing the directory structure."""
    dir_structure = {"name": os.path.basename(path), "path": path, "children": []}
    
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                dir_structure["children"].append(build_directory_structure(item_path))
            else:
                dir_structure["children"].append({"name": item, "path": item_path})
    except PermissionError:
        return {"error": "Permission denied"}
    except Exception as e:
        return {"error": str(e)}

    return dir_structure

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Visualizer</title>
    <style>
        body { font-family: Arial, sans-serif; }
        #output { white-space: pre; }
    </style>
</head>
<body>
    <h1>Directory Visualizer</h1>
    <input type="text" id="pathInput" placeholder="Enter directory path" />
    <button onclick="fetchDirectory()">Visualize</button>
    <div id="output"></div>

    <script>
        async function fetchDirectory() {
            const path = document.getElementById('pathInput').value;
            const response = await fetch(`/api/directory?path=${encodeURIComponent(path)}`);
            const data = await response.json();
            document.getElementById('output').innerText = JSON.stringify(data, null, 2);
        }
    </script>
</body>
</html>
```

### Requirements:
- Flask: `pip install Flask`
- Ensure to run this code in a safe environment that has access to your filesystem.
- For production use, consider configuring proper logging, security measures, and testing edge cases.
