"""
Generated Code Metadata:
========================
Original URL: https://immediate-affinity.com
Prompt: Write a comprehensive guide on building a website that provides investment education, including topics such as risk management, emotional decision-making, and tax implications.
Generated: DETERMINISTIC_f6f19297626c4241
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_education_website.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
from markdown import markdown

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///investment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
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
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'risk', 'tax', 'psychology'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('articles', lazy=True))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)  # e.g., 'beginner', 'intermediate', 'advanced'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CourseModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    course = db.relationship('Course', backref=db.backref('modules', lazy=True))

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    """Render the home page with featured content."""
    featured_articles = Article.query.order_by(Article.created_at.desc()).limit(3).all()
    featured_courses = Course.query.order_by(Course.created_at.desc()).limit(2).all()
    return render_template('home.html', 
                         articles=featured_articles, 
                         courses=featured_courses)

@app.route('/articles')
def articles():
    """List all articles with filtering options."""
    category = request.args.get('category', 'all')
    query = Article.query
    
    if category != 'all':
        query = query.filter_by(category=category)
    
    articles = query.order_by(Article.created_at.desc()).all()
    return render_template('articles.html', articles=articles, category=category)

@app.route('/article/<int:article_id>')
def view_article(article_id):
    """View a single article."""
    article = Article.query.get_or_404(article_id)
    html_content = markdown(article.content)
    return render_template('article.html', article=article, content=html_content)

@app.route('/courses')
def courses():
    """List all available courses."""
    courses = Course.query.order_by(Course.created_at.desc()).all()
    return render_template('courses.html', courses=courses)

@app.route('/course/<int:course_id>')
@login_required
def view_course(course_id):
    """View a course and its modules."""
    course = Course.query.get_or_404(course_id)
    modules = CourseModule.query.filter_by(course_id=course_id).order_by(CourseModule.order).all()
    return render_template('course.html', course=course, modules=modules)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = bool(request.form.get('remember'))
        
        user = User.query.filter_by(username=username).first()
        
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Handle user logout."""
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle new user registration."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
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
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Admin routes
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """Admin dashboard (requires admin privileges)."""
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('home'))
    
    return render_template('admin/dashboard.html')

@app.route('/admin/create-article', methods=['GET', 'POST'])
@login_required
def create_article():
    """Create a new article (admin only)."""
    if not current_user.is_admin:
        flash('You do not have permission to access this page')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        
        if not title or not content or not category:
            flash('Please fill all fields')
            return redirect(url_for('create_article'))
        
        article = Article(
            title=title,
            content=content,
            category=category,
            author_id
