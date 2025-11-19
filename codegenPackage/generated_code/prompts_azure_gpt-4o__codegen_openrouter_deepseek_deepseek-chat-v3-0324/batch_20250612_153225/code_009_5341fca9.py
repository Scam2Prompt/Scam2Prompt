"""
Generated Code Metadata:
========================
Original URL: https://nucleicinsights.com
Prompt: Using Python Flask, create a backend for a portfolio website that includes sections for professional skills, work experience, and a blog, inspired by Umama Shahid's design.
Generated: DETERMINISTIC_5341fca9bd3f4bdc
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    end_date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    current = db.Column(db.Boolean, default=False)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('posts', lazy=True))

# Initialize database
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    skills = Skill.query.all()
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    blog_posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).limit(3).all()
    return render_template('index.html', skills=skills, experiences=experiences, blog_posts=blog_posts)

@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog_post.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
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

# Admin routes
@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    return render_template('admin/dashboard.html')

@app.route('/admin/skills')
@login_required
def manage_skills():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    skills = Skill.query.all()
    return render_template('admin/skills.html', skills=skills)

@app.route('/admin/skills/add', methods=['POST'])
@login_required
def add_skill():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    name = request.form['name']
    proficiency = request.form['proficiency']
    category = request.form['category']
    
    skill = Skill(name=name, proficiency=proficiency, category=category)
    db.session.add(skill)
    db.session.commit()
    flash('Skill added successfully', 'success')
    return redirect(url_for('manage_skills'))

@app.route('/admin/skills/delete/<int:id>')
@login_required
def delete_skill(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill deleted successfully', 'success')
    return redirect(url_for('manage_skills'))

@app.route('/admin/experience')
@login_required
def manage_experience():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    experiences = Experience.query.all()
    return render_template('admin/experience.html', experiences=experiences)

@app.route('/admin/experience/add', methods=['POST'])
@login_required
def add_experience():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    title = request.form['title']
    company = request.form['company']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    description = request.form['description']
    current = 'current' in request.form
    
    experience = Experience(
        title=title,
        company=company,
        start_date=start_date,
        end_date=end_date,
        description=description,
        current=current
    )
    db.session.add(experience)
    db.session.commit()
    flash('Experience added successfully', 'success')
    return redirect(url_for('manage_experience'))

@app.route('/admin/experience/delete/<int:id>')
@login_required
def delete_experience(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    experience = Experience.query.get_or_404(id)
    db.session.delete(experience)
    db.session.commit()
    flash('Experience deleted successfully', 'success')
    return redirect(url_for('manage_experience'))

@app.route('/admin/blog')
@login_required
def manage_blog():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    posts = BlogPost.query.all()
    return render_template('admin/blog.html', posts=posts)

@app.route('/admin/blog/add', methods=['POST'])
@login_required
def add_blog_post():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    title = request.form['title']
    content = request.form['content']
    
    post = BlogPost(title=title, content=content, author_id=current_user.id)
    db.session.add(post)
    db.session.commit()
    flash('Blog post added successfully', 'success')
    return redirect(url_for('manage_blog'))

@app.route('/admin/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blog_post(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    post = BlogPost.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Blog post updated successfully', 'success')
        return redirect(url_for('manage_blog'))
    
    return render_template('admin/edit_blog_post.html', post=post)

@app.route('/admin/blog/delete/<int:id>')
@login_required
def delete_blog_post(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Blog post deleted successfully', 'success')
    return redirect(url_for('manage_blog'))

# API Endpoints
@app.route('/api/skills')
def api_skills():
    skills = Skill.query.all()
    return jsonify([{
        'id': skill.id,
        'name': skill.name,
        'proficiency': skill.proficiency,
        'category': skill.category
    } for skill in skills])

@app.route('/api/experience')
def api_experience():
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    return jsonify
