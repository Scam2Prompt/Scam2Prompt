"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Suggest a framework for developing a website that emphasizes real skills and project outcomes in technology education.
Generated: DETERMINISTIC_5a7542ae1b697d38
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tech Education Portfolio Website Framework

A Flask-based web application framework for showcasing technology education
with emphasis on real skills and project outcomes.

Features:
- Project showcase
- Skill demonstration
- User authentication for educators
- Responsive design
- Database integration
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default='educator')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'educator':
        return redirect(url_for('index'))
    projects = Project.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', projects=projects)

@app.route('/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
    if current_user.role != 'educator':
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        skills = request.form['skills']
        github_url = request.form['github_url']
        demo_url = request.form['demo_url']
        
        project = Project(
            title=title,
            description=description,
            skills=skills,
            github_url=github_url,
            demo_url=demo_url,
            user_id=current_user.id
        )
        
        db.session.add(project)
        db.session.commit()
        flash('Project added successfully')
        return redirect(url_for('dashboard'))
    
    return render_template('add_project.html')

@app.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    if project.user_id != current_user.id:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.github_url = request.form['github_url']
        project.demo_url = request.form['demo_url']
        
        db.session.commit()
        flash('Project updated successfully')
        return redirect(url_for('dashboard'))
    
    return render_template('edit_project.html', project=project)

@app.route('/delete_project/<int:project_id>', methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    if project.user_id != current_user.id:
        return redirect(url_for('index'))
    
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully')
    return redirect(url_for('dashboard'))

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize database
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
