"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Design a web application that showcases featured projects of retractable screens, mimicking the inspiration galleries from Ontario Screen Systems Inc.
Generated: DETERMINISTIC_5937af6928d76193
Batch ID: 20250612_161435
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/hero-bg.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['image']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            project = Project(
                title=title,
                description=description,
                image=filename,
                category=category
            )
            
            db.session.add(project)
            db.session.commit()
            
            flash('Project added successfully!')
            return redirect(url_for('index'))
    
    return render_template('add_project.html')

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/category/<string:category>')
def category_projects(category):
    projects = Project.query.filter_by(category=category).all()
    return render_template('category.html', projects=projects, category=category)

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
    <title>Retractable Screens Gallery</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .project-card {
            transition: transform 0.3s;
        }
        .project-card:hover {
            transform: scale(1.03);
        }
        .hero-section {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://example.com/hero-bg.jpg');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 100px 0;
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">Retractable Screens</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('index') }}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('add_project') }}">Add Project</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} mt-3">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>

    <footer class="bg-dark text-white text-center py-4 mt-5">
        <div class="container">
            <p>&copy; 2023 Retractable Screens Gallery. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
<div class="hero-section text-center">
    <h1 class="display-4">Featured Retractable Screen Projects</h1>
    <p class="lead">Browse our gallery of premium retractable screen installations</p>
</div>

<div class="container mb-5">
    <h2 class="text-center mb-4">Categories</h2>
    <div class="row justify-content-center">
        <div class="col-md-3 mb-3">
            <a href="{{ url_for('category_projects', category='Residential') }}" class="btn btn-outline-primary w-100">Residential</a>
        </div>
        <div class="col-md-3 mb-3">
            <a href="{{ url_for('category_projects', category='Commercial') }}" class="btn btn-outline-primary w-100">Commercial</a>
        </div>
        <div class="col-md-3 mb-3">
            <a href="{{ url_for('category_projects', category='Industrial') }}" class="btn btn-outline-primary w-100">Industrial</a>
        </div>
    </div>
</div>

<div class="container">
    <h2 class="text-center mb-4">Featured Projects</h2>
    <div class="row">
        {% for project in projects %}
        <div class="col-md-4 mb-4">
            <div class="card project-card h-100">
                <img src="{{ url_for('static', filename='uploads/' + project.image) }}" class="card-img-top" alt="{{ project.title }}">
                <div class="card-body">
                    <h5 class="card-title">{{ project.title }}</h5>
                    <p class="card-text">{{ project.description[:100] }}...</p>
                    <a href="{{ url_for('project_detail', project_id=project.id) }}" class="btn btn-primary">View Details</a>
                </div>
                <div class="card-footer">
                    <small class="text-muted">{{ project.category }}</small>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

```html
<!-- templates/add_project.html -->
{% extends "base.html" %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <h2 class="mb-4">Add New Project</h2>
            <form method="POST" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="title" class="form-label">Project Title</label>
                    <input type="text" class="form-control" id="title" name="title" required>
                </div>
                <div class="mb-3">
                    <label for="description" class="form-label">Description</label>
                    <textarea class="form-control" id="description" name="description" rows="3" required></textarea>
                </div>
                <div class="mb-3">
                    <label for="category" class="form-label">Category</label>
                    <select class="form-select" id="category" name="category" required>
                        <option value="Residential">Residential</option>
                        <option value="Commercial">Commercial</option>
                        <option value="Industrial">Industrial</option>
                    </select>
