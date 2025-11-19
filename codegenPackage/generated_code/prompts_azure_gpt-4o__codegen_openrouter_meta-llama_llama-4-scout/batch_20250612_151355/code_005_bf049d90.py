"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Create a Python script using Flask to serve a portfolio webpage for architectural projects, with endpoints for displaying project details and multimedia galleries.
Generated: DETERMINISTIC_bf049d90ce02bf4b
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample in-memory data store for demonstration purposes
projects = [
    {
        "id": 1,
        "name": "Project 1",
        "description": "This is project 1",
        "images": ["image1.jpg", "image2.jpg"],
        "videos": ["video1.mp4"]
    },
    {
        "id": 2,
        "name": "Project 2",
        "description": "This is project 2",
        "images": ["image3.jpg", "image4.jpg"],
        "videos": ["video2.mp4"]
    }
]

# Route for homepage
@app.route('/')
def index():
    """Renders the portfolio homepage"""
    return render_template('index.html', projects=projects)

# Route for project details
@app.route('/project/<int:project_id>')
def project_details(project_id):
    """Renders project details page"""
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, description="Project not found")
    return render_template('project.html', project=project)

# Route for project images
@app.route('/project/<int:project_id>/images')
def project_images(project_id):
    """Returns project images as JSON"""
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, description="Project not found")
    return jsonify(project['images'])

# Route for project videos
@app.route('/project/<int:project_id>/videos')
def project_videos(project_id):
    """Returns project videos as JSON"""
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, description="Project not found")
    return jsonify(project['videos'])

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return render_template('404.html'), 404

# Error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    """Handles 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>
<body>
    <h1>Portfolio</h1>
    <ul>
    {% for project in projects %}
        <li>
            <a href="{{ url_for('project_details', project_id=project.id) }}">{{ project.name }}</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/project.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.name }}</title>
</head>
<body>
    <h1>{{ project.name }}</h1>
    <p>{{ project.description }}</p>
    <h2>Images</h2>
    <ul>
    {% for image in project.images %}
        <li>{{ image }}</li>
    {% endfor %}
    </ul>
    <h2>Videos</h2>
    <ul>
    {% for video in project.videos %}
        <li>{{ video }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

```html
<!-- templates/500.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>An internal server error occurred.</p>
</body>
</html>
```
