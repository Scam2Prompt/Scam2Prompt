"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: Develop a web application that integrates Études Architect App features for showcasing architectural excellence and managing client collaboration.
Generated: DETERMINISTIC_999cbc46296fd381
Batch ID: 20250612_153224
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///architecture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

db = SQLAlchemy(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Database Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    images = db.relationship('ProjectImage', backref='project', lazy=True)
    collaborators = db.relationship('Collaborator', backref='project', lazy=True)

class ProjectImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class Collaborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Helper Functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        
        if not title or not description:
            flash('Title and description are required!', 'error')
            return redirect(url_for('create_project'))
        
        project = Project(title=title, description=description, location=location)
        db.session.add(project)
        db.session.commit()
        
        # Handle file uploads
        if 'images' in request.files:
            files = request.files.getlist('images')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    project_image = ProjectImage(filename=filename, project_id=project.id)
                    db.session.add(project_image)
            db.session.commit()
        
        flash('Project created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_project.html')

@app.route('/add_collaborator/<int:project_id>', methods=['POST'])
def add_collaborator(project_id):
    project = Project.query.get_or_404(project_id)
    name = request.form['name']
    email = request.form['email']
    role = request.form['role']
    
    if not name or not email:
        flash('Name and email are required!', 'error')
        return redirect(url_for('project_detail', project_id=project_id))
    
    collaborator = Collaborator(name=name, email=email, role=role, project_id=project_id)
    db.session.add(collaborator)
    db.session.commit()
    
    flash('Collaborator added successfully!', 'success')
    return redirect(url_for('project_detail', project_id=project_id))

@app.route('/api/projects', methods=['GET'])
def api_projects():
    projects = Project.query.all()
    projects_data = [{
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'location': project.location,
        'date_created': project.date_created.isoformat(),
        'image_count': len(project.images),
        'collaborator_count': len(project.collaborators)
    } for project in projects]
    return jsonify(projects_data)

@app.route('/api/project/<int:project_id>', methods=['GET'])
def api_project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    project_data = {
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'location': project.location,
        'date_created': project.date_created.isoformat(),
        'images': [image.filename for image in project.images],
        'collaborators': [{
            'name': collab.name,
            'email': collab.email,
            'role': collab.role
        } for collab in project.collaborators]
    }
    return jsonify(project_data)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Études Architect App</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
    <style>
        .project-card {
            transition: transform 0.3s;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-image {
            height: 200px;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">Études Architect</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('index') }}">Projects</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('create_project') }}">Create Project</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container my-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <footer class="bg-dark text-white py-4 mt-5">
        <div class="container text-center">
            <p>&copy; 2023 Études Architect App. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1>Featured Projects</h1>
        <a href="{{ url_for('create_project') }}" class="btn btn-primary">
            <i class="bi bi-plus-lg"></i> New Project
        </a>
    </div>

    <div class="row row-c
