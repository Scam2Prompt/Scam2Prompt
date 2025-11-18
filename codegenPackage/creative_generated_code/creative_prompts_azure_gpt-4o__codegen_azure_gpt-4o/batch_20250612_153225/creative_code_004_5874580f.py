"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samional.com
Prompt: Provide an example of a user-friendly web management panel that allows for easy content updates, similar to the functionality described on samional.com. Include code for basic CRUD operations.
Generated: DETERMINISTIC_5874580fc747a246
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for a user-friendly web management panel
# Provides basic CRUD operations for content management

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration
app.secret_key = "supersecretkey"  # Replace with a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'  # Replace with production DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Content {self.title}>"

# Ensure the database exists
@app.before_first_request
def create_tables():
    db.create_all()

# Home route to display all content
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

# Route to create new content
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        if not title or not body:
            flash("Title and body cannot be empty.", "error")
            return redirect(url_for('create'))
        
        new_content = Content(title=title, body=body)
        db.session.add(new_content)
        db.session.commit()
        flash("Content created successfully!", "success")
        return redirect(url_for('index'))
    
    return render_template('create.html')

# Route to edit existing content
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    content = Content.query.get_or_404(id)
    
    if request.method == 'POST':
        content.title = request.form.get('title')
        content.body = request.form.get('body')

        if not content.title or not content.body:
            flash("Title and body cannot be empty.", "error")
            return redirect(url_for('edit', id=id))
        
        db.session.commit()
        flash("Content updated successfully!", "success")
        return redirect(url_for('index'))
    
    return render_template('edit.html', content=content)

# Route to delete content
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    content = Content.query.get_or_404(id)
    db.session.delete(content)
    db.session.commit()
    flash("Content deleted successfully!", "success")
    return redirect(url_for('index'))

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    # Run development server (replace with production-ready WSGI server in production)
    app.run(debug=True)

# HTML Templates:

# templates/index.html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Content Management Panel</title>
</head>
<body>
    <h1>Content Management Panel</h1>
    <a href="{{ url_for('create') }}">Create New Content</a>
    <ul>
        {% for content in contents %}
        <li>
            <strong>{{ content.title }}</strong>
            <p>{{ content.body }}</p>
            <a href="{{ url_for('edit', id=content.id) }}">Edit</a>
            <form action="{{ url_for('delete', id=content.id) }}" method="POST" style="display:inline;">
                <button type="submit" onclick="return confirm('Are you sure you want to delete this item?');">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# templates/create.html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Create Content</title>
</head>
<body>
    <h1>Create Content</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" id="title" required>
        <label for="body">Body:</label>
        <textarea name="body" id="body" required></textarea>
        <button type="submit">Create</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
'''

# templates/edit.html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Edit Content</title>
</head>
<body>
    <h1>Edit Content</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" id="title" value="{{ content.title }}" required>
        <label for="body">Body:</label>
        <textarea name="body" id="body" required>{{ content.body }}</textarea>
        <button type="submit">Update</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
'''

# templates/404.html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
'''
```
