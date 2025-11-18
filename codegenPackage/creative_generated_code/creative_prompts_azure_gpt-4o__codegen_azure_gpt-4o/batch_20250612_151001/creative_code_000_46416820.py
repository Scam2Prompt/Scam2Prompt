"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://card.xumicloud.top
Prompt: Write code to create a customizable navigation page similar to "须弥の导航页," including features for adding private links, managing categories, and adjusting settings.
Generated: DETERMINISTIC_464168204171b626
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested Python code using Flask as the web framework and SQLite as the database for a customizable navigation page:

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Secret key for session management
app.secret_key = "supersecretkey"

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///navigation_page.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for categories
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

# Database model for links
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

# Route: Home page showing all categories and links
@app.route('/')
def home():
    categories = Category.query.all()
    links = Link.query.all()
    return render_template('home.html', categories=categories, links=links)

# Route: Add category
@app.route('/add_category', methods=['POST'])
def add_category():
    category_name = request.form.get('name')
    if not category_name:
        flash("Category name cannot be empty!", "error")
        return redirect(url_for('home'))

    if Category.query.filter_by(name=category_name).first():
        flash("Category already exists!", "error")
        return redirect(url_for('home'))

    try:
        new_category = Category(name=category_name)
        db.session.add(new_category)
        db.session.commit()
        flash("Category added successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error adding category: {str(e)}", "error")
    return redirect(url_for('home'))

# Route: Add private link
@app.route('/add_link', methods=['POST'])
def add_link():
    link_name = request.form.get('name')
    link_url = request.form.get('url')
    category_id = request.form.get('category_id')

    if not link_name or not link_url or not category_id:
        flash("All fields are required!", "error")
        return redirect(url_for('home'))

    try:
        new_link = Link(name=link_name, url=link_url, category_id=int(category_id))
        db.session.add(new_link)
        db.session.commit()
        flash("Link added successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error adding link: {str(e)}", "error")
    return redirect(url_for('home'))

# Route: Delete category
@app.route('/delete_category/<int:category_id>')
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    try:
        db.session.delete(category)
        db.session.commit()
        flash("Category deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting category: {str(e)}", "error")
    return redirect(url_for('home'))

# Route: Delete link
@app.route('/delete_link/<int:link_id>')
def delete_link(link_id):
    link = Link.query.get_or_404(link_id)
    try:
        db.session.delete(link)
        db.session.commit()
        flash("Link deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting link: {str(e)}", "error")
    return redirect(url_for('home'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Initialize the database and create tables
@app.before_first_request
def setup_database():
    if not os.path.exists('navigation_page.db'):
        db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### File: `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Navigation Page</title>
</head>
<body>
    <h1>Navigation Page</h1>

    <!-- Flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <!-- Add Category Form -->
    <h2>Add Category</h2>
    <form method="POST" action="/add_category">
        <input type="text" name="name" placeholder="Category Name" required>
        <button type="submit">Add Category</button>
    </form>

    <!-- Add Link Form -->
    <h2>Add Link</h2>
    <form method="POST" action="/add_link">
        <input type="text" name="name" placeholder="Link Name" required>
        <input type="url" name="url" placeholder="Link URL" required>
        <select name="category_id" required>
            <option value="" disabled selected>Select Category</option>
            {% for category in categories %}
                <option value="{{ category.id }}">{{ category.name }}</option>
            {% endfor %}
        </select>
        <button type="submit">Add Link</button>
    </form>

    <!-- List Categories and Links -->
    <h2>Categories</h2>
    {% for category in categories %}
        <div>
            <h3>{{ category.name }}</h3>
            <button onclick="window.location.href='/delete_category/{{ category.id }}'">Delete Category</button>
            <ul>
                {% for link in links if link.category_id == category.id %}
                    <li>
                        <a href="{{ link.url }}" target="_blank">{{ link.name }}</a>
                        <button onclick="window.location.href='/delete_link/{{ link.id }}'">Delete Link</button>
                    </li>
                {% endfor %}
            </ul>
        </div>
    {% endfor %}
</body>
</html>
```

### File: `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you're looking for does not exist.</p>
    <a href="/">Go back to Home</a>
</body>
</html>
```
