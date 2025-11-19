"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theneuraluniverse.com
Prompt: Suggest a framework for developing a website that combines medical and spiritual blogs like The Neural Universe, emphasizing user engagement and content categorization.
Generated: DETERMINISTIC_a53fc06177b4efd4
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Application configuration
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Use SQLite for demonstration purposes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize LoginManager for user authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    """Model for user accounts."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class BlogPost(db.Model):
    """Model for blog posts."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # E.g., 'Medical' or 'Spiritual'
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    """Home page displaying blog posts."""
    medical_posts = BlogPost.query.filter_by(category='Medical').all()
    spiritual_posts = BlogPost.query.filter_by(category='Spiritual').all()
    return render_template('home.html', medical_posts=medical_posts, spiritual_posts=spiritual_posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Replace with hashed password verification in production
            login_user(user)
            return redirect(url_for('home'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Logout route."""
    logout_user()
    return redirect(url_for('home'))

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create a new blog post."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        
        # Validate user input
        if not title or not content or not category:
            return "Missing fields", 400
        
        # Save blog post to the database
        new_post = BlogPost(title=title, content=content, category=category, author_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('create_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """View a specific blog post."""
    post = BlogPost.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Custom 500 page."""
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Notes:
- Install dependencies using: `pip install flask flask_sqlalchemy flask_login flask_migrate`
- Create the necessary HTML templates (`home.html`, `login.html`, `create_post.html`, `view_post.html`, `404.html`, and `500.html`) for rendering the pages.
