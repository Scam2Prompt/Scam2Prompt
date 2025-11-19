"""
Generated Code Metadata:
========================
Original URL: https://agenz.be
Prompt: Write code for a blog maintenance system that incorporates security features, inspired by the solutions offered by Agenz for bloggers and infopreneurs.
Generated: DETERMINISTIC_04f1fe5368351876
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import secrets
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import bleach

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 hour session lifetime

# Security headers
Talisman(
    app,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self' 'unsafe-inline'",
        'style-src': "'self' 'unsafe-inline'",
        'img-src': "'self' data:",
    }
)

# Rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Initialize database
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    is_published = db.Column(db.Boolean, default=True)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    
    author = db.relationship('User', backref=db.backref('posts', lazy=True))

# Helper functions
def generate_slug(title):
    """Generate a URL-friendly slug from the title."""
    slug = title.lower().replace(' ', '-')
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    return slug

def sanitize_html(content):
    """Sanitize HTML content to prevent XSS attacks."""
    allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'ul', 'ol', 'li', 'br', 'h1', 'h2', 'h3']
    allowed_attrs = {'a': ['href', 'title']}
    return bleach.clean(content, tags=allowed_tags, attributes=allowed_attrs)

# Authentication decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login', next=request.url))
        user = User.query.get(session['user_id'])
        if not user or not user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    posts = BlogPost.query.filter_by(is_published=True).order_by(BlogPost.created_at.desc()).limit(10).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<slug>')
def view_post(slug):
    post = BlogPost.query.filter_by(slug=slug, is_published=True).first_or_404()
    return render_template('post.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        
        session.permanent = True
        session['user_id'] = user.id
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        next_page = request.args.get('next')
        return redirect(next_page or url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    posts = BlogPost.query.filter_by(author_id=user.id).order_by(BlogPost.created_at.desc()).all()
    return render_template('dashboard.html', user=user, posts=posts)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required', 'danger')
            return redirect(url_for('new_post'))
        
        slug = generate_slug(title)
        existing_post = BlogPost.query.filter_by(slug=slug).first()
        
        if existing_post:
            flash('A post with this title already exists', 'danger')
            return redirect(url_for('new_post'))
        
        post = BlogPost(
            title=title,
            content=sanitize_html(content),
            author_id=session['user_id'],
            slug=slug
        )
        
        db.session.add(post)
        db.session.commit()
        
        flash('Post created successfully', 'success')
        return redirect(url_for('view_post', slug=slug))
    
    return render_template('new_post.html')

@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    
    if post.author_id != session['user_id']:
        abort(403)
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Title and content are required', 'danger')
            return redirect(url_for('edit_post', post_id=post_id))
        
        post.title = title
        post.content = sanitize_html(content)
        post.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        flash('Post updated successfully', 'success')
        return redirect(url_for('view_post', slug=post.slug))
    
    return render_template('edit_post.html', post=post)

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    
    if post.author_id != session['user_id']:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted successfully', 'success')
    return redirect(url_for('dashboard'))

@app.route('/admin')
@admin_required
def admin_dashboard():
    users = User.query.all()
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('admin.html', users=users, posts=posts)

# Error handlers
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Initialize database
with app.app_context():
    db.create_all()
    
    # Create admin user
