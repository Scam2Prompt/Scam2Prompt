"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Suggest a structure for an NGO's blog section, focusing on education and community development topics, similar to Youngistaan's blog."
Generated: DETERMINISTIC_a431c52542434103
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Initialize the database
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each post
    title = db.Column(db.String(100), nullable=False)  # Title of the blog post
    content = db.Column(db.Text, nullable=False)  # Content of the blog post
    category = db.Column(db.String(50), nullable=False)  # Category (e.g., Education, Community Development)
    author = db.Column(db.String(50), nullable=False)  # Author of the blog post
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for the post

    def __repr__(self):
        return f"<BlogPost {self.title}>"

# Route to display all blog posts
@app.route('/')
def index():
    try:
        posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()  # Fetch all posts, newest first
        return render_template('index.html', posts=posts)
    except Exception as e:
        flash(f"An error occurred while fetching posts: {str(e)}", "danger")
        return render_template('index.html', posts=[])

# Route to display a single blog post
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    try:
        post = BlogPost.query.get_or_404(post_id)  # Fetch the post or return 404
        return render_template('post_detail.html', post=post)
    except Exception as e:
        flash(f"An error occurred while fetching the post: {str(e)}", "danger")
        return redirect(url_for('index'))

# Route to create a new blog post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']
            category = request.form['category']
            author = request.form['author']

            # Validate input
            if not title or not content or not category or not author:
                flash("All fields are required.", "warning")
                return redirect(url_for('create_post'))

            # Create a new blog post
            new_post = BlogPost(title=title, content=content, category=category, author=author)
            db.session.add(new_post)
            db.session.commit()
            flash("Blog post created successfully!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"An error occurred while creating the post: {str(e)}", "danger")
            return redirect(url_for('create_post'))
    return render_template('create_post.html')

# Route to delete a blog post
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    try:
        post = BlogPost.query.get_or_404(post_id)  # Fetch the post or return 404
        db.session.delete(post)
        db.session.commit()
        flash("Blog post deleted successfully!", "success")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"An error occurred while deleting the post: {str(e)}", "danger")
        return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Notes:
- This code uses Flask for the web framework and SQLAlchemy for database management.
- Templates (`index.html`, `post_detail.html`, `create_post.html`) need to be created separately in the `templates` folder.
- Replace `your_secret_key` with a secure key in production.
- Error handling is included to ensure robustness.
