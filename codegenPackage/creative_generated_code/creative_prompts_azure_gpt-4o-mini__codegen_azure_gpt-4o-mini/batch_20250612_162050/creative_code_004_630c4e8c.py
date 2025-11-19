"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sstco.ma
Prompt: Suggest libraries for building a web application that showcases construction projects, inspired by SSTCO's portfolio of completed and ongoing projects.
Generated: DETERMINISTIC_630c4e8ca5fa91c8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random key for session management

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a model for construction projects
class Project(db.Model):
    """Model to represent a construction project."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'completed', 'ongoing'

    def __repr__(self):
        return f'<Project {self.name}>'

# Route for the home page that displays all projects
@app.route('/')
def home():
    """Render the home page displaying all construction projects."""
    projects = Project.query.all()  # Query all projects from the database
    return render_template('home.html', projects=projects)

# Route for adding a new project
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    """Handle adding a new project to the database."""
    if request.method == 'POST':  # Check if the form is submitted
        try:
            name = request.form['name']
            description = request.form['description']
            status = request.form['status']

            # Create a new project instance
            new_project = Project(name=name, description=description, status=status)
            db.session.add(new_project)  # Add the project to the session
            db.session.commit()  # Commit the session to the database
            
            flash('Project added successfully!', 'success')
            return redirect(url_for('home'))  # Redirect to home page
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error adding project: {str(e)}', 'danger')  # Flash error message

    return render_template('add_project.html')  # Render form for adding a project

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(e):
    """Render a custom internal server error page."""
    return render_template('500.html'), 500

# Main entry point for running the application
if __name__ == '__main__':
    db.create_all()  # Create database tables if they do not exist
    app.run(debug=True)  # Run the application with debug mode enabled
```

### Required Libraries
To run this application, ensure you have the following libraries installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Directory Structure
The application assumes you have the following directory structure with corresponding templates:

```
/your_project_directory
|-- app.py               # Main application file
|-- templates/           # Template directory
    |-- home.html        # Template for home page
    |-- add_project.html  # Template for adding project page
    |-- 404.html         # Template for 404 error page
    |-- 500.html         # Template for 500 error page
```
