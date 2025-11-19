"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Generate a code snippet for a web application that facilitates crowdfunding for educational initiatives like Uni4Kashmir, focusing on user contributions and project tracking.
Generated: DETERMINISTIC_190daf8332a76930
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///edu_fund.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    contributions = db.relationship('Contribution', backref='contributor', lazy=True)
    projects = db.relationship('Project', backref='creator', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contributions = db.relationship('Contribution', backref='project', lazy=True)

class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    contributed_at = db.Column(db.DateTime, default=datetime.utcnow)
    contributor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    projects = Project.query.order_by(Project.created_at.desc()).limit(3).all()
    return render_template('index.html', projects=projects)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'error')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already exists!', 'error')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash('Invalid username or password!', 'error')
            return redirect(url_for('login'))

        login_user(user)
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_projects = Project.query.filter_by(creator_id=current_user.id).all()
    user_contributions = Contribution.query.filter_by(contributor_id=current_user.id).all()
    return render_template('dashboard.html', projects=user_projects, contributions=user_contributions)

@app.route('/projects')
def projects():
    all_projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects.html', projects=all_projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    contributions = Contribution.query.filter_by(project_id=project_id).order_by(Contribution.contributed_at.desc()).all()
    return render_template('project_detail.html', project=project, contributions=contributions)

@app.route('/create_project', methods=['GET', 'POST'])
@login_required
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        target_amount = float(request.form['target_amount'])
        deadline_str = request.form['deadline']

        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format!', 'error')
            return redirect(url_for('create_project'))

        if deadline <= datetime.utcnow():
            flash('Deadline must be in the future!', 'error')
            return redirect(url_for('create_project'))

        new_project = Project(
            title=title,
            description=description,
            target_amount=target_amount,
            deadline=deadline,
            creator_id=current_user.id
        )

        db.session.add(new_project)
        db.session.commit()

        flash('Project created successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_project.html')

@app.route('/contribute/<int:project_id>', methods=['GET', 'POST'])
@login_required
def contribute(project_id):
    project = Project.query.get_or_404(project_id)

    if request.method == 'POST':
        amount = float(request.form['amount'])

        if amount <= 0:
            flash('Contribution amount must be positive!', 'error')
            return redirect(url_for('contribute', project_id=project_id))

        if project.current_amount + amount > project.target_amount:
            flash('Contribution exceeds project target!', 'error')
            return redirect(url_for('contribute', project_id=project_id))

        new_contribution = Contribution(
            amount=amount,
            contributor_id=current_user.id,
            project_id=project_id
        )

        project.current_amount += amount
        db.session.add(new_contribution)
        db.session.commit()

        flash('Thank you for your contribution!', 'success')
        return redirect(url_for('project_detail', project_id=project_id))

    return render_template('contribute.html', project=project)

# API Endpoints
@app.route('/api/projects')
def api_projects():
    projects = Project.query.all()
    projects_data = [{
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'target_amount': project.target_amount,
        'current_amount': project.current_amount,
        'deadline': project.deadline.isoformat(),
        'creator': project.creator.username
    } for project in projects]
    return jsonify(projects_data)

@app.route('/api/project/<int:project_id>')
def api_project(project_id):
    project = Project.query.get_or_404(project_id)
    project_data = {
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'target_amount': project.target_amount,
        'current_amount': project.current_amount,
        'deadline': project.deadline.isoformat(),
        'creator': project.creator.username,
        'contributions': [{
            'amount': contribution.amount,
            'contributor': contribution.contributor.username,
            'contributed_at': contribution.contributed_at.isoformat()
        } for contribution in project.contributions]
    }
    return jsonify(project_data)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

# Run the application
if __name__ == '__main__':
    create_tables
