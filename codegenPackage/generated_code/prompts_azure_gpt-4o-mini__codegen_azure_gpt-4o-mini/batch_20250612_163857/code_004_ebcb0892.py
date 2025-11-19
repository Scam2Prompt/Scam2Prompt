"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: What programming libraries can be used to develop a website for community-based projects similar to St. Andrew’s School Project for The Young?
Generated: DETERMINISTIC_ebcb089255b7d342
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for community projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of community projects."""
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Route to add a new project
@app.route('/add', methods=['POST'])
def add_project():
    """Add a new project to the database."""
    title = request.form.get('title')
    description = request.form.get('description')

    if not title or not description:
        flash('Title and description are required!', 'error')
        return redirect(url_for('index'))

    new_project = Project(title=title, description=description)

    try:
        db.session.add(new_project)
        db.session.commit()
        flash('Project added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding project: {str(e)}', 'error')

    return redirect(url_for('index'))

# Route to delete a project
@app.route('/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    """Delete a project from the database."""
    project = Project.query.get_or_404(project_id)

    try:
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting project: {str(e)}', 'error')

    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Community Projects</title>
</head>
<body>
    <h1>Community Projects</h1>
    <form action="{{ url_for('add_project') }}" method="POST">
        <input type="text" name="title" placeholder="Project Title" required>
        <textarea name="description" placeholder="Project Description" required></textarea>
        <button type="submit">Add Project</button>
    </form>

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <ul>
        {% for project in projects %}
            <li>
                <strong>{{ project.title }}</strong>: {{ project.description }}
                <form action="{{ url_for('delete_project', project_id=project.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Requirements
To run this code, you will need to install the following Python libraries:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Database Initialization
To initialize the database, run the following commands in a Python shell:
```python
from your_application_file import db
db.create_all()
```

Replace `your_application_file` with the name of the Python file containing the Flask application code.
