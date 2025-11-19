"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmastar.pages.dev
Prompt: Recommend libraries for building a successful IT agency website with a focus on real projects.
Generated: DETERMINISTIC_fad31d54ddec71a8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure application settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Route for the home page
@app.route('/')
def index():
    """Render the home page with all projects."""
    projects = Project.query.all()  # Fetch all projects from the database
    return render_template('index.html', projects=projects)

# Route for adding a new project
@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Handle adding a new project."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        if not title or not description:
            flash('Title and description are required!', 'error')
            return redirect(url_for('add_project'))

        new_project = Project(title=title, description=description)

        try:
            db.session.add(new_project)
            db.session.commit()  # Save project to the database
            flash('Project added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            logging.error(f'Error adding project: {e}')
            flash('An error occurred while adding the project.', 'error')

    return render_template('add_project.html')

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)  # Start the Flask application
    except Exception as e:
        logging.error(f'Failed to start the application: {e}')  # Log any startup errors
``` 

Ensure you have `Flask`, `Flask-SQLAlchemy`, and `Flask-Migrate` installed in your environment. Adjust the database URI for production settings accordingly. Create the necessary HTML templates (`index.html` and `add_project.html`) to render the web pages.
