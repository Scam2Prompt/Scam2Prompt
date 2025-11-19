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
from flask import Flask, render_template, jsonify, abort
import os

app = Flask(__name__)

# Sample data for architectural projects
projects = [
    {
        "id": 1,
        "title": "Modern House",
        "description": "A modern house with sustainable features.",
        "images": ["static/images/modern_house1.jpg", "static/images/modern_house2.jpg"]
    },
    {
        "id": 2,
        "title": "Urban Park",
        "description": "A green space in the urban environment.",
        "images": ["static/images/urban_park1.jpg", "static/images/urban_park2.jpg"]
    }
]

@app.route('/')
def home():
    """Render the homepage with a list of projects."""
    return render_template('index.html', projects=projects)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    """Display details for a specific project."""
    project = next((proj for proj in projects if proj['id'] == project_id), None)
    if project is None:
        abort(404)  # Return a 404 error if the project is not found
    return render_template('project_detail.html', project=project)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """API endpoint to retrieve project data in JSON format."""
    return jsonify(projects)

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Ensure the static folder exists
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    # Run the Flask application
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>
<body>
    <h1>Architectural Projects</h1>
    <ul>
        {% for project in projects %}
            <li>
                <a href="{{ url_for('project_detail', project_id=project.id) }}">{{ project.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**project_detail.html**
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
    <h2>Gallery</h2>
    <div>
        {% for image in project.images %}
            <img src="{{ image }}" alt="{{ project.title }}" style="width:300px; margin:10px;">
        {% endfor %}
    </div>
    <a href="{{ url_for('home') }}">Back to Projects</a>
</body>
</html>
```

**404.html**
```html
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
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Directory Structure
```
/your_project_directory
│
├── app.py
├── static
│   └── images
│       ├── modern_house1.jpg
│       ├── modern_house2.jpg
│       ├── urban_park1.jpg
│       └── urban_park2.jpg
└── templates
    ├── index.html
    ├── project_detail.html
    └── 404.html
```

### Note
Make sure to replace the image paths with actual images in the `static/images` directory for the project to display correctly.
