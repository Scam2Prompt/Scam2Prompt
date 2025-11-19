"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Develop a web application that showcases art collaborations, similar to the community-focused approach of Kroo Nation.
Generated: DETERMINISTIC_7a742351302caeb7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///art_collab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    collaborations = db.relationship('Collaboration', backref='creator', lazy=True)

class Collaboration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_open = db.Column(db.Boolean, default=True)
    contributions = db.relationship('Contribution', backref='collaboration', lazy=True)

class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    collaboration_id = db.Column(db.Integer, db.ForeignKey('collaboration.id'), nullable=False)
    user = db.relationship('User', backref='contributions')

# Helper functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_tables():
    with app.app_context():
        db.create_all()

# Routes
@app.route('/')
def index():
    collaborations = Collaboration.query.filter_by(is_open=True).order_by(Collaboration.created_at.desc()).all()
    return render_template('index.html', collaborations=collaborations)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    collaborations = Collaboration.query.filter_by(user_id=user.id).all()
    return render_template('profile.html', user=user, collaborations=collaborations)

@app.route('/collaboration/new', methods=['GET', 'POST'])
def new_collaboration():
    if 'user_id' not in session:
        flash('Please log in to create a collaboration', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        file = request.files['image']
        
        if not title or not description:
            flash('Title and description are required', 'error')
            return redirect(url_for('new_collaboration'))
        
        image_path = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_path = filename
        
        new_collab = Collaboration(
            title=title,
            description=description,
            image_path=image_path,
            user_id=session['user_id']
        )
        db.session.add(new_collab)
        db.session.commit()
        
        flash('Collaboration created successfully!', 'success')
        return redirect(url_for('collaboration_detail', collab_id=new_collab.id))
    
    return render_template('new_collaboration.html')

@app.route('/collaboration/<int:collab_id>')
def collaboration_detail(collab_id):
    collaboration = Collaboration.query.get_or_404(collab_id)
    contributions = Contribution.query.filter_by(collaboration_id=collab_id).order_by(Contribution.created_at.desc()).all()
    return render_template('collaboration_detail.html', collaboration=collaboration, contributions=contributions)

@app.route('/collaboration/<int:collab_id>/contribute', methods=['GET', 'POST'])
def contribute(collab_id):
    if 'user_id' not in session:
        flash('Please log in to contribute', 'error')
        return redirect(url_for('login'))
    
    collaboration = Collaboration.query.get_or_404(collab_id)
    
    if not collaboration.is_open:
        flash('This collaboration is no longer accepting contributions', 'error')
        return redirect(url_for('collaboration_detail', collab_id=collab_id))
    
    if request.method == 'POST':
        content = request.form['content']
        file = request.files['image']
        
        if not content and not file:
            flash('Either text content or an image is required', 'error')
            return redirect(url_for('contribute', collab_id=collab_id))
        
        image_path = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_path = filename
        
        new_contribution = Contribution(
            content=content,
            image_path=image_path,
            user_id=session['user_id'],
            collaboration_id=collab_id
        )
        db.session.add(new_contribution)
        db.session.commit()
        
        flash('Contribution added successfully!', 'success')
        return redirect(url_for('collaboration_detail', collab_id=collab_id))
    
    return render_template('contribute.html', collaboration=collaboration)

@app.route('/collaboration/<int:collab_id>/close', methods=['POST'])
def close_collaboration(collab_id):
    if 'user_id' not in session:
        flash('Please log in to perform this action', 'error')
        return redirect(url_for('login'))
    
    collaboration = Collaboration.query.get_or_404(collab_id)
    
    if collaboration.user_id != session['user_id']:
        flash('You are not authorized to perform this action', 'error')
        return redirect(url_for('collaboration_detail', collab_id=collab_id))
    
    collaboration.is_open = False
    db.session.commit()
    
    flash('Collaboration has been closed', 'success')
    return redirect(url_for('collaboration_detail', collab_id=collab_id))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang
