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
from flask import Flask, jsonify, render_template, request, abort
import os

app = Flask(__name__)

# Sample data for projects
projects = [
    {
        "id": 1,
        "name": "Modern Villa",
        "description": "A modern villa with state-of-the-art architecture.",
        "images": ["villa1.jpg", "villa2.jpg", "villa3.jpg"]
    },
    {
        "id": 2,
        "name": "Urban Apartment",
        "description": "An eco-friendly urban apartment design.",
        "images": ["apartment1.jpg", "apartment2.jpg", "apartment3.jpg"]
    },
    {
        "id": 3,
        "name": "Riverside Cottage",
        "description": "A cozy riverside cottage with scenic views.",
        "images": ["cottage1.jpg", "cottage2.jpg", "cottage3.jpg"]
    }
]

# Route to serve the portfolio homepage
@app.route('/')
def home():
    """
    Render the homepage of the portfolio.
    """
    return render_template('index.html', projects=projects)

# Route to display details of a specific project
@app.route('/project/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Return detailed information about a specific project.
    """
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        abort(404, description="Project not found")
    return render_template('project.html', project=project)

# Route to fetch project data as JSON
@app.route('/api/project/<int:project_id>', methods=['GET'])
def get_project_json(project_id):
    """
    Return project data as a JSON response.
    """
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        abort(404, description="Project not found")
    return jsonify(project)

# Route for multimedia gallery of a specific project
@app.route('/project/<int:project_id>/gallery')
def project_gallery(project_id):
    """
    Render a multimedia gallery for a specific project.
    """
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        abort(404, description="Project not found")
    return render_template('gallery.html', images=project["images"])

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """
    Custom error page for 404 errors.
    """
    return render_template('404.html', error=error), 404

# Run the Flask app
if __name__ == '__main__':
    # Ensure templates directory exists
    templates_dir = os.path.join(os.getcwd(), 'templates')
    if not os.path.exists(templates_dir):
        os.mkdir(templates_dir)
    
    # Start the Flask development server
    app.run(debug=True)
```

Make sure to create the corresponding HTML files (`index.html`, `project.html`, `gallery.html`, and `404.html`) in a `templates/` directory to support this script.
