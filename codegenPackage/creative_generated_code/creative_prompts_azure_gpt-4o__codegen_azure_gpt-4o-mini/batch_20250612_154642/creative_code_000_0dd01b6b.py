"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Write code to create a web-based application that showcases architectural projects, inspired by Études' approach to merging creativity and functionality.
Generated: DETERMINISTIC_0dd01b6b98617565
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///projects.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Route for the home page that displays all projects
@app.route('/')
def index():
    """Render the homepage with all architectural projects."""
    projects = Project.query.all()  # Fetch all projects from the database
    return render_template('index.html', projects=projects)

# Route to add a new project
@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Handle the addition of a new architectural project."""
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image_url = request.form.get('image_url')

        # Basic validation
        if not title or not description or not image_url:
            flash('All fields are required!', 'error')
            return redirect(url_for('add_project'))

        # Create a new project instance and add it to the database
        new_project = Project(title=title, description=description, image_url=image_url)
        db.session.add(new_project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_project.html')

# Error handling for 404 not found
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error page."""
    return render_template('404.html'), 404

# Error handling for 500 internal server error
@app.errorhandler(500)
def internal_error(e):
    """Return a custom 500 error page."""
    db.session.rollback()  # Rollback any changes to the database
    return render_template('500.html'), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

### HTML Templates
You would also need the following HTML templates saved in a `templates` directory:

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architectural Projects</title>
</head>
<body>
    <h1>Architectural Projects</h1>
    <a href="/add">Add New Project</a>
    <ul>
        {% for project in projects %}
        <li>
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
            <img src="{{ project.image_url }}" alt="{{ project.title }}" style="max-width: 300px;">
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `add_project.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New Project</title>
</head>
<body>
    <h1>Add New Project</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea><br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url" required><br>
        <button type="submit">Add Project</button>
    </form>
    <a href="/">Back to Projects</a>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Projects</a>
</body>
</html>
```

#### `500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>An unexpected error has occurred. Please try again later.</p>
    <a href="/">Back to Projects</a>
</body>
</html>
```

### Setup Instructions
1. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
2. Set up your environment variables for `DATABASE_URL` and `SECRET_KEY`.
3. Create the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
4. Run the application:
   ```bash
   python app.py
   ```
