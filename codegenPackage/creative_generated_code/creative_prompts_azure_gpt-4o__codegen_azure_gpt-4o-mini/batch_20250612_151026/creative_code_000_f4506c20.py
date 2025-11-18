"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Write code for a web application that tracks the progress of experiential learning courses, including features for habit creation and talent maximization, as described by Virtual5's methodology.
Generated: DETERMINISTIC_f4506c208d8018f9
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model to represent a Course
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    progress = db.Column(db.Float, default=0.0)
    habits = db.relationship('Habit', backref='course', lazy=True)

    def __repr__(self):
        return f'<Course {self.title}>'

# Model to represent a Habit
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        return f'<Habit {self.name}>'

# Route to render the main application page
@app.route('/')
def index():
    return render_template('index.html')

# API route to create a new course
@app.route('/api/courses', methods=['POST'])
def create_course():
    try:
        data = request.json
        new_course = Course(title=data['title'], description=data.get('description'))
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully!', 'course_id': new_course.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session on error
        return jsonify({'error': str(e)}), 400

# API route to update course progress
@app.route('/api/courses/<int:course_id>/progress', methods=['PATCH'])
def update_progress(course_id):
    try:
        data = request.json
        course = Course.query.get_or_404(course_id)
        course.progress = data['progress']
        db.session.commit()
        return jsonify({'message': 'Progress updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API route to create a new habit for a course
@app.route('/api/courses/<int:course_id>/habits', methods=['POST'])
def create_habit(course_id):
    try:
        data = request.json
        new_habit = Habit(name=data['name'], frequency=data['frequency'], course_id=course_id)
        db.session.add(new_habit)
        db.session.commit()
        return jsonify({'message': 'Habit created successfully!', 'habit_id': new_habit.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API route to fetch all courses with their habits
@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        result = []
        for course in courses:
            habits = [{'id': habit.id, 'name': habit.name, 'frequency': habit.frequency} for habit in course.habits]
            result.append({'id': course.id, 'title': course.title, 'description': course.description, 'progress': course.progress, 'habits': habits})
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
    <title>Experiential Learning Tracker</title>
</head>
<body>
    <h1>Welcome to the Experiential Learning Tracker</h1>
    <p>Use the API to manage your courses and habits!</p>
</body>
</html>
```

```bash
# requirements.txt
Flask==2.1.1
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
```

```bash
# To set up the project, run the following commands:
# 1. Install dependencies
pip install -r requirements.txt

# 2. Initialize the database
flask db init
flask db migrate
flask db upgrade

# 3. Run the Flask application
python app.py
```

Make sure to set up the environment and the database as described in the comments.
