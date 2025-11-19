"""
Generated Code Metadata:
========================
Original URL: https://bridgeqom.pages.dev
Prompt: "Develop a simple app using the Bridge App Explorer for a community-driven project like QOM."
Generated: DETERMINISTIC_7394574f969c86ff
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize database
db = SQLAlchemy(app)

# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    image_path = db.Column(db.String(200))

class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    contributor = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects', methods=['POST'])
def create_project():
    try:
        title = request.form.get('title')
        description = request.form.get('description')
        creator = request.form.get('creator')
        
        if not all([title, description, creator]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Handle file upload
        image_path = None
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        project = Project(
            title=title,
            description=description,
            creator=creator,
            image_path=image_path
        )
        db.session.add(project)
        db.session.commit()

        return jsonify({'message': 'Project created successfully', 'project_id': project.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    contributions = Contribution.query.filter_by(project_id=project_id).all()
    
    return render_template('project.html', 
                         project=project, 
                         contributions=contributions)

@app.route('/projects/<int:project_id>/contribute', methods=['POST'])
def contribute_to_project(project_id):
    try:
        contributor = request.form.get('contributor')
        amount = request.form.get('amount')
        message = request.form.get('message', '')
        
        if not all([contributor, amount]):
            return jsonify({'error': 'Missing required fields'}), 400

        contribution = Contribution(
            project_id=project_id,
            contributor=contributor,
            amount=float(amount),
            message=message
        )
        db.session.add(contribution)
        db.session.commit()

        return jsonify({'message': 'Contribution added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

# Main
if __name__ == '__main__':
    # Create upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Community Projects</title>
    <style>
        .project-card {
            border: 1px solid #ddd;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
        }
        .project-image {
            max-width: 200px;
            max-height: 200px;
        }
    </style>
</head>
<body>
    <h1>Community Projects</h1>
    <a href="/create-project">Create New Project</a>
    
    <div class="projects-list">
        {% for project in projects %}
        <div class="project-card">
            <h2><a href="/projects/{{ project.id }}">{{ project.title }}</a></h2>
            <p>By: {{ project.creator }}</p>
            <p>{{ project.description }}</p>
            {% if project.image_path %}
            <img src="{{ project.image_path }}" alt="{{ project.title }}" class="project-image">
            {% endif %}
        </div>
        {% endfor %}
    </div>
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
    <title>{{ project.title }}</title>
    <style>
        .contribution {
            border: 1px solid #eee;
            padding: 10px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>{{ project.title }}</h1>
    <p>Created by: {{ project.creator }}</p>
    <p>{{ project.description }}</p>
    {% if project.image_path %}
    <img src="{{ project.image_path }}" alt="{{ project.title }}" width="300">
    {% endif %}
    
    <h2>Contributions</h2>
    <div class="contributions-list">
        {% for contribution in contributions %}
        <div class="contribution">
            <p><strong>{{ contribution.contributor }}</strong> contributed {{ contribution.amount }}</p>
            <p>{{ contribution.message }}</p>
        </div>
        {% endfor %}
    </div>
    
    <h2>Make a Contribution</h2>
    <form action="/projects/{{ project.id }}/contribute" method="POST">
        <label for="contributor">Your Name:</label>
        <input type="text" id="contributor" name="contributor" required><br>
        
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" step="0.01" required><br>
        
        <label for="message">Message (optional):</label>
        <textarea id="message" name="message"></textarea><br>
        
        <button type="submit">Contribute</button>
    </form>
</body>
</html>
```

```html
<!-- templates/create-project.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Project</title>
</head>
<body>
    <h1>Create New Project</h1>
    <form action="/projects" method="POST" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>
        
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea><br>
        
        <label for="creator">Your Name:</label>
        <input type="text" id="creator" name="creator" required><br>
        
        <label for="image">Project Image (optional):</label>
        <input type="file" id="image" name="image" accept="image/*"><br>
        
        <button type="submit">Create Project</button>
    </form>
</body>
</html>
```
