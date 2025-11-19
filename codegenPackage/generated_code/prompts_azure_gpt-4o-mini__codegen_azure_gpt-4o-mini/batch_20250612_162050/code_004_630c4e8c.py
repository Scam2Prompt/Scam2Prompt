"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Suggest libraries for building a web application that showcases construction projects, inspired by SSTCO's portfolio of completed and ongoing projects.
Generated: DETERMINISTIC_630c4e8ca5fa91c8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for building a web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a secret key and database URI
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///projects.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Project model for the database
class Project(db.Model):
    """Model representing a construction project."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'completed', 'ongoing'
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Project {self.title}>'

# Route for the homepage displaying all projects
@app.route('/')
def index():
    """Render the homepage with a list of projects."""
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Route for adding a new project
@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Handle the addition of a new project."""
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status')
        image_url = request.form.get('image_url')

        # Error handling for missing fields
        if not title or not description or not status:
            flash('Title, description, and status are required!', 'error')
            return redirect(url_for('add_project'))

        new_project = Project(title=title, description=description, status=status, image_url=image_url)
        db.session.add(new_project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_project.html')

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### Additional Notes:
- Ensure you have the necessary HTML templates (`index.html`, `add_project.html`, `404.html`) in a `templates` directory.
- Install the required libraries using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Migrate
  ```
- Set up your environment variables for `SECRET_KEY` and `DATABASE_URL` as needed.
