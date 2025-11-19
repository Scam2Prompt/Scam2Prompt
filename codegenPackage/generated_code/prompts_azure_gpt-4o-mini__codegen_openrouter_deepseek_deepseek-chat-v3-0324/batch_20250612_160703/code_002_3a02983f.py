"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: Can you provide a code example for a web application that tracks and showcases revitalization projects in small municipalities, inspired by the initiatives from the Starke Orte Netzwerk?
Generated: DETERMINISTIC_3a02983f09de934a
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
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
from functools import wraps
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database
db = SQLAlchemy(app)

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Database Models
class Municipality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100))
    population = db.Column(db.Integer)
    projects = db.relationship('Project', backref='municipality', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))  # planning, in_progress, completed
    municipality_id = db.Column(db.Integer, db.ForeignKey('municipality.id'), nullable=False)
    image_path = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Helper functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Routes
@app.route('/')
def index():
    try:
        projects = Project.query.order_by(Project.created_at.desc()).limit(6).all()
        municipalities = Municipality.query.all()
        return render_template('index.html', projects=projects, municipalities=municipalities)
    except Exception as e:
        app.logger.error(f"Error in index route: {str(e)}")
        flash('An error occurred while loading the page.', 'danger')
        return render_template('index.html', projects=[], municipalities=[])

@app.route('/projects')
def list_projects():
    try:
        projects = Project.query.order_by(Project.created_at.desc()).all()
        return render_template('projects.html', projects=projects)
    except Exception as e:
        app.logger.error(f"Error in list_projects route: {str(e)}")
        flash('An error occurred while loading projects.', 'danger')
        return render_template('projects.html', projects=[])

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        return render_template('project_detail.html', project=project)
    except Exception as e:
        app.logger.error(f"Error in project_detail route: {str(e)}")
        flash('Project not found.', 'danger')
        return redirect(url_for('list_projects'))

@app.route('/municipalities')
def list_municipalities():
    try:
        municipalities = Municipality.query.order_by(Municipality.name).all()
        return render_template('municipalities.html', municipalities=municipalities)
    except Exception as e:
        app.logger.error(f"Error in list_municipalities route: {str(e)}")
        flash('An error occurred while loading municipalities.', 'danger')
        return render_template('municipalities.html', municipalities=[])

@app.route('/municipalities/<int:municipality_id>')
def municipality_projects(municipality_id):
    try:
        municipality = Municipality.query.get_or_404(municipality_id)
        projects = Project.query.filter_by(municipality_id=municipality_id).order_by(Project.created_at.desc()).all()
        return render_template('municipality_projects.html', municipality=municipality, projects=projects)
    except Exception as e:
        app.logger.error(f"Error in municipality_projects route: {str(e)}")
        flash('Municipality not found.', 'danger')
        return redirect(url_for('list_municipalities'))

@app.route('/api/projects')
def api_projects():
    try:
        projects = Project.query.all()
        return jsonify([{
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'municipality': project.municipality.name,
            'status': project.status,
            'image_url': url_for('static', filename=f'uploads/{project.image_path}') if project.image_path else None
        } for project in projects])
    except Exception as e:
        app.logger.error(f"Error in api_projects route: {str(e)}")
        return jsonify({'error': 'An error occurred'}), 500

# Admin routes would be protected with authentication in a production environment
@app.route('/admin/project/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            municipality_id = request.form['municipality_id']
            status = request.form['status']
            
            # Handle dates
            start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date() if request.form['start_date'] else None
            end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date() if request.form['end_date'] else None
            
            # Handle file upload
            image_path = None
            if 'image' in request.files:
                file = request.files['image']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image_path = filename
            
            project = Project(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                status=status,
                municipality_id=municipality_id,
                image_path=image_path
            )
            
            db.session.add(project)
            db.session.commit()
            flash('Project created successfully!', 'success')
            return redirect(url_for('project_detail', project_id=project.id))
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error creating project: {str(e)}")
            flash('An error occurred while creating the project.', 'danger')
    
    municipalities = Municipality.query.order_by(Municipality.name).all()
    return render_template('new_project.html', municipalities=municipalities)

@app.route('/admin/project/<int:project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        try:
            project.title = request.form['title']
            project.description = request.form['description']
            project.municipality_id = request.form['municipality_id']
            project.status = request.form['status']
            
            # Handle dates
            project.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date() if request.form['start_date'] else None
            project.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date() if request.form['end_date'] else None
            
            # Handle file upload
            if 'image' in request.files:
                file = request.files['image']
                if file and allowed_file(file.filename):
                    # Remove old image if exists
                    if project.image_path:
                        try:
                            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project.image_path))
                        except OSError:
                            pass
                    
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    project.image_path = filename
            
            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('project_detail', project_id=project.id))
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error updating project: {str(e)}")
            flash('An error occurred while updating the project.', 'danger')
    
    municipalities = Municipality.query.order_by(Municipality.name).all()
    return render_template('edit_project.html', project=project,
