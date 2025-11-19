"""
Generated Code Metadata:
========================
Original URL: https://cem-ac.org
Prompt: Generate a code snippet for a web application that showcases artistic projects related to cinematography and stage arts in Mexico, emphasizing cultural responsibility.
Generated: DETERMINISTIC_d27a90e43755dffe
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to display all projects
@app.route('/')
def index():
    try:
        projects = Project.query.all()  # Fetch all projects from the database
        return render_template('index.html', projects=projects)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message if fetching fails

# Route to add a new project
@app.route('/add', methods=['POST'])
def add_project():
    try:
        data = request.json  # Get JSON data from the request
        new_project = Project(
            title=data['title'],
            description=data['description'],
            artist=data['artist'],
            year=data['year']
        )
        db.session.add(new_project)  # Add the new project to the session
        db.session.commit()  # Commit the session to save changes
        return jsonify({"message": "Project added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error message if adding fails

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cinematography and Stage Arts Projects</title>
</head>
<body>
    <h1>Artistic Projects in Cinematography and Stage Arts</h1>
    <ul>
        {% for project in projects %}
            <li>
                <h2>{{ project.title }}</h2>
                <p><strong>Artist:</strong> {{ project.artist }}</p>
                <p><strong>Description:</strong> {{ project.description }}</p>
                <p><strong>Year:</strong> {{ project.year }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- The database is set to SQLite for simplicity; adjust the URI for production use.
- The HTML template is basic; consider enhancing it with CSS for better presentation.
- Error handling is included for both fetching and adding projects.
