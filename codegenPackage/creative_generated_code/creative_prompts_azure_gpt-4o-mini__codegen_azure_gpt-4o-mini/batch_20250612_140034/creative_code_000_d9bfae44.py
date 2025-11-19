"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://completecircleconsulting.xyz
Prompt: Generate code for a web application that showcases commission work samples related to nature-inspired projects.
Generated: DETERMINISTIC_d9bfae4400f5c388
Batch ID: 20250612_140034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secure session management

# Initialize the database
db = SQLAlchemy(app)

# Model for Commission Work Samples
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Route for the home page
@app.route('/')
def home():
    try:
        projects = Project.query.all()  # Fetch all projects from the database
        return render_template('home.html', projects=projects)
    except Exception as e:
        flash('An error occurred while fetching projects. Please try again later.', 'danger')
        return render_template('home.html', projects=[])

# Route for adding a new project
@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['image_url']

        # Validation
        if not title or not description or not image_url:
            flash('All fields are required.', 'danger')
            return redirect(url_for('add_project'))

        new_project = Project(title=title, description=description, image_url=image_url)

        try:
            db.session.add(new_project)  # Add project to the session
            db.session.commit()  # Commit changes to the database
            flash('Project added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash('An error occurred while adding the project.', 'danger')
            return redirect(url_for('add_project'))

    return render_template('add_project.html')

# Error handling for 404 and other HTTP errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template("error.html", error=e), e.code

# Function to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### Required HTML Templates

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nature-Inspired Projects</title>
</head>
<body>
    <h1>Nature-Inspired Projects</h1>
    <a href="{{ url_for('add_project') }}">Add New Project</a>
    <div>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                    <div>{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>
    <ul>
        {% for project in projects %}
            <li>
                <h2>{{ project.title }}</h2>
                <p>{{ project.description }}</p>
                <img src="{{ project.image_url }}" alt="{{ project.title }}" />
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_project.html**
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
    <form method="post">
        <div>
            <label for="title">Title:</label>
            <input type="text" name="title" required>
        </div>
        <div>
            <label for="description">Description:</label>
            <textarea name="description" required></textarea>
        </div>
        <div>
            <label for="image_url">Image URL:</label>
            <input type="text" name="image_url" required>
        </div>
        <button type="submit">Add Project</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

**error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('home') }}">Return to Home</a>
</body>
</html>
```

### Instructions to Run

1. Ensure you have Flask and Flask-SQLAlchemy installed:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

2. Save the Python script in a file, e.g., `app.py`.

3. Create a folder named `templates` and save the HTML files inside it.

4. Run the application:
   ```bash
   python app.py
   ```

Visit `http://127.0.0.1:5000/` in your web browser to access the application.
