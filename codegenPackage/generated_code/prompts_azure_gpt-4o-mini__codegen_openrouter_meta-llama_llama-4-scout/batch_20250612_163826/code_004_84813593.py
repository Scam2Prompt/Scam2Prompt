"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Design a simple web application that displays training schedules and upcoming events for a running club, using Thompson Estate Athletics as a model.
Generated: DETERMINISTIC_8481359393ece44c
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Thompson Estate Athletics Web Application**
=============================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///thompson_estate_athletics.db"
db = SQLAlchemy(app)


# Models
class TrainingSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"TrainingSchedule('{self.date}', '{self.time}', '{self.description}')"


class UpcomingEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"UpcomingEvent('{self.date}', '{self.time}', '{self.description}')"


# Routes
@app.route("/")
def index():
    training_schedules = TrainingSchedule.query.all()
    upcoming_events = UpcomingEvent.query.all()
    return render_template("index.html", training_schedules=training_schedules, upcoming_events=upcoming_events)


@app.route("/add_training_schedule", methods=["GET", "POST"])
def add_training_schedule():
    if request.method == "POST":
        try:
            date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()
            time = request.form["time"]
            description = request.form["description"]
            training_schedule = TrainingSchedule(date=date, time=time, description=description)
            db.session.add(training_schedule)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return str(e)
    return render_template("add_training_schedule.html")


@app.route("/add_upcoming_event", methods=["GET", "POST"])
def add_upcoming_event():
    if request.method == "POST":
        try:
            date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()
            time = request.form["time"]
            description = request.form["description"]
            upcoming_event = UpcomingEvent(date=date, time=time, description=description)
            db.session.add(upcoming_event)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return str(e)
    return render_template("add_upcoming_event.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thompson Estate Athletics</title>
</head>
<body>
    <h1>Training Schedules</h1>
    <ul>
    {% for training_schedule in training_schedules %}
        <li>{{ training_schedule.date }} - {{ training_schedule.time }}: {{ training_schedule.description }}</li>
    {% endfor %}
    </ul>

    <h1>Upcoming Events</h1>
    <ul>
    {% for upcoming_event in upcoming_events %}
        <li>{{ upcoming_event.date }} - {{ upcoming_event.time }}: {{ upcoming_event.description }}</li>
    {% endfor %}
    </ul>

    <p><a href="{{ url_for('add_training_schedule') }}">Add Training Schedule</a></p>
    <p><a href="{{ url_for('add_upcoming_event') }}">Add Upcoming Event</a></p>
</body>
</html>
```

```html
<!-- templates/add_training_schedule.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Training Schedule</title>
</head>
<body>
    <h1>Add Training Schedule</h1>
    <form method="POST">
        <label for="date">Date:</label>
        <input type="date" id="date" name="date"><br><br>
        <label for="time">Time:</label>
        <input type="text" id="time" name="time"><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```html
<!-- templates/add_upcoming_event.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Upcoming Event</title>
</head>
<body>
    <h1>Add Upcoming Event</h1>
    <form method="POST">
        <label for="date">Date:</label>
        <input type="date" id="date" name="date"><br><br>
        <label for="time">Time:</label>
        <input type="text" id="time" name="time"><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
