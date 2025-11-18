"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Create a Python script using Flask to serve a portfolio webpage for architectural projects, with endpoints for displaying project details and multimedia galleries.
Generated: DETERMINISTIC_bf049d90ce02bf4b
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, abort
import os

app = Flask(__name__)

# Sample Data: Projects and their details
projects = {
    1: {
        "title": "Modern House",
        "description": "A modern house design with eco-friendly materials.",
        "gallery": ["static/images/modern_house1.jpg", "static/images/modern_house2.jpg"]
    },
    2: {
        "title": "Urban Skyscraper",
        "description": "A skyscraper designed for urban living.",
        "gallery": ["static/images/skyscraper1.jpg", "static/images/skyscraper2.jpg"]
    }
}

@app.route('/')
def home():
    """Serve the homepage with a list of projects."""
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Serve details for a specific project.
    
    Args:
        project_id (int): The ID of the project to display.
    
    Returns:
        JSON or 404 error if project is not found.
    """
    project = projects.get(project_id)
    if project:
        return render_template('project_detail.html', project=project)
    else:
        abort(404)  # Return a 404 error if project not found

@app.route('/api/projects', methods=['GET'])
def api_projects():
    """API endpoint to get a list of projects in JSON format."""
    return jsonify(projects)

@app.route('/api/project/<int:project_id>', methods=['GET'])
def api_project_detail(project_id):
    """API endpoint to get details of a specific project.
    
    Args:
        project_id (int): The ID of the project to retrieve.
    
    Returns:
        JSON or 404 error if project is not found.
    """
    project = projects.get(project_id)
    if project:
        return jsonify(project)
    else:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Ensure the script runs only if it's the main module
    if not os.environ.get('FLASK_ENV'):
        app.run(debug=True)  # Set debug=True for development; switch to False in production
    else:
        app.run()
```

### Template File: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>
<body>
    <h1>Architectural Projects</h1>
    <ul>
        {% for project_id, project in projects.items() %}
        <li>
            <a href="{{ url_for('project_detail', project_id=project_id) }}">{{ project.title }}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Template File: `templates/project_detail.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.title }}</title>
</head>
<body>
    <h1>{{ project.title }}</h1>
    <p>{{ project.description }}</p>
    <h2>Gallery</h2>
    <div>
        {% for image in project.gallery %}
        <img src="{{ image }}" alt="{{ project.title }}" style="width:300px; height:auto;"/>
        {% endfor %}
    </div>
    <a href="{{ url_for('home') }}">Back to Projects</a>
</body>
</html>
```

### Template File: `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
``` 

### Additional Notes:
- Ensure you have Flask installed (`pip install Flask`).
- Add images in the specified static directory (`static/images/`).
- This script is ready for production with the correct environment configuration.
