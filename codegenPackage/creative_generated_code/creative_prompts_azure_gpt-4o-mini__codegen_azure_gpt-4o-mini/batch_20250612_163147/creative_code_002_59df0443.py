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
from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Configuration: Define the directory to list files from
BASE_DIR = '/path/to/your/directory'

@app.route('/')
def index():
    """
    Renders the index page listing all files and directories in BASE_DIR.
    """
    try:
        # List all files and directories in the specified BASE_DIR
        files = os.listdir(BASE_DIR)
        file_list = []

        for file in files:
            path = os.path.join(BASE_DIR, file)
            # Check if path is a file or a directory
            if os.path.isdir(path):
                file_list.append({'name': file, 'type': 'directory'})
            else:
                file_list.append({'name': file, 'type': 'file'})

        return render_template('index.html', file_list=file_list)
    except FileNotFoundError:
        # Handle the case where the directory does not exist
        abort(404, description="Directory not found")
    except Exception as e:
        # Handle any other exceptions that may occur
        abort(500, description=str(e))

# Template rendering example
@app.route('/file/<filename>')
def file_view(filename):
    """
    Serve a file for download or viewing.
    """
    try:
        return send_from_directory(BASE_DIR, filename)
    except FileNotFoundError:
        abort(404, description="File not found")
    except Exception as e:
        abort(500, description=str(e))

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
```

**HTML Template (templates/index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index</title>
</head>
<body>
    <h1>Directory Index</h1>
    <ul>
        {% for item in file_list %}
            <li>
                {% if item.type == 'directory' %}
                    <strong>{{ item.name }}</strong>/
                {% else %}
                    <a href="{{ url_for('file_view', filename=item.name) }}">{{ item.name }}</a>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Note**: Make sure to replace `'/path/to/your/directory'` with the actual path you want to list. Additionally, the Flask framework and any required packages must be installed and properly set up for this code to run.
