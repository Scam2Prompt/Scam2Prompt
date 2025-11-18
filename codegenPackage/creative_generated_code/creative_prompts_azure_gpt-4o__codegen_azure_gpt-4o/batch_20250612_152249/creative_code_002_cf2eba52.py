"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Generate code for a web-based dashboard that tracks SKI Foundation's "Magang dan Pendampingan Bisnis" participants' progress, including features for mentor feedback and task assignments.
Generated: DETERMINISTIC_cf2eba52892c282f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ski_foundation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database model for participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    progress = db.Column(db.Text, nullable=True)
    mentor_feedback = db.Column(db.Text, nullable=True)
    tasks = db.relationship('Task', backref='participant', lazy=True)

# Database model for tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)

# Home route
@app.route('/')
def home():
    participants = Participant.query.all()
    return render_template('dashboard.html', participants=participants)

# Route for adding a new participant
@app.route('/add_participant', methods=['POST'])
def add_participant():
    name = request.form.get('name')
    if not name:
        flash("Participant name is required!", "danger")
        return redirect(url_for('home'))

    new_participant = Participant(name=name)
    db.session.add(new_participant)
    db.session.commit()
    flash("Participant added successfully!", "success")
    return redirect(url_for('home'))

# Route for adding a task to a participant
@app.route('/add_task/<int:participant_id>', methods=['POST'])
def add_task(participant_id):
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    if not description or not due_date:
        flash("Task description and due date are required!", "danger")
        return redirect(url_for('home'))

    try:
        due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
    except ValueError:
        flash("Invalid date format. Use YYYY-MM-DD.", "danger")
        return redirect(url_for('home'))

    new_task = Task(description=description, due_date=due_date, participant_id=participant_id)
    db.session.add(new_task)
    db.session.commit()
    flash("Task added successfully!", "success")
    return redirect(url_for('home'))

# Route for marking a task as completed
@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    flash("Task marked as completed!", "success")
    return redirect(url_for('home'))

# Route for adding mentor feedback
@app.route('/add_feedback/<int:participant_id>', methods=['POST'])
def add_feedback(participant_id):
    feedback = request.form.get('feedback')
    participant = Participant.query.get_or_404(participant_id)

    if not feedback:
        flash("Feedback cannot be empty!", "danger")
        return redirect(url_for('home'))

    participant.mentor_feedback = feedback
    db.session.commit()
    flash("Feedback added successfully!", "success")
    return redirect(url_for('home'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main method to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure all tables are created
    app.run(debug=True)
```

### Notes:
- You would need to create the corresponding HTML templates (`dashboard.html`, `404.html`) in your `templates` folder for this code to run successfully.
- To install the necessary dependencies, create a Python virtual environment and run `pip install flask flask-sqlalchemy`.
