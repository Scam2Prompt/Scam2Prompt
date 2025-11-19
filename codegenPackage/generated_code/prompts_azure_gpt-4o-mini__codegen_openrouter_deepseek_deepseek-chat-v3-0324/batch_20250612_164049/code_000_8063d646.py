"""
Generated Code Metadata:
========================
Original URL: https://oeg-group.com
Prompt: Generate code for a web application that showcases outdoor environment design projects, focusing on user collaboration and creativity.
Generated: DETERMINISTIC_8063d646dc2f1ce0
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Outdoor Environment Design Showcase Web Application

```python
# app.py - Main application file for Outdoor Design Showcase

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///design_showcase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.Text)
    avatar = db.Column(db.String(120))
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    
    projects = db.relationship('Project', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(120))
    design_type = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    images = db.relationship('ProjectImage', backref='project', lazy=True, cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='project', lazy=True, cascade='all, delete-orphan')
    
    likes = db.relationship('Like', backref='project', lazy=True, cascade='all, delete-orphan')

class ProjectImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    caption = db.Column(db.String(200))
    is_primary = db.Column(db.Boolean, default=False)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# Utility functions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filename
    return None

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.created_at.desc()).limit(6).all()
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projects():
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.created_at.desc()).paginate(page=page, per_page=9)
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    if request.method == 'POST':
        try:
            title = request.form['title']
            description = request.form['description']
            location = request.form['location']
            design_type = request.form['design_type']
            
            project = Project(
                title=title,
                description=description,
                location=location,
                design_type=design_type,
                user_id=current_user.id
            )
            db.session.add(project)
            db.session.commit()
            
            # Handle image uploads
            files = request.files.getlist('images')
            for i, file in enumerate(files):
                filename = save_uploaded_file(file)
                if filename:
                    is_primary = (i == 0)  # First image is primary
                    image = ProjectImage(
                        filename=filename,
                        is_primary=is_primary,
                        project_id=project.id
                    )
                    db.session.add(image)
            
            db.session.commit()
            flash('Project created successfully!', 'success')
            return redirect(url_for('project_detail', project_id=project.id))
        except Exception as e:
            db.session.rollback()
            flash('Error creating project: ' + str(e), 'error')
    
    return render_template('create_project.html')

@app.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    if project.author.id != current_user.id:
        flash('You can only edit your own projects', 'error')
        return redirect(url_for('project_detail', project_id=project.id))
    
    if request.method == 'POST':
        try:
            project.title = request.form['title']
            project.description = request.form['description']
            project.location = request.form['location']
            project.design_type = request.form['design_type']
            
            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('project_detail', project_id=project.id))
        except Exception as e:
            db.session.rollback()
            flash('Error updating project: ' + str(e), 'error')
    
    return render_template('edit_project.html', project=project)

@app.route('/delete_project/<int:project_id>', methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    if project.author.id != current_user.id:
        flash('You can only delete your own projects', 'error')
        return redirect(url_for('project_detail', project_id=project.id))
    
    try:
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting project: ' + str(e), 'error')
    
    return redirect(url_for('projects'))

@app.route('/add_comment/<int:project_id>', methods=['POST'])
@login_required
def add_comment(project_id):
    project = Project.query.get_or_404(project_id)
    content = request.form.get('content')
    
    if not content:
        flash('Comment cannot be empty', 'error')
        return redirect(url_for('project_detail', project_id=project.id))
    
    try:
        comment = Comment(
            content=content,
            user_id=current_user.id,
            project_id=project.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Comment added successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error adding comment: ' + str(e), 'error')
    
    return redirect(url_for('project_detail', project_id
