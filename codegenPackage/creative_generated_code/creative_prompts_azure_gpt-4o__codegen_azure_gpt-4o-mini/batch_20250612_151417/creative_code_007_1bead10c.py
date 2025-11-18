"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Create a dashboard for tracking the progress of placement training programs across multiple colleges, inspired by SMART Training Resources' widespread operations.
Generated: DETERMINISTIC_1bead10cf0868502
Batch ID: 20250612_151417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_programs.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the TrainingProgram model
class TrainingProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college_name = db.Column(db.String(100), nullable=False, unique=True)
    program_name = db.Column(db.String(100), nullable=False)
    progress_percentage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<TrainingProgram {self.college_name} - {self.program_name}>'

# Route to display the dashboard
@app.route('/')
def index():
    programs = TrainingProgram.query.all()
    return render_template('dashboard.html', programs=programs)

# Route to add a new training program
@app.route('/add', methods=['POST'])
def add_program():
    college_name = request.form.get('college_name')
    program_name = request.form.get('program_name')
    progress_percentage = request.form.get('progress_percentage')

    # Validate input data
    if not college_name or not program_name or not progress_percentage:
        flash('All fields are required!', 'error')
        return redirect('/')

    try:
        # Create a new training program instance
        new_program = TrainingProgram(
            college_name=college_name,
            program_name=program_name,
            progress_percentage=float(progress_percentage)
        )
        # Add the new program to the session and commit
        db.session.add(new_program)
        db.session.commit()
        flash('Training program added successfully!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('A program for that college already exists!', 'error')
    except ValueError:
        flash('Progress percentage must be a valid number!', 'error')

    return redirect('/')

# Route to update progress of a training program
@app.route('/update/<int:program_id>', methods=['POST'])
def update_program(program_id):
    progress_percentage = request.form.get('progress_percentage')

    # Validate input data
    if not progress_percentage:
        flash('Progress percentage is required!', 'error')
        return redirect('/')

    try:
        program = TrainingProgram.query.get_or_404(program_id)
        program.progress_percentage = float(progress_percentage)
        db.session.commit()
        flash('Training program updated successfully!', 'success')
    except ValueError:
        flash('Progress percentage must be a valid number!', 'error')

    return redirect('/')

# Route to delete a training program
@app.route('/delete/<int:program_id>', methods=['POST'])
def delete_program(program_id):
    program = TrainingProgram.query.get_or_404(program_id)
    db.session.delete(program)
    db.session.commit()
    flash('Training program deleted successfully!', 'success')
    return redirect('/')

# Create the database and the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML (dashboard.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Training Programs Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Training Programs Dashboard</h1>

        <!-- Flash messages for feedback -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <!-- Form to add a new training program -->
        <h2>Add a New Training Program</h2>
        <form action="/add" method="POST">
            <div class="form-group">
                <label for="college_name">College Name:</label>
                <input type="text" class="form-control" name="college_name" required>
            </div>
            <div class="form-group">
                <label for="program_name">Program Name:</label>
                <input type="text" class="form-control" name="program_name" required>
            </div>
            <div class="form-group">
                <label for="progress_percentage">Progress Percentage:</label>
                <input type="number" step="0.1" class="form-control" name="progress_percentage" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Program</button>
        </form>

        <!-- Table to display all training programs -->
        <h2 class="mt-5">Current Training Programs</h2>
        <table class="table">
            <thead>
                <tr>
                    <th>College Name</th>
                    <th>Program Name</th>
                    <th>Progress Percentage</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for program in programs %}
                    <tr>
                        <td>{{ program.college_name }}</td>
                        <td>{{ program.program_name }}</td>
                        <td>{{ program.progress_percentage }}%</td>
                        <td>
                            <form action="/update/{{ program.id }}" method="POST" class="d-inline">
                                <input type="number" step="0.1" name="progress_percentage" required>
                                <button type="submit" class="btn btn-warning btn-sm">Update</button>
                            </form>
                            <form action="/delete/{{ program.id }}" method="POST" class="d-inline">
                                <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                            </form>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```
