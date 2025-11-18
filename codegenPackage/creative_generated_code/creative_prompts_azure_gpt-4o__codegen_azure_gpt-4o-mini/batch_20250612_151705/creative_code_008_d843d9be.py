"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Develop a dashboard using Python and Flask to track the progress of students in Debridge Advisory's sales training programs, segmented by industry type.
Generated: DETERMINISTIC_d843d9be3d8e3880
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Create Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    progress = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.name}, Industry {self.industry}, Progress {self.progress}>'

# Initialize the database - only run this once at the start
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the dashboard
@app.route('/')
def dashboard():
    """Render the main dashboard showing student progress."""
    try:
        students = Student.query.all()
        return render_template('dashboard.html', students=students)
    except Exception as e:
        logging.error(f"Error retrieving students for dashboard: {e}")
        return "Error loading dashboard", 500

# API endpoint to add a new student
@app.route('/add_student', methods=['POST'])
def add_student():
    """API endpoint to add a new student to the database."""
    try:
        data = request.json
        new_student = Student(
            name=data['name'],
            industry=data['industry'],
            progress=data['progress']
        )
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding student: {e}")
        return jsonify({'error': 'Error adding student'}), 400

# API endpoint to update student progress
@app.route('/update_progress/<int:student_id>', methods=['PUT'])
def update_progress(student_id):
    """API endpoint to update progress for a specified student."""
    try:
        data = request.json
        student = Student.query.get_or_404(student_id)
        student.progress = data['progress']
        db.session.commit()
        return jsonify({'message': 'Progress updated successfully'}), 200
    except Exception as e:
        logging.error(f"Error updating student progress: {e}")
        return jsonify({'error': 'Error updating progress'}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (dashboard.html)** - Place this file in a folder named `templates`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Progress Dashboard</title>
</head>
<body>
    <h1>Student Progress Dashboard</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Industry</th>
                <th>Progress (%)</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.name }}</td>
                <td>{{ student.industry }}</td>
                <td>{{ student.progress }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <script>
        // Add JavaScript here if needed for further interactivity
    </script>
</body>
</html>
```

Make sure to install Flask and Flask-SQLAlchemy with the following commands if you haven't:

```bash
pip install Flask Flask-SQLAlchemy
```

This code provides a basic structure for the dashboard to track students in a sales training program, with necessary CRUD operations and error handling.
