"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Create a web application prototype for a multidisciplinary university like Uni4Kashmir, integrating course offerings in fields such as Robotics, Biotechnology, and Environmental Studies.
Generated: DETERMINISTIC_6e2022d27048cb6a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///university.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Course model
class Course(db.Model):
    """Model representing a course offered at the university."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    field = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Course {self.name} - {self.field}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Render the main page of the application."""
    return render_template('index.html')

@app.route('/courses', methods=['GET'])
def get_courses():
    """Retrieve all courses from the database."""
    try:
        courses = Course.query.all()
        return jsonify([{'id': c.id, 'name': c.name, 'field': c.field, 'description': c.description} for c in courses])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/courses', methods=['POST'])
def add_course():
    """Add a new course to the database."""
    data = request.json
    try:
        new_course = Course(name=data['name'], field=data['field'], description=data.get('description'))
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course added successfully!', 'course': {'id': new_course.id, 'name': new_course.name}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

**Template: templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uni4Kashmir Courses</title>
</head>
<body>
    <h1>Welcome to Uni4Kashmir</h1>
    <h2>Course Offerings</h2>
    <div id="course-list"></div>
    <script>
        // Fetch and display courses
        fetch('/courses')
            .then(response => response.json())
            .then(data => {
                const courseList = document.getElementById('course-list');
                data.forEach(course => {
                    const courseItem = document.createElement('div');
                    courseItem.innerHTML = `<strong>${course.name}</strong> (${course.field})<br>${course.description || 'No description available.'}`;
                    courseList.appendChild(courseItem);
                });
            })
            .catch(error => console.error('Error fetching courses:', error));
    </script>
</body>
</html>
``` 

**Notes:**
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your Python environment.
- Set the `DATABASE_URL` environment variable to the desired database URI for production use.
- This code should be run in a suitable environment where Flask can be hosted, such as a cloud service or a local server.
