"""
Generated Code Metadata:
========================
Original URL: https://bytnox.com
Prompt: Illustrate how to implement a feature in an app that allows users to showcase their architectural projects, inspired by the Études Architect App mentioned on bytnox.com.
Generated: DETERMINISTIC_fdeb5842993a9723
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

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

# Create the database tables
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to display the project submission form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle project submissions
@app.route('/submit', methods=['POST'])
def submit_project():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Create a new project entry
        new_project = Project(
            title=request.form['title'],
            description=request.form['description'],
            image_filename=filename
        )

        # Add the project to the database
        db.session.add(new_project)
        db.session.commit()

        return jsonify({'message': 'Project submitted successfully!'}), 201
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# Route to display all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'image_url': os.path.join(app.config['UPLOAD_FOLDER'], project.image_filename)
    } for project in projects]), 200

# Run the application
if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Your Project</title>
</head>
<body>
    <h1>Showcase Your Architectural Project</h1>
    <form action="/submit" method="post" enctype="multipart/form-data">
        <label for="title">Project Title:</label>
        <input type="text" id="title" name="title" required><br><br>
        
        <label for="description">Project Description:</label>
        <textarea id="description" name="description" required></textarea><br><br>
        
        <label for="file">Upload Image:</label>
        <input type="file" id="file" name="file" required><br><br>
        
        <input type="submit" value="Submit Project">
    </form>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Create an `uploads` directory in the same location as your script to store uploaded images.
- This code is a basic implementation and can be extended with features like user authentication, project editing, and more.
