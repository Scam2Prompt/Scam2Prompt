"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Provide code to create a blog section for a real estate website, allowing posts about market trends (e.g., rental price increases, remittance statistics) as seen on Félix Trujillo Falla's blog.
Generated: DETERMINISTIC_83bacf81eb05593f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db = SQLAlchemy(app)

# Database model for BlogPost
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each blog post
    title = db.Column(db.String(100), nullable=False)  # Blog post title
    content = db.Column(db.Text, nullable=False)  # Blog post content
    author = db.Column(db.String(50), nullable=False)  # Author's name
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)  # Date posted

    def __repr__(self):
        return f"BlogPost(title={self.title}, author={self.author}, date_posted={self.date_posted})"

# Route to display all blog posts
@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()  # Fetch all posts, sorted by date
    return render_template('index.html', posts=posts)

# Route to display the form for creating a new blog post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        
        if not title or not content or not author:
            flash('All fields are required!', 'danger')  # Error feedback for missing fields
            return redirect(url_for('new_post'))

        try:
            post = BlogPost(title=title, content=content, author=author)  # Create a new blog post instance
            db.session.add(post)  # Add the instance to the database session
            db.session.commit()  # Commit the transaction
            flash('Post created successfully!', 'success')  # Success feedback
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Roll back the transaction in case of error
            flash(f'Error creating post: {str(e)}', 'danger')  # Error feedback
            return redirect(url_for('new_post'))
    return render_template('new_post.html')

# Route to view a single blog post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = BlogPost.query.get_or_404(post_id)  # Fetch the post by ID or return a 404 if not found
    return render_template('view_post.html', post=post)

# Route to delete a blog post
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)  # Fetch the post by ID or return a 404 if not found
    try:
        db.session.delete(post)  # Delete the post
        db.session.commit()  # Commit the transaction
        flash('Post deleted successfully!', 'success')  # Success feedback
    except Exception as e:
        db.session.rollback()  # Roll back the transaction in case of error
        flash(f'Error deleting post: {str(e)}', 'danger')  # Error feedback
    return redirect(url_for('index'))

# Entry point for running the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database and tables are created
    app.run(debug=True)  # Run the Flask application in debug mode
```

**Notes:**
1. The code assumes the existence of `index.html`, `new_post.html`, and `view_post.html` templates to render respective pages.
2. Replace `'your_secret_key'` with a secure key for production use.
3. Install necessary dependencies using `pip install flask flask_sqlalchemy`.
4. Follow security best practices for handling user input and deploying the app in production (e.g., use HTTPS, validate inputs).
