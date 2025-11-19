"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Generate a code snippet for a web application that showcases a portfolio of architectural projects similar to those featured on Linea 7's website, emphasizing user-centric design and functionality.
Generated: DETERMINISTIC_78b90ae3951f3584
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify, request
import os

# Initialize the Flask application
app = Flask(__name__)

# Sample data representing architectural projects
# In a production environment, this data would likely come from a database
projects = [
    {
        "id": 1,
        "title": "Modern Residential Design",
        "description": "A sleek and modern residential project with sustainable materials.",
        "image_url": "/static/images/residential.jpg",
        "category": "Residential"
    },
    {
        "id": 2,
        "title": "Urban Office Space",
        "description": "An innovative office space designed for collaboration and productivity.",
        "image_url": "/static/images/office.jpg",
        "category": "Commercial"
    },
    {
        "id": 3,
        "title": "Cultural Center",
        "description": "A cultural center that blends traditional and contemporary architectural styles.",
        "image_url": "/static/images/cultural.jpg",
        "category": "Public"
    }
]

# Route to serve the homepage
@app.route('/')
def home():
    """
    Render the homepage with a list of architectural projects.
    """
    return render_template('index.html', projects=projects)

# Route to fetch project details via API
@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    API endpoint to fetch all projects.
    Returns:
        JSON response containing all project data.
    """
    return jsonify(projects)

# Route to fetch a specific project by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    API endpoint to fetch a specific project by ID.
    Args:
        project_id (int): ID of the project to fetch.
    Returns:
        JSON response containing the project data or an error message.
    """
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    else:
        return jsonify({"error": "Project not found"}), 404

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    Args:
        e: The error object.
    Returns:
        Rendered 404 error page.
    """
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Ensure the static folder is correctly set for serving images
    app.static_folder = 'static'
    
    # Run the Flask application
    app.run(debug=True)
```

### Directory Structure:
```
project/
├── app.py
├── static/
│   ├── images/
│   │   ├── residential.jpg
│   │   ├── office.jpg
│   │   ├── cultural.jpg
├── templates/
│   ├── index.html
│   ├── 404.html
```

### Example `index.html` Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Portfolio</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Architectural Portfolio</h1>
    </header>
    <main>
        <section>
            <h2>Projects</h2>
            <div class="projects">
                {% for project in projects %}
                <div class="project">
                    <img src="{{ project.image_url }}" alt="{{ project.title }}">
                    <h3>{{ project.title }}</h3>
                    <p>{{ project.description }}</p>
                    <p><strong>Category:</strong> {{ project.category }}</p>
                </div>
                {% endfor %}
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Architectural Portfolio</p>
    </footer>
</body>
</html>
```

### Example `404.html` Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <header>
        <h1>404 - Page Not Found</h1>
    </header>
    <main>
        <p>Sorry, the page you are looking for does not exist.</p>
        <a href="/">Return to Homepage</a>
    </main>
</body>
</html>
```
