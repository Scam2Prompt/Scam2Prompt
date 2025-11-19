"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://completecircleconsulting.xyz
Prompt: Generate code for a web application that showcases commission work samples related to nature-inspired projects.
Generated: DETERMINISTIC_d9bfae4400f5c388
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask web application to showcase commission work samples related to nature-inspired projects

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Directory to store project sample images
PROJECTS_DIR = "static/projects"

# Ensure the projects directory exists
if not os.path.exists(PROJECTS_DIR):
    os.makedirs(PROJECTS_DIR)

# Sample data for projects (to simulate a database)
projects = [
    {"id": 1, "title": "Forest Landscape Painting", "description": "A serene forest landscape.", "image": "forest.jpg"},
    {"id": 2, "title": "Ocean Wave Sculpture", "description": "An intricate sculpture inspired by ocean waves.", "image": "ocean.jpg"},
    {"id": 3, "title": "Mountain View Photography", "description": "A breathtaking photograph capturing mountain views.", "image": "mountain.jpg"},
]

@app.route("/")
def home():
    """
    Render the home page which lists all nature-inspired projects.
    """
    return render_template("index.html", projects=projects)

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    """
    Render the detail page for a specific project.
    """
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return render_template("project_detail.html", project=project)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully by rendering a custom error page.
    """
    return render_template("404.html"), 404

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

### `templates/index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nature-Inspired Projects</title>
</head>
<body>
    <h1>Nature-Inspired Commission Work Samples</h1>
    <ul>
        {% for project in projects %}
        <li>
            <a href="/project/{{ project.id }}">
                <h2>{{ project.title }}</h2>
                <p>{{ project.description }}</p>
                <img src="/static/projects/{{ project.image }}" alt="{{ project.title }}" width="200">
            </a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### `templates/project_detail.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.title }}</title>
</head>
<body>
    <h1>{{ project.title }}</h1>
    <p>{{ project.description }}</p>
    <img src="/static/projects/{{ project.image }}" alt="{{ project.title }}" width="400">
    <p><a href="/">Back to all projects</a></p>
</body>
</html>
```

### `templates/404.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you're looking for doesn't exist.</p>
    <p><a href="/">Return to Home</a></p>
</body>
</html>
```

### Directory Structure:
```
/project_showcase_app
    ├── app.py
    ├── static/
    │   └── projects/
    │       ├── forest.jpg
    │       ├── ocean.jpg
    │       └── mountain.jpg
    ├── templates/
    │   ├── index.html
    │   ├── project_detail.html
    │   └── 404.html
```
