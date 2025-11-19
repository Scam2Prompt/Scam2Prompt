"""
Generated Code Metadata:
========================
Original URL: https://coarco.org
Prompt: "Write a Python script to create a simple web archive for storing and displaying art projects, inspired by the structure of coarco.org's project archive."
Generated: DETERMINISTIC_174ad391517233a9
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Web Archive for Art Projects
Inspired by coarco.org's project archive structure

Features:
- Flask-based web application
- SQLite database for storing projects
- File uploads for project images
- Responsive design with Bootstrap
- Basic authentication for admin functions
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import sqlite3
from functools import wraps

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['DATABASE'] = 'art_archive.db'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database setup
def get_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                year INTEGER,
                medium TEXT,
                image_filename TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        db.commit()

# User model
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    if user:
        return User(user['id'], user['username'])
    return None

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return login_manager.unauthorized()
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    db = get_db()
    projects = db.execute('SELECT * FROM projects ORDER BY created_at DESC').fetchall()
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    db = get_db()
    project = db.execute('SELECT * FROM projects WHERE id = ?', (project_id,)).fetchone()
    if project is None:
        flash('Project not found', 'error')
        return redirect(url_for('index'))
    return render_template('project_detail.html', project=project)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if user and check_password_hash(user['password_hash'], password):
            user_obj = User(user['id'], user['username'])
            login_user(user_obj)
            flash('Logged in successfully', 'success')
            return redirect(url_for('index'))
        
        flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/admin/add_project', methods=['GET', 'POST'])
@admin_required
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        year = request.form['year']
        medium = request.form['medium']
        
        # Handle file upload
        if 'image' not in request.files:
            flash('No file uploaded', 'error')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            db = get_db()
            db.execute(
                'INSERT INTO projects (title, description, year, medium, image_filename) VALUES (?, ?, ?, ?, ?)',
                (title, description, year, medium, filename)
            )
            db.commit()
            flash('Project added successfully', 'success')
            return redirect(url_for('index'))
        
        flash('Invalid file type', 'error')
    
    return render_template('add_project.html')

@app.route('/admin/edit_project/<int:project_id>', methods=['GET', 'POST'])
@admin_required
def edit_project(project_id):
    db = get_db()
    project = db.execute('SELECT * FROM projects WHERE id = ?', (project_id,)).fetchone()
    
    if project is None:
        flash('Project not found', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        year = request.form['year']
        medium = request.form['medium']
        
        # Handle file upload if new file is provided
        if 'image' in request.files and request.files['image'].filename != '':
            file = request.files['image']
            if file and allowed_file(file.filename):
                # Delete old file
                if project['image_filename']:
                    try:
                        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project['image_filename']))
                    except OSError:
                        pass
                
                # Save new file
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                db.execute(
                    'UPDATE projects SET title = ?, description = ?, year = ?, medium = ?, image_filename = ? WHERE id = ?',
                    (title, description, year, medium, filename, project_id)
                )
            else:
                flash('Invalid file type', 'error')
                return redirect(request.url)
        else:
            db.execute(
                'UPDATE projects SET title = ?, description = ?, year = ?, medium = ? WHERE id = ?',
                (title, description, year, medium, project_id)
            )
        
        db.commit()
        flash('Project updated successfully', 'success')
        return redirect(url_for('project_detail', project_id=project_id))
    
    return render_template('edit_project.html', project=project)

@app.route('/admin/delete_project/<int:project_id>', methods=['POST'])
@admin_required
def delete_project(project_id):
    db = get_db()
    project = db.execute('SELECT * FROM projects WHERE id = ?', (project_id,)).fetchone()
    
    if project is None:
        flash('Project not found', 'error')
        return redirect(url_for('index'))
    
    # Delete associated image file
    if project['image_filename']:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], project['image_filename']))
        except OSError:
            pass
    
    db.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    db.commit()
    flash('Project deleted successfully', 'success')
    return redirect(url_for('index'))

# Templates would be in a 'templates' folder
# Static files would be in a 'static' folder

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```
