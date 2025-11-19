"""
Generated Code Metadata:
========================
Original URL: https://healthwithdiagnostics.com
Prompt: What are some best practices for creating a website about health and wellness, like healthwithdiagnostics.com, that incorporates expert speak, awareness campaigns, and articles on various medical topics?
Generated: DETERMINISTIC_f187537b57c53abc
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based website for health and wellness content
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from datetime import datetime
from markdown import markdown

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health.db'
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
    is_expert = db.Column(db.Boolean, default=False)
    bio = db.Column(db.Text)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref='articles')
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_featured = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50))
    image_url = db.Column(db.String(200))

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    image_url = db.Column(db.String(200))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    featured_articles = Article.query.filter_by(is_featured=True).order_by(Article.published_at.desc()).limit(3).all()
    active_campaigns = Campaign.query.filter_by(is_active=True).order_by(Campaign.start_date.desc()).limit(2).all()
    return render_template('index.html', 
                          featured_articles=featured_articles,
                          active_campaigns=active_campaigns)

@app.route('/articles')
def articles():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    articles = Article.query.order_by(Article.published_at.desc()).paginate(page=page, per_page=per_page)
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    article.content = markdown(article.content)  # Convert markdown to HTML
    return render_template('article_detail.html', article=article)

@app.route('/campaigns')
def campaigns():
    campaigns = Campaign.query.order_by(Campaign.start_date.desc()).all()
    return render_template('campaigns.html', campaigns=campaigns)

@app.route('/experts')
def experts():
    experts = User.query.filter_by(is_expert=True).all()
    return render_template('experts.html', experts=experts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_expert:
        return redirect(url_for('index'))
    
    user_articles = Article.query.filter_by(author_id=current_user.id).order_by(Article.published_at.desc()).all()
    return render_template('dashboard.html', articles=user_articles)

@app.route('/create-article', methods=['GET', 'POST'])
@login_required
def create_article():
    if not current_user.is_expert:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        excerpt = request.form['excerpt']
        category = request.form['category']
        is_featured = 'is_featured' in request.form
        
        article = Article(
            title=title,
            content=content,
            excerpt=excerpt,
            author_id=current_user.id,
            is_featured=is_featured,
            category=category
        )
        db.session.add(article)
        db.session.commit()
        flash('Article published successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('create_article.html')

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

# CLI Commands
@app.cli.command('init-db')
def init_db():
    """Initialize the database."""
    db.create_all()
    print('Database initialized.')

@app.cli.command('create-admin')
def create_admin():
    """Create an admin user."""
    username = input('Enter username: ')
    email = input('Enter email: ')
    password = input('Enter password: ')
    
    user = User(username=username, email=email, is_expert=True)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    print('Admin user created.')

if __name__ == '__main__':
    app.run(debug=True)
```
