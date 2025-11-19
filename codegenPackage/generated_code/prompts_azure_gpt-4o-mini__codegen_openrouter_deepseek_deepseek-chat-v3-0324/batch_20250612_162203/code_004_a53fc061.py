"""
Generated Code Metadata:
========================
Original URL: https://theneuraluniverse.com
Prompt: Suggest a framework for developing a website that combines medical and spiritual blogs like The Neural Universe, emphasizing user engagement and content categorization.
Generated: DETERMINISTIC_a53fc06177b4efd4
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based framework for a medical and spiritual blog website
# File: app.py

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from datetime import datetime
import os
from markdown import markdown

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    posts = db.relationship('Post', backref='category', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_html = db.Column(db.Text)
    excerpt = db.Column(db.String(300))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_featured = db.Column(db.Boolean, default=False)
    views = db.Column(db.Integer, default=0)
    tags = db.Column(db.String(200))
    
    @staticmethod
    def on_content_changed(target, value, oldvalue, initiator):
        target.content_html = markdown(value)

db.event.listen(Post.content, 'set', Post.on_content_changed)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_approved = db.Column(db.Boolean, default=False)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    featured_posts = Post.query.filter_by(is_featured=True).order_by(Post.created_at.desc()).limit(3).all()
    medical_posts = Post.query.join(Category).filter(Category.name == 'Medical').order_by(Post.created_at.desc()).limit(3).all()
    spiritual_posts = Post.query.join(Category).filter(Category.name == 'Spiritual').order_by(Post.created_at.desc()).limit(3).all()
    return render_template('index.html', 
                         featured_posts=featured_posts,
                         medical_posts=medical_posts,
                         spiritual_posts=spiritual_posts)

@app.route('/category/<string:category_name>')
def category_posts(category_name):
    category = Category.query.filter_by(name=category_name).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category_id=category.id).order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('category.html', category=category, posts=posts)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    post.views += 1
    db.session.commit()
    
    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('Please login to comment', 'warning')
            return redirect(url_for('login'))
        
        content = request.form.get('content')
        if not content:
            flash('Comment cannot be empty', 'danger')
        else:
            comment = Comment(content=content, post_id=post_id, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            flash('Your comment has been submitted for review', 'success')
            return redirect(url_for('post_detail', post_id=post_id))
    
    comments = Comment.query.filter_by(post_id=post_id, is_approved=True).order_by(Comment.created_at.desc()).all()
    return render_template('post.html', post=post, comments=comments)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
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
            flash('Passwords do not match', 'danger')
        elif User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

# API Endpoints
@app.route('/api/posts')
def api_posts():
    category = request.args.get('category')
    limit = request.args.get('limit', default=10, type=int)
    
    query = Post.query.order_by(Post.created_at.desc())
    if category:
        query = query.join(Category).filter(Category.name == category)
    
    posts = query.limit(limit).all()
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'excerpt': post.excerpt,
        'category': post.category.name,
        'created_at': post.created_at.isoformat(),
        'url': url_for('post_detail', post_id=post.id, _external=True)
    } for post in posts])

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# CLI Commands
@app.cli.command('initdb')
def initdb_command():
    """Initialize the database."""
    db.create_all()
    
    # Create default categories
    categories = [
        ('Medical', 'Articles about neuroscience, psychology, and health'),
        ('Spiritual', 'Articles about consciousness, meditation, and spirituality')
    ]
    
    for name, desc in categories:
        if not Category.query.filter_by(name=name).first():
            category = Category(name=name, description=desc)
            db.session.add(category)
    
    db.session.commit()
    print('Initialized the database.')

if __name__ == '__main__':
    app.run(debug=True)
```
