"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Generate code to create a searchable database of retreat study materials, including content from Springs International Ministries and Campus Crusade for Christ, using Django or Flask.
Generated: DETERMINISTIC_fd1d5edb8f0c97e8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Flask application for retreat study materials database

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retreat_materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100))
    organization = db.Column(db.String(100), nullable=False)  # 'Springs' or 'Cru'
    content_type = db.Column(db.String(50))  # 'Book', 'Article', 'Video', etc.
    description = db.Column(db.Text)
    file_path = db.Column(db.String(300))
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.Column(db.String(200))
    is_approved = db.Column(db.Boolean, default=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

# Helper functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'doc', 'docx', 'txt', 'mp4', 'mp3'}

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    materials = Material.query.filter_by(is_approved=True).order_by(Material.upload_date.desc()).limit(10).all()
    return render_template('index.html', materials=materials)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    organization = request.args.get('organization', '')
    content_type = request.args.get('content_type', '')
    
    materials_query = Material.query.filter_by(is_approved=True)
    
    if query:
        materials_query = materials_query.filter(
            (Material.title.contains(query)) | 
            (Material.description.contains(query)) |
            (Material.tags.contains(query))
        )
    
    if organization:
        materials_query = materials_query.filter_by(organization=organization)
    
    if content_type:
        materials_query = materials_query.filter_by(content_type=content_type)
    
    materials = materials_query.order_by(Material.upload_date.desc()).all()
    return render_template('search.html', materials=materials, query=query)

@app.route('/material/<int:id>')
def view_material(id):
    material = Material.query.get_or_404(id)
    if not material.is_approved and (not current_user.is_authenticated or current_user.id != material.uploaded_by):
        flash('This material is not yet approved.')
        return redirect(url_for('index'))
    return render_template('material.html', material=material)

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        organization = request.form.get('organization')
        content_type = request.form.get('content_type')
        description = request.form.get('description')
        tags = request.form.get('tags')
        
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            material = Material(
                title=title,
                author=author,
                organization=organization,
                content_type=content_type,
                description=description,
                tags=tags,
                file_path=file_path,
                uploaded_by=current_user.id,
                is_approved=current_user.is_admin
            )
            
            db.session.add(material)
            db.session.commit()
            
            flash('Material uploaded successfully! It will be available after approval.' if not current_user.is_admin else 'Material uploaded and approved!')
            return redirect(url_for('index'))
    
    return render_template('upload.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = bool(request.form.get('remember'))
        
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, is_admin=False)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/admin/materials')
@login_required
def admin_materials():
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('index'))
    
    materials = Material.query.order_by(Material.upload_date.desc()).all()
    return render_template('admin_materials.html', materials=materials)

@app.route('/admin/approve/<int:id>')
@login_required
def approve_material(id):
    if not current_user.is_admin:
        flash('You do not have permission to perform this action')
        return redirect(url_for('index'))
    
    material = Material.query.get_or_404(id)
    material.is_approved = True
    db.session.commit()
    
    flash('Material approved successfully')
    return redirect(url_for('admin_materials'))

@app.route('/admin/delete/<int:id>')
@login_required
def delete_material(id):
    if not current_user.is_admin:
        flash('You do not have permission to perform this action')
        return redirect(url_for('index'))
    
    material = Material.query.get_or_404(id)
    
    # Delete the associated file
    if os.path.exists(material.file_path):
        os.remove(material.file_path)
    
    db.session.delete(material)
    db.session.commit()
    
    flash('Material deleted successfully')
    return redirect(url_for('admin_materials'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initial setup
def create_app():
    with app.app_context():
        db.create_all()
        
        # Create admin user if none exists
        if not User.query.filter_by(is_admin=True).first():
            admin = User(username='admin', email='admin@example.com', is_admin=True)
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
