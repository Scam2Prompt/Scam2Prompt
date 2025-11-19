"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Create a web application prototype for a multidisciplinary university like Uni4Kashmir, integrating course offerings in fields such as Robotics, Biotechnology, and Environmental Studies.
Generated: DETERMINISTIC_6e2022d27048cb6a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    field = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Course {self.name} - {self.field}>'

# Route for the home page
@app.route('/')
def index():
    # Fetch all courses from the database
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

# Route to add a new course
@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        field = request.form.get('field')
        description = request.form.get('description')

        # Error handling for empty fields
        if not name or not field or not description:
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_course'))

        # Create a new course instance
        new_course = Course(name=name, field=field, description=description)

        # Add the course to the database
        try:
            db.session.add(new_course)
            db.session.commit()
            flash('Course added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding course: {str(e)}', 'danger')

        return redirect(url_for('index'))

    return render_template('add_course.html')

# Route to delete a course
@app.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    try:
        db.session.delete(course)
        db.session.commit()
        flash('Course deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting course: {str(e)}', 'danger')

    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University Courses</title>
</head>
<body>
    <h1>Course Offerings</h1>
    <a href="{{ url_for('add_course') }}">Add New Course</a>
    <ul>
        {% for course in courses %}
            <li>
                {{ course.name }} - {{ course.field }}
                <form action="{{ url_for('delete_course', course_id=course.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_course.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Course</title>
</head>
<body>
    <h1>Add New Course</h1>
    <form action="{{ url_for('add_course') }}" method="POST">
        <label for="name">Course Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="field">Field of Study:</label>
        <input type="text" id="field" name="field" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Add Course</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Course List</a>
</body>
</html>
```

### Database Migration
To create the database and tables, run the following commands in your terminal:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Note
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Replace `'your_secret_key'` with a secure random key for production use.
- This code is a basic prototype and should be expanded with user authentication, input validation, and additional features for a production-ready application.
