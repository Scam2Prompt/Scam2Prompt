"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: Write code for a web-based portfolio management system that showcases case studies and projects, similar to the portfolio section on the Canadian Tech-Institute for Academic Research website.
Generated: DETERMINISTIC_2d84296075a2602d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import Flask for web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Needed for session management

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Project {self.title}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page to display projects
@app.route('/')
def index():
    projects = Project.query.all()  # Retrieve all projects from the database
    return render_template('index.html', projects=projects)

# Route to add a new project
@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        link = request.form['link']
        
        new_project = Project(title=title, description=description, link=link)
        
        try:
            db.session.add(new_project)  # Add new project to the session
            db.session.commit()  # Commit the session to save changes
            flash('Project added successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()  # Rollback in case of error
            flash('Error: Project could not be added.', 'error')

    return render_template('add_project.html')

# Route to view project details
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)  # Fetch project or send a 404 if not found
    return render_template('project_detail.html', project=project)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**HTML Template Example: index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>
<body>
    <h1>Portfolio Projects</h1>
    <a href="{{ url_for('add_project') }}">Add New Project</a>
    <ul>
        {% for project in projects %}
            <li>
                <a href="{{ url_for('project_detail', project_id=project.id) }}">{{ project.title }}</a>
                <p>{{ project.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**HTML Template Example: add_project.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Project</title>
</head>
<body>
    <h1>Add New Project</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <br>
        <label for="link">Link:</label>
        <input type="url" name="link" required>
        <br>
        <button type="submit">Add Project</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Portfolio</a>
</body>
</html>
```

**HTML Template Example: project_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.title }}</title>
</head>
<body>
    <h1>{{ project.title }}</h1>
    <p>{{ project.description }}</p>
    <p><a href="{{ project.link }}">View Project</a></p>
    <a href="{{ url_for('index') }}">Back to Portfolio</a>
</body>
</html>
```

**HTML Template Example: 404.html**
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
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Portfolio</a>
</body>
</html>
``` 

This code provides a simple web-based portfolio management system using Flask and SQLAlchemy, along with HTML templates for rendering the user interface. Be sure to install the necessary dependencies (`Flask`, `Flask-SQLAlchemy`) before running the application.
