"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Suggest a library or framework to build a website for showcasing carpentry projects, including features for displaying photos of completed works like those on Aluivars' site.
Generated: DETERMINISTIC_62448992d0fefde0
Batch ID: 20250612_153224
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
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database and upload folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

# Initialize the database
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    """Display all projects on the homepage."""
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

# Route for adding a new project
@app.route('/add', methods=['GET', 'POST'])
def add_project():
    """Add a new carpentry project."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']

        # Basic error handling for file uploads
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Create a new Project instance
            new_project = Project(title=title, description=description, image_filename=filename)
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return "Invalid file format. Allowed formats: jpg, jpeg, png, gif.", 400

    return render_template('add_project.html')

# Function to check allowed file extensions
def allowed_file(filename):
    """Check if the uploaded file is allowed."""
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carpentry Projects</title>
</head>
<body>
    <h1>Carpentry Projects</h1>
    <a href="{{ url_for('add_project') }}">Add New Project</a>
    <ul>
        {% for project in projects %}
            <li>
                <h2>{{ project.title }}</h2>
                <p>{{ project.description }}</p>
                <img src="{{ url_for('static', filename='uploads/' + project.image_filename) }}" alt="{{ project.title }}" style="width:200px;">
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- add_project.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New Project</title>
</head>
<body>
    <h1>Add New Carpentry Project</h1>
    <form method="POST" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="image">Image:</label>
        <input type="file" id="image" name="image" accept="image/*" required>
        <br>
        <button type="submit">Add Project</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Projects</a>
</body>
</html>
```

Make sure to create the appropriate folders (e.g., 'static/uploads') and run the application in an environment where Flask is installed.
