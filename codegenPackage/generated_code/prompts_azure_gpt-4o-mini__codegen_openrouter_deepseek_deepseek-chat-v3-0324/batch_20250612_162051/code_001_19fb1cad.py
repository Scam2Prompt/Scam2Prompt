"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: How can I implement a digital learning environment using resources from the "Curso online de Generación de Actividades y Uso de PDI con Tablets y Dispositivos Móviles" provided by Unimel Educación?
Generated: DETERMINISTIC_19fb1cad9f2409a6
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digital_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}

# Initialize database
db = SQLAlchemy(app)

# Database models
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modules = db.relationship('Module', backref='course', lazy=True)

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    resources = db.relationship('Resource', backref='module', lazy=True)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    file_path = db.Column(db.String(255))
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    resource_type = db.Column(db.String(50), nullable=False)  # pdf, video, image, etc.

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes
@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def view_course(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course.html', course=course)

@app.route('/module/<int:module_id>')
def view_module(module_id):
    module = Module.query.get_or_404(module_id)
    return render_template('module.html', module=module)

@app.route('/upload_resource/<int:module_id>', methods=['GET', 'POST'])
def upload_resource(module_id):
    module = Module.query.get_or_404(module_id)
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            resource = Resource(
                title=request.form['title'],
                description=request.form['description'],
                file_path=filename,
                module_id=module_id,
                resource_type=filename.rsplit('.', 1)[1].lower()
            )
            
            db.session.add(resource)
            db.session.commit()
            flash('Resource uploaded successfully!')
            return redirect(url_for('view_module', module_id=module_id))
    
    return render_template('upload_resource.html', module=module)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entorno Digital de Aprendizaje</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Cursos Disponibles</h1>
        <div class="row">
            {% for course in courses %}
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ course.title }}</h5>
                        <p class="card-text">{{ course.description }}</p>
                        <a href="{{ url_for('view_course', course_id=course.id) }}" class="btn btn-primary">Ver Curso</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/course.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ course.title }}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">{{ course.title }}</h1>
        <p>{{ course.description }}</p>
        
        <h2 class="my-4">Módulos</h2>
        <div class="list-group">
            {% for module in course.modules %}
            <a href="{{ url_for('view_module', module_id=module.id) }}" class="list-group-item list-group-item-action">
                <h5>{{ module.title }}</h5>
                <p>{{ module.description }}</p>
            </a>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/module.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ module.title }}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">{{ module.title }}</h1>
        <p>{{ module.description }}</p>
        
        <h2 class="my-4">Recursos</h2>
        <div class="row">
            {% for resource in module.resources %}
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ resource.title }}</h5>
                        <p class="card-text">{{ resource.description }}</p>
                        {% if resource.resource_type in ['jpg', 'jpeg', 'png', 'gif'] %}
                            <img src="{{ url_for('uploaded_file', filename=resource.file_path) }}" class="img-fluid" alt="{{ resource.title }}">
                        {% elif resource.resource_type == 'pdf' %}
                            <a href="{{ url_for('uploaded_file', filename=resource.file_path) }}" class="btn btn-primary">Ver PDF</a>
                        {% elif resource.resource_type in ['mp4', 'mov'] %}
                            <video width="100%" controls>
                                <source src="{{ url_for('uploaded_file', filename=resource.file_path) }}" type="video/{{ resource.resource_type }}">
                            </video>
                        {% endif %}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <a href="{{ url_for('upload_resource', module_id=module.id) }}" class="btn btn-success">Subir Recurso</a>
    </div>
</body>
</html>
```

```html
<!-- templates/upload_resource.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subir Recurso</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/
