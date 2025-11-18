"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Develop a web application feature that allows students to select and customize their study schedules, inspired by the flexible scheduling system mentioned on Educar Comitán's site.
Generated: DETERMINISTIC_3f31fe2192a4332c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedules.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define the Schedule model
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    study_sessions = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the Schedule object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'student_name': self.student_name,
            'study_sessions': json.loads(self.study_sessions),
            'created_at': self.created_at.isoformat(),
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page with study schedules."""
    schedules = Schedule.query.all()
    return render_template('index.html', schedules=schedules)

@app.route('/create_schedule', methods=['GET', 'POST'])
def create_schedule():
    """Create a new study schedule."""
    if request.method == 'POST':
        student_name = request.form.get('student_name')
        study_sessions = request.form.get('study_sessions')

        if not student_name or not study_sessions:
            flash('Both fields are required!', category='error')
            return redirect(url_for('create_schedule'))

        try:
            new_schedule = Schedule(
                student_name=student_name,
                study_sessions=json.dumps(study_sessions.split(','))  # Convert to JSON
            )
            db.session.add(new_schedule)
            db.session.commit()
            flash('Study schedule created successfully!', category='success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating schedule: {str(e)}', category='error')
        
        return redirect(url_for('index'))

    return render_template('create_schedule.html')

@app.route('/delete_schedule/<int:schedule_id>', methods=['POST'])
def delete_schedule(schedule_id):
    """Delete a specific study schedule by ID."""
    schedule = Schedule.query.get(schedule_id)
    if schedule:
        try:
            db.session.delete(schedule)
            db.session.commit()
            flash('Schedule deleted successfully!', category='success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting schedule: {str(e)}', category='error')
    else:
        flash('Schedule not found!', category='error')
    
    return redirect(url_for('index'))

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

**Templates (HTML)**

1. `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Study Schedules</title>
</head>
<body>
    <h1>Study Schedules</h1>
    <a href="{{ url_for('create_schedule') }}">Create a New Schedule</a>
    <ul>
        {% for schedule in schedules %}
            <li>
                <strong>{{ schedule.student_name }}</strong>: {{ schedule.study_sessions }} 
                <form action="{{ url_for('delete_schedule', schedule_id=schedule.id) }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. `create_schedule.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Study Schedule</title>
</head>
<body>
    <h1>Create Study Schedule</h1>
    <form method="POST">
        <label for="student_name">Student Name:</label>
        <input type="text" id="student_name" name="student_name" required>
        <br>
        <label for="study_sessions">Study Sessions (comma-separated):</label>
        <input type="text" id="study_sessions" name="study_sessions" required>
        <br>
        <button type="submit">Create Schedule</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Schedules</a>
</body>
</html>
```

3. `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Go to Home</a>
</body>
</html>
```

**Notes:**
- Ensure to install Flask and Flask-SQLAlchemy using pip if not already installed.
- The database is SQLite for simplicity; change the URI for production use.
- Replace `'your_secret_key'` with a strong secret key for session management.
- Adjust the templates as needed for production styling and structure.
