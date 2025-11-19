"""
Generated Code Metadata:
========================
Original URL: https://centraldata-enterpristore.com
Prompt: "Create a WYSIWYG content management system for an ecommerce platform using Infor FACTS and CSD data."
Generated: DETERMINISTIC_7d7a713fcc58c7d0
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Content {self.title}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of content."""
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

# Route to create new content
@app.route('/create', methods=['GET', 'POST'])
def create_content():
    """Create new content entry."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_content = Content(title=title, body=body)

        try:
            db.session.add(new_content)
            db.session.commit()
            flash('Content created successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Error: Content with this title already exists.', 'danger')

    return render_template('create.html')

# Route to edit existing content
@app.route('/edit/<int:content_id>', methods=['GET', 'POST'])
def edit_content(content_id):
    """Edit existing content entry."""
    content = Content.query.get_or_404(content_id)

    if request.method == 'POST':
        content.title = request.form['title']
        content.body = request.form['body']

        try:
            db.session.commit()
            flash('Content updated successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Error: Could not update content.', 'danger')

    return render_template('edit.html', content=content)

# Route to delete content
@app.route('/delete/<int:content_id>', methods=['POST'])
def delete_content(content_id):
    """Delete content entry."""
    content = Content.query.get_or_404(content_id)
    db.session.delete(content)
    db.session.commit()
    flash('Content deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content Management System</title>
</head>
<body>
    <h1>Content Management System</h1>
    <a href="{{ url_for('create_content') }}">Create New Content</a>
    <ul>
        {% for content in contents %}
            <li>
                <h2>{{ content.title }}</h2>
                <p>{{ content.body }}</p>
                <a href="{{ url_for('edit_content', content_id=content.id) }}">Edit</a>
                <form action="{{ url_for('delete_content', content_id=content.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**create.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Content</title>
</head>
<body>
    <h1>Create New Content</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="body">Body:</label>
        <textarea name="body" required></textarea>
        <button type="submit">Create</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**edit.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Content</title>
</head>
<body>
    <h1>Edit Content</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" value="{{ content.title }}" required>
        <label for="body">Body:</label>
        <textarea name="body" required>{{ content.body }}</textarea>
        <button type="submit">Update</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a secure key for production use.
- This code is a basic implementation and may require additional features and security measures for a production environment.
