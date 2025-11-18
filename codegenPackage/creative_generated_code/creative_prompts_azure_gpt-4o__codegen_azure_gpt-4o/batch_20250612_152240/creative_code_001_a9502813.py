"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hwii-net.pages.dev
Prompt: Recommend a library or API for creating a simple blog platform like the one described on hwii.net, with features for casual posts and rants.
Generated: DETERMINISTIC_a950281332a4e45f
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the use of Flask, a lightweight web framework, for building
a simple blog platform with features for casual posts and rants. It includes error handling,
comments, and follows best practices. For database management, SQLite is used as a backend.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy for database operations
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'casual' or 'rant'

    def __repr__(self):
        return f'<BlogPost {self.title}>'


# Route: Home page displaying all blog posts
@app.route('/')
def index():
    try:
        posts = BlogPost.query.all()
        return render_template('index.html', posts=posts)
    except Exception as e:
        flash(f"Error loading posts: {str(e)}", 'danger')
        return render_template('index.html', posts=[])


# Route: Page for adding a new blog post
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']
            category = request.form['category']

            # Validate inputs
            if not title or not content or not category:
                flash('All fields are required.', 'warning')
                return redirect(url_for('add_post'))

            # Create and save the new blog post
            new_post = BlogPost(title=title, content=content, category=category)
            db.session.add(new_post)
            db.session.commit()
            flash('Post added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error adding post: {str(e)}", 'danger')
            return redirect(url_for('add_post'))
    return render_template('add_post.html')


# Route: View a specific blog post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    try:
        post = BlogPost.query.get_or_404(post_id)
        return render_template('view_post.html', post=post)
    except Exception as e:
        flash(f"Error loading post: {str(e)}", 'danger')
        return redirect(url_for('index'))


# Route: Delete a blog post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    try:
        post = BlogPost.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully!', 'success')
    except Exception as e:
        flash(f"Error deleting post: {str(e)}", 'danger')
    return redirect(url_for('index'))


# Create database tables before first request
@app.before_first_request
def create_tables():
    db.create_all()


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
1. **Templates:** You will need corresponding HTML files for rendering (e.g., `index.html`, `add_post.html`, `view_post.html`) in a `templates` directory.
2. **Database:** A SQLite database `blog.db` will be automatically created in the project directory.
3. **Security:** Replace `SECRET_KEY` with a securely generated key before deploying to production.
4. **Dependencies:** Install the required Python packages using `pip install flask flask-sqlalchemy`.
