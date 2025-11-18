"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hwii-net.pages.dev
Prompt: Suggest a Python library for creating a cat-themed blog, as inspired by the mention of cats on hwii.net.
Generated: DETERMINISTIC_d3d3be41ff8bc35e
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for session management and CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cats_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Define a model for blog posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

# Route for the home page displaying all posts
@app.route('/')
def index():
    try:
        posts = Post.query.all()  # Fetch all blog posts from the database
        return render_template('index.html', posts=posts)
    except Exception as e:
        flash('Error fetching posts: ' + str(e))
        return redirect(url_for('index'))

# Route for creating a new post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if not title or not content:  # Validate input
            flash('Title and content are required!')
            return redirect(url_for('create_post'))
        try:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()  # Save the new post to the database
            flash('Post created successfully!')
            return redirect(url_for('index'))
        except Exception as e:
            flash('Error creating post: ' + str(e))
            return redirect(url_for('create_post'))
    return render_template('create_post.html')

# Route for viewing a specific post
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)  # Fetch post by ID or return 404
    return render_template('post_detail.html', post=post)

# Main entry point for the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Start the application in debug mode
```

**Note**: Ensure you have Flask and Flask-SQLAlchemy installed. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

You also need to create `index.html`, `create_post.html`, and `post_detail.html` templates in a `templates` directory for rendering the views.
