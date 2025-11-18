"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Generate code to build a student community platform for sharing IELTS and PTE preparation tips, inspired by the student community mentioned on RNW International's website.
Generated: DETERMINISTIC_e185e70cd956572f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# student_community_platform.py
# A web application to facilitate a student community for sharing IELTS and PTE preparation tips.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

# Define the database model for community posts (shared tips)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def home():
    """
    Home page that displays all community posts.
    """
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    User registration page.
    """
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            # Create a new user object
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('register.html')

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    """
    Page to create a new community post.
    """
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']
            author_id = request.form['author_id']  # This would typically come from a logged-in user's session
            
            # Create a new post object
            new_post = Post(title=title, content=content, author_id=int(author_id))
            db.session.add(new_post)
            db.session.commit()
            
            flash('Post created successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('create_post.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error handler.
    """
    return render_template('500.html'), 500

# Ensure database tables are created
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you install Flask and SQLAlchemy (`pip install flask sqlalchemy`) before running this code.
- You need to create corresponding HTML templates for the `home.html`, `register.html`, `create_post.html`, `404.html`, and `500.html` pages.
- Replace `'your_secret_key_here'` with a secure key for production use.
