"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Design a web application that showcases the impact of youth-led environmental projects, integrating features for sharing on social media platforms like Facebook and Instagram.
Generated: DETERMINISTIC_6043a6340aecb1f4
Batch ID: 20250612_155855
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u={request.host_url}project/{project.id": {
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
# app.py - Main application file for the youth-led environmental projects showcase

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import requests
import json

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///projects.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FACEBOOK_APP_ID'] = os.environ.get('FACEBOOK_APP_ID')
app.config['FACEBOOK_APP_SECRET'] = os.environ.get('FACEBOOK_APP_SECRET')
app.config['INSTAGRAM_APP_ID'] = os.environ.get('INSTAGRAM_APP_ID')
app.config['INSTAGRAM_APP_SECRET'] = os.environ.get('INSTAGRAM_APP_SECRET')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    projects = db.relationship('Project', backref='creator', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    impact = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    likes = db.Column(db.Integer, default=0)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.date_created.desc()).limit(6).all()
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projects():
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.date_created.desc()).paginate(page=page, per_page=9)
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        impact = request.form['impact']
        image_url = request.form['image_url']
        
        project = Project(
            title=title,
            description=description,
            location=location,
            impact=impact,
            image_url=image_url,
            user_id=current_user.id
        )
        
        db.session.add(project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('project_detail', project_id=project.id))
    
    return render_template('add_project.html')

@app.route('/like_project/<int:project_id>', methods=['POST'])
@login_required
def like_project(project_id):
    project = Project.query.get_or_404(project_id)
    project.likes += 1
    db.session.commit()
    return redirect(url_for('project_detail', project_id=project.id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/share/facebook/<int:project_id>')
@login_required
def share_facebook(project_id):
    project = Project.query.get_or_404(project_id)
    share_url = f"https://www.facebook.com/sharer/sharer.php?u={request.host_url}project/{project.id}"
    return redirect(share_url)

@app.route('/share/instagram/<int:project_id>')
@login_required
def share_instagram(project_id):
    project = Project.query.get_or_404(project_id)
    # Instagram doesn't have a direct share API, so we redirect to their app
    return redirect(f"instagram://library?AssetPath={request.host_url}project/{project.id}")

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', False))
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Youth Environmental Projects</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-success">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">Youth Environmental Projects</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('index') }}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('projects') }}">Projects</a>
                    </li>
                    {% if current_user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('add_project') }}">Add Project</a>
                    </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    {% if current_user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('logout') }}">Logout</
