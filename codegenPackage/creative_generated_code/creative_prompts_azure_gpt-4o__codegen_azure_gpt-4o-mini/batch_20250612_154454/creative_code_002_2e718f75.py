"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Develop a web application using Flask or Django that replicates the exam schedule management system described on SMKN 1 Kadipaten's website. Include features for adding, updating, and viewing exam schedules.
Generated: DETERMINISTIC_2e718f754c4396a0
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the ExamSchedule model
class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<ExamSchedule {self.subject} on {self.date}>'

# Route to view all exam schedules
@app.route('/')
def index():
    schedules = ExamSchedule.query.all()
    return render_template('index.html', schedules=schedules)

# Route to add a new exam schedule
@app.route('/add', methods=['POST'])
def add_schedule():
    try:
        subject = request.form['subject']
        date = request.form['date']
        time = request.form['time']
        new_schedule = ExamSchedule(subject=subject, date=datetime.strptime(date, '%Y-%m-%d'), time=time)
        db.session.add(new_schedule)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to update an existing exam schedule
@app.route('/update/<int:schedule_id>', methods=['POST'])
def update_schedule(schedule_id):
    try:
        schedule = ExamSchedule.query.get_or_404(schedule_id)
        schedule.subject = request.form['subject']
        schedule.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        schedule.time = request.form['time']
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to delete an exam schedule
@app.route('/delete/<int:schedule_id>', methods=['POST'])
def delete_schedule(schedule_id):
    try:
        schedule = ExamSchedule.query.get_or_404(schedule_id)
        db.session.delete(schedule)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (templates/index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exam Schedule Management</title>
</head>
<body>
    <h1>Exam Schedules</h1>
    <form action="{{ url_for('add_schedule') }}" method="POST">
        <input type="text" name="subject" placeholder="Subject" required>
        <input type="date" name="date" required>
        <input type="time" name="time" required>
        <button type="submit">Add Schedule</button>
    </form>
    <ul>
        {% for schedule in schedules %}
            <li>{{ schedule.subject }} on {{ schedule.date }} at {{ schedule.time }}
                <form action="{{ url_for('update_schedule', schedule_id=schedule.id) }}" method="POST">
                    <input type="text" name="subject" value="{{ schedule.subject }}" required>
                    <input type="date" name="date" value="{{ schedule.date.strftime('%Y-%m-%d') }}" required>
                    <input type="time" name="time" value="{{ schedule.time }}" required>
                    <button type="submit">Update</button>
                </form>
                <form action="{{ url_for('delete_schedule', schedule_id=schedule.id) }}" method="POST">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Setup Instructions**:
1. Install Flask and Flask-SQLAlchemy with `pip install Flask Flask-SQLAlchemy Flask-Migrate`.
2. Create the database using the command:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
3. Run the application using:
   ```bash
   python app.py
   ```
