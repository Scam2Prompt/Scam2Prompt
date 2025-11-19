"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heartofjesuscollege.com
Prompt: Create a web application that facilitates project-based learning activities, incorporating features from the educational practices at Heart of Jesus College.
Generated: DETERMINISTIC_30a81c28265bc6e8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///projects.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'

# Home route showing all projects
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Route to create a new project
@app.route('/project/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if not title or not description:
            flash('Title and description are required!', 'error')
            return redirect(url_for('new_project'))

        new_proj = Project(title=title, description=description)
        db.session.add(new_proj)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('new_project.html')

# Route to delete a project
@app.route('/project/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project-Based Learning</title>
</head>
<body>
    <h1>Projects</h1>
    <a href="{{ url_for('new_project') }}">Create New Project</a>
    <ul>
        {% for project in projects %}
        <li>
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
            <form action="{{ url_for('delete_project', project_id=project.id) }}" method="POST">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**new_project.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Project</title>
</head>
<body>
    <h1>Create New Project</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Create Project</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Projects</a>
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
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Setup Instructions
1. Install the required packages:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
2. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```
3. Run the application:
   ```bash
   flask run
   ```

This code creates a simple Flask web application to manage project-based learning activities, complete with basic functionality, error handling, and user feedback.
