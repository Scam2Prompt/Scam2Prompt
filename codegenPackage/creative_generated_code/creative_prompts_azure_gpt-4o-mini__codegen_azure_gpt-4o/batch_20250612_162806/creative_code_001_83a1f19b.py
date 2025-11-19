"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: How can I implement a project gallery feature for a paving company’s website that showcases residential and commercial paving projects?
Generated: DETERMINISTIC_83a1f19b4300606a
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configure upload folder and allowed file types for project images
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Check if the uploaded file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define the Project class to hold project data
class Project:
    def __init__(self, id, title, description, image_path, category):
        self.id = id
        self.title = title
        self.description = description
        self.image_path = image_path
        self.category = category

# In-memory storage for projects (replace with a database in production)
projects = []

# Route to display the project gallery
@app.route('/')
def gallery():
    residential_projects = [p for p in projects if p.category == 'residential']
    commercial_projects = [p for p in projects if p.category == 'commercial']
    return render_template('gallery.html', residential_projects=residential_projects, commercial_projects=commercial_projects)

# Route to add a new project via form submission
@app.route('/add-project', methods=['POST'])
def add_project():
    try:
        # Gather form data
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        file = request.files.get('image')

        # Validate form data
        if not title or not description or not category or not file:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Validate category
        if category not in {'residential', 'commercial'}:
            return jsonify({'error': 'Invalid category'}), 400
        
        # Validate file upload
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Save the file to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Add the project to in-memory storage
            project_id = len(projects) + 1
            new_project = Project(project_id, title, description, image_path, category)
            projects.append(new_project)

            return jsonify({'message': 'Project added successfully'}), 201
        else:
            return jsonify({'error': 'Invalid file type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (`gallery.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .project {
            border: 1px solid #ccc;
            padding: 10px;
            width: 300px;
        }
        .project img {
            width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Residential Projects</h1>
    <div class="gallery">
        {% for project in residential_projects %}
            <div class="project">
                <img src="{{ project.image_path }}" alt="{{ project.title }}">
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
            </div>
        {% endfor %}
    </div>

    <h1>Commercial Projects</h1>
    <div class="gallery">
        {% for project in commercial_projects %}
            <div class="project">
                <img src="{{ project.image_path }}" alt="{{ project.title }}">
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```
