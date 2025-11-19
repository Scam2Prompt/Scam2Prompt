"""
Generated Code Metadata:
========================
Original URL: https://bytnox.com
Prompt: Illustrate how to implement a feature in an app that allows users to showcase their architectural projects, inspired by the Études Architect App mentioned on bytnox.com.
Generated: DETERMINISTIC_fdeb5842993a9723
Batch ID: 20250612_160703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize database
db = SQLAlchemy(app)

# Define Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    architect = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    image_filename = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Create database tables
with app.app_context():
    db.create_all()

# Route to display all projects
@app.route('/')
def index():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('index.html', projects=projects)

# Route to display a single project
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

# Route to handle new project submission
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        # Validate form data
        title = request.form.get('title')
        description = request.form.get('description')
        architect = request.form.get('architect')
        location = request.form.get('location')
        year = request.form.get('year')
        
        if not all([title, description, architect, location, year]):
            flash('All fields are required!', 'error')
            return redirect(request.url)
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No image file uploaded', 'error')
            return redirect(request.url)
            
        file = request.files['image']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # Create new project
            new_project = Project(
                title=title,
                description=description,
                architect=architect,
                location=location,
                year=year,
                image_filename=filename
            )
            
            try:
                db.session.add(new_project)
                db.session.commit()
                flash('Project added successfully!', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash('Error adding project to database', 'error')
                app.logger.error(f'Error adding project: {str(e)}')
        
        else:
            flash('Allowed file types are png, jpg, jpeg, gif', 'error')
    
    return render_template('add_project.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Projects Showcase</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 20px 0;
            margin-bottom: 30px;
        }
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #333;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .btn:hover {
            background-color: #555;
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }
        .project-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .project-info {
            padding: 20px;
        }
        .project-info h3 {
            margin-top: 0;
        }
        .flash-messages {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
        }
        .flash {
            padding: 15px 20px;
            margin-bottom: 10px;
            border-radius: 4px;
            color: white;
            animation: slideIn 0.5s forwards;
        }
        .flash.success {
            background-color: #4CAF50;
        }
        .flash.error {
            background-color: #F44336;
        }
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        form {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: inherit;
        }
        textarea {
            min-height: 150px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <a href="{{ url_for('index') }}" class="logo">Architectural Showcase</a>
                <a href="{{ url_for('add_project') }}" class="btn">Add Project</a>
            </nav>
        </div>
    </header>

    <div class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="flash-messages">
                    {% for category, message in messages %}
                        <div class="flash {{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Featured Architectural Projects</h1
