"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Generate code for a web-based dashboard that tracks SKI Foundation's "Magang dan Pendampingan Bisnis" participants' progress, including features for mentor feedback and task assignments.
Generated: DETERMINISTIC_cf2eba52892c282f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**dashboard.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ski_foundation.db"
db = SQLAlchemy(app)

# Define models for participants, mentors, and tasks
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    tasks = db.relationship("Task", backref="participant", lazy=True)

class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    feedbacks = db.relationship("Feedback", backref="mentor", lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey("participant.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")
    feedbacks = db.relationship("Feedback", backref="task", lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey("mentor.id"), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)
    comment = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the dashboard
@app.route("/")
def dashboard():
    participants = Participant.query.all()
    return render_template("dashboard.html", participants=participants)

# Route for participant details
@app.route("/participant/<int:participant_id>")
def participant_details(participant_id):
    participant = Participant.query.get_or_404(participant_id)
    tasks = participant.tasks.all()
    return render_template("participant_details.html", participant=participant, tasks=tasks)

# Route for task assignment
@app.route("/task/assign", methods=["POST"])
def assign_task():
    participant_id = request.form["participant_id"]
    task_title = request.form["task_title"]
    task_description = request.form["task_description"]
    participant = Participant.query.get(participant_id)
    if participant:
        task = Task(participant_id=participant_id, title=task_title, description=task_description)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("participant_details", participant_id=participant_id))
    return "Participant not found", 404

# Route for mentor feedback
@app.route("/feedback/add", methods=["POST"])
def add_feedback():
    mentor_id = request.form["mentor_id"]
    task_id = request.form["task_id"]
    comment = request.form["comment"]
    mentor = Mentor.query.get(mentor_id)
    task = Task.query.get(task_id)
    if mentor and task:
        feedback = Feedback(mentor_id=mentor_id, task_id=task_id, comment=comment)
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for("participant_details", participant_id=task.participant_id))
    return "Mentor or task not found", 404

# Route for updating task status
@app.route("/task/update_status", methods=["POST"])
def update_task_status():
    task_id = request.form["task_id"]
    status = request.form["status"]
    task = Task.query.get(task_id)
    if task:
        task.status = status
        db.session.commit()
        return redirect(url_for("participant_details", participant_id=task.participant_id))
    return "Task not found", 404

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/dashboard.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>SKI Foundation Dashboard</title>
</head>
<body>
    <h1>Participants</h1>
    <ul>
    {% for participant in participants %}
        <li>
            {{ participant.name }} ({{ participant.email }})
            <a href="{{ url_for('participant_details', participant_id=participant.id) }}">View Details</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/participant_details.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Participant Details</title>
</head>
<body>
    <h1>{{ participant.name }} ({{ participant.email }})</h1>
    <h2>Tasks</h2>
    <ul>
    {% for task in tasks %}
        <li>
            {{ task.title }} ({{ task.status }})
            <a href="#">View Feedback</a>
        </li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('assign_task') }}" method="post">
        <input type="hidden" name="participant_id" value="{{ participant.id }}">
        <input type="text" name="task_title" placeholder="Task title">
        <textarea name="task_description" placeholder="Task description"></textarea>
        <input type="submit" value="Assign Task">
    </form>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}
```
