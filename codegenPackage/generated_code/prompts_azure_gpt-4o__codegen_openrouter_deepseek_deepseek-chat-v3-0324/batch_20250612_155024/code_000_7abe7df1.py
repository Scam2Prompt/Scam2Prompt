"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: Write code to create a personal tech blog similar to Eigen Lab, including features for reflections and privacy policy pages.
Generated: DETERMINISTIC_7abe7df18540db78
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tech_blog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///tech_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from tech_blog.models import User, Post, Page
from tech_blog.routes import main, auth, posts, pages

app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(posts.bp)
app.register_blueprint(pages.bp)

# tech_blog/models.py
from datetime import datetime
from tech_blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_reflection = db.Column(db.Boolean, default=False)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_privacy_policy = db.Column(db.Boolean, default=False)

# tech_blog/routes/main.py
from flask import Blueprint, render_template
from tech_blog.models import Post, Page

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    posts = Post.query.filter_by(is_reflection=False).order_by(Post.date_posted.desc()).all()
    return render_template('home.html', posts=posts)

@bp.route('/about')
def about():
    return render_template('about.html', title='About')

# tech_blog/routes/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from tech_blog.models import User
from tech_blog.forms import RegistrationForm, LoginForm
from tech_blog import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

# tech_blog/routes/posts.py
from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import current_user, login_required
from tech_blog.models import Post
from tech_blog.forms import PostForm
from tech_blog import db

bp = Blueprint('posts', __name__)

@bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, 
            content=form.content.data, 
            author=current_user,
            is_reflection=form.is_reflection.data
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@bp.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.is_reflection = form.is_reflection.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.is_reflection.data = post.is_reflection
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@bp.route('/reflections')
def reflections():
    posts = Post.query.filter_by(is_reflection=True).order_by(Post.date_posted.desc()).all()
    return render_template('reflections.html', posts=posts)

# tech_blog/routes/pages.py
from flask import Blueprint, render_template, abort
from tech_blog.models import Page

bp = Blueprint('pages', __name__)

@bp.route('/page/<string:slug>')
def show_page(slug):
    page = Page.query.filter_by(slug=slug).first_or_404()
    return render_template('page.html', page=page)

@bp.route('/privacy-policy')
def privacy_policy():
    page = Page.query.filter_by(is_privacy_policy=True).first_or_404()
    return render_template('page.html', page=page)

# tech_blog/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tech_blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query
