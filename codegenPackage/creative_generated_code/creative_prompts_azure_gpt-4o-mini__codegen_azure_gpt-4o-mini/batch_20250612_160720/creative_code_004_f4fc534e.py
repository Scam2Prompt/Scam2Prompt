"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Suggest a library for developing a forum for discussing Wazaif, inspired by the community engagement seen at Darul Raza International Ruhani Center.
Generated: DETERMINISTIC_f4fc534ee1993766
Batch ID: 20250612_160720
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wazaif_forum.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the ForumPost model
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# Route for the home page
@app.route('/')
def index():
    # Retrieve all forum posts from the database
    posts = ForumPost.query.all()
    return render_template('index.html', posts=posts)

# Route for creating a new post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        content = request.form['content']
        
        # Error handling for empty fields
        if not title or not content:
            flash('Title and Content cannot be empty', 'error')
            return redirect(url_for('new_post'))

        # Create a new forum post
        new_post = ForumPost(title=title, content=content)
        
        try:
            db.session.add(new_post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('Error creating post: ' + str(e), 'error')

    return render_template('new_post.html')

# Route for viewing a specific post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = ForumPost.query.get_or_404(post_id)
    return render_template('post.html', post=post)

# Error handling for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Create the database if it does not exist
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```

**Notes:**
- Ensure you have Flask and Flask-SQLAlchemy installed. You can install them via pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- Create corresponding HTML templates (`index.html`, `new_post.html`, `post.html`, `404.html`) to render the views.
- Replace `'your_secret_key'` with a strong, random secret key for session management.
