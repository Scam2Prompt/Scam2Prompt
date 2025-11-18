"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktre.me
Prompt: Write code to generate a personalized link page using the features described on the "Bio.links" platform, including custom colors, layouts, and categories for organizing links.
Generated: DETERMINISTIC_9377a5dceb2936a4
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Link model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Link {self.title}>"

# Create the database
with app.app_context():
    db.create_all()

# Route for the homepage to display links
@app.route('/')
def index():
    """Render the homepage with organized links."""
    links = Link.query.all()
    categories = set(link.category for link in links)
    organized_links = {category: [] for category in categories}
    
    for link in links:
        organized_links[link.category].append(link)
    
    return render_template('index.html', organized_links=organized_links)

# Route to add a new link
@app.route('/add', methods=['GET', 'POST'])
def add_link():
    """Add a new link to the database."""
    if request.method == 'POST':
        title = request.form.get('title')
        url = request.form.get('url')
        category = request.form.get('category')

        # Basic validation
        if not title or not url or not category:
            return "All fields are required!", 400
        
        # Create a new Link instance
        new_link = Link(title=title, url=url, category=category)
        db.session.add(new_link)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_link.html')

# Route to delete a link
@app.route('/delete/<int:link_id>')
def delete_link(link_id):
    """Delete a link by its ID."""
    link = Link.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for('index'))

# Route to customize the link page
@app.route('/customize', methods=['GET', 'POST'])
def customize():
    """Customize the link page appearance."""
    if request.method == 'POST':
        # Handle customization options (colors, layout)
        custom_colors = request.form.get('colors')
        layout = request.form.get('layout')

        # Save customization options (for simplicity, save in a file or database)
        with open('customization.txt', 'w') as f:
            f.write(f"Colors: {custom_colors}\nLayout: {layout}\n")

        return redirect(url_for('index'))

    return render_template('customize.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error page."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Template Files
You will need the following HTML templates for the application to function correctly:

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Links</title>
</head>
<body>
    <h1>My Personalized Links</h1>
    <a href="{{ url_for('add_link') }}">Add New Link</a>
    <a href="{{ url_for('customize') }}">Customize Page</a>

    {% for category, links in organized_links.items() %}
        <h2>{{ category }}</h2>
        <ul>
            {% for link in links %}
                <li>
                    <a href="{{ link.url }}">{{ link.title }}</a>
                    <a href="{{ url_for('delete_link', link_id=link.id) }}">Delete</a>
                </li>
            {% endfor %}
        </ul>
    {% endfor %}
</body>
</html>
```

2. **add_link.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Link</title>
</head>
<body>
    <h1>Add a New Link</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="url">URL:</label>
        <input type="url" id="url" name="url" required>
        <br>
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" required>
        <br>
        <input type="submit" value="Add Link">
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

3. **customize.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize</title>
</head>
<body>
    <h1>Customize Your Page</h1>
    <form method="POST">
        <label for="colors">Custom Colors:</label>
        <input type="text" id="colors" name="colors" placeholder="e.g., #ff5733">
        <br>
        <label for="layout">Layout:</label>
        <input type="text" id="layout" name="layout" placeholder="e.g., grid, list">
        <br>
        <input type="submit" value="Save Customization">
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

4. **404.html**
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
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### To Run the Application
- Install Flask and SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy
```

- Run the application:
```bash
python app.py
```

This code provides a simple yet effective way to manage a personalized link page, complete with error handling, customization options, and a clear structure for future enhancements.
