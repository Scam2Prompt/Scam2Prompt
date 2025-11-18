"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://howtosuecslplasma.org
Prompt: Suggest libraries or frameworks for creating a heavily moderated bulletin board system, as mentioned on "howtosuecslplasma.org", to ensure accurate information sharing about plasma donation lawsuits.
Generated: DETERMINISTIC_3601cd97e14c5dbb
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing required libraries for building a bulletin board system
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Application configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bulletin_board.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Bulletin post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    author = db.relationship('User', backref='posts')

# Load user function for Flask login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for homepage displaying all posts
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

# Route for creating new posts
@app.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            new_post = Post(title=title, content=content, author_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Title and content cannot be empty!', 'danger')
    return render_template('new_post.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username and password cannot be empty!', 'danger')
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'danger')
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

# Error handling for server errors
@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred.", 500

# Main entry point of the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```
