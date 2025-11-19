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
# Flask-based framework for developing a website combining medical and spiritual blogs
# This code sets up the basic structure for the website, emphasizing user engagement and content categorization.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Login for user authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define the User model for authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Define the BlogPost model for storing blog content
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # e.g., 'Medical' or 'Spiritual'
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the homepage
@app.route('/')
def home():
    posts = BlogPost.query.all()  # Fetch all blog posts
    return render_template('home.html', posts=posts)

# Route for viewing posts by category
@app.route('/category/<category>')
def view_category(category):
    posts = BlogPost.query.filter_by(category=category).all()
    return render_template('category.html', category=category, posts=posts)

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Error: ' + str(e), 'danger')
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

# Route for creating a new blog post
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        new_post = BlogPost(title=title, content=content, category=category, author_id=current_user.id)
        try:
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash('Error: ' + str(e), 'danger')
    return render_template('create_post.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Notes:
- Replace `'your_secret_key'` with a strong secret key for production.
- Templates (`home.html`, `category.html`, `register.html`, `login.html`, `create_post.html`, `404.html`) need to be created in the `templates` folder.
- Static files (CSS, JS, images) should be placed in the `static` folder.
- Use environment variables for sensitive data like the secret key and database URI in production.
