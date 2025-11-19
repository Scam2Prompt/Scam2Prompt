"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Suggest a framework for developing a web application that showcases completed construction projects, similar to the portfolio of Construye RK.
Generated: DETERMINISTIC_f17558d051f9cce9
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI; replace with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Project model
class Project(db.Model):
    """Model representing a construction project."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Project {self.title}>'

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions."""
    return render_template("error.html", error=e), e.code

@app.route('/')
def index():
    """Render the homepage with a list of projects."""
    projects = Project.query.all()  # Retrieve all projects from the database
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Render the detail page for a specific project."""
    project = Project.query.get_or_404(project_id)  # Get project or return 404
    return render_template('project_detail.html', project=project)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Route to add a new project."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['image_url']

        # Create a new project instance
        new_project = Project(title=title, description=description, image_url=image_url)
        
        try:
            db.session.add(new_project)  # Add the project to the session
            db.session.commit()  # Commit the session to save the project
            return redirect(url_for('index'))  # Redirect to homepage after adding
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return f"An error occurred: {e}", 500  # Return error message

    return render_template('add_project.html')  # Render form for adding a project

# Run the application if this file is executed
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app with debug mode enabled
```

**Note**: This code assumes you have Flask and Flask-SQLAlchemy installed in your environment. Make sure to create the required HTML templates (`index.html`, `project_detail.html`, `add_project.html`, and `error.html`) to match the functionality provided by this backend code.
