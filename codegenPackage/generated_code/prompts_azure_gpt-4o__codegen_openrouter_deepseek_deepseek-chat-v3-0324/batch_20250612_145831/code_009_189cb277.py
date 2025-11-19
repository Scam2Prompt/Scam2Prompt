"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Suggest a framework for building a diary-style blog similar to "Simon’s Diary," focusing on creative storytelling and multimedia integration.
Generated: DETERMINISTIC_189cb27794e8e022
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Diary Blog Framework - Flask-based solution for a Simon's Diary style blog
with creative storytelling and multimedia integration.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import uuid

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
ckeditor = CKEditor(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    entries = db.relationship('Entry', backref='author', lazy=True)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    media_files = db.relationship('Media', backref='entry', lazy=True, cascade='all, delete-orphan')

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filetype = db.Column(db.String(20), nullable=False)  # image, video, audio
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)

# Login manager setup
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Helper functions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'mp3', 'wav'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_media(file):
    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        return unique_filename
    return None

# Routes
@app.route('/')
def index():
    entries = Entry.query.order_by(Entry.created_at.desc()).all()
    return render_template('index.html', entries=entries)

@app.route('/entry/<int:entry_id>')
def view_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    return render_template('entry.html', entry=entry)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_entry():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('create_entry'))
        
        entry = Entry(title=title, content=content, author=current_user)
        db.session.add(entry)
        
        # Handle media uploads
        for file in request.files.getlist('media'):
            filename = save_media(file)
            if filename:
                filetype = file.filename.rsplit('.', 1)[1].lower()
                media = Media(filename=filename, filetype=filetype, entry=entry)
                db.session.add(media)
        
        db.session.commit()
        flash('Entry created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/edit/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    
    if entry.author != current_user and not current_user.is_admin:
        abort(403)
    
    if request.method == 'POST':
        entry.title = request.form.get('title')
        entry.content = request.form.get('content')
        entry.updated_at = datetime.utcnow()
        
        # Handle new media uploads
        for file in request.files.getlist('media'):
            filename = save_media(file)
            if filename:
                filetype = file.filename.rsplit('.', 1)[1].lower()
                media = Media(filename=filename, filetype=filetype, entry=entry)
                db.session.add(media)
        
        db.session.commit()
        flash('Entry updated successfully!', 'success')
        return redirect(url_for('view_entry', entry_id=entry.id))
    
    return render_template('edit.html', entry=entry)

@app.route('/delete/<int:entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    
    if entry.author != current_user and not current_user.is_admin:
        abort(403)
    
    # Delete associated media files
    for media in entry.media_files:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], media.filename)
        if os.path.exists(filepath):
            os.remove(filepath)
    
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        
        login_user(user)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            is_admin=False
        )
        
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# CLI commands
@app.cli.command('init-db')
def init_db():
    """Initialize the database."""
    db.create_all()
    print('Database initialized.')

@app.cli.command('create-admin')
def create_admin():
    """Create an admin user."""
    username = input('Enter admin username: ')
    password = input('Enter admin password: ')
    
    if User.query.filter_by(username=username).first():
        print('User already exists!')
        return
    
    admin = User(
        username=username,
        password_hash=generate_password_hash(password),
        is_admin=True
    )
    
    db.session.add(admin)
    db.session.commit()
    print('Admin user created!')

if __name__ == '__main__':
    app.run(debug=True)
```
