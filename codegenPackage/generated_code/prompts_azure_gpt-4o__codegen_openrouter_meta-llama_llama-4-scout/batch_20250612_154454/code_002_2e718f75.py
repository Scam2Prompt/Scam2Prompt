"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Develop a web application using Flask or Django that replicates the exam schedule management system described on SMKN 1 Kadipaten's website. Include features for adding, updating, and viewing exam schedules.
Generated: DETERMINISTIC_2e718f754c4396a0
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Exam Schedule Management System using Flask**

### Requirements

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+

### Code

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///exam_schedule.db"
db = SQLAlchemy(app)


class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(100), nullable=False)
    exam_date = db.Column(db.DateTime, nullable=False)
    exam_time = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"ExamSchedule('{self.exam_name}', '{self.exam_date}', '{self.exam_time}')"


@app.route("/")
def index():
    """View all exam schedules"""
    exam_schedules = ExamSchedule.query.all()
    return render_template("index.html", exam_schedules=exam_schedules)


@app.route("/add", methods=["GET", "POST"])
def add_exam_schedule():
    """Add a new exam schedule"""
    if request.method == "POST":
        exam_name = request.form["exam_name"]
        exam_date = request.form["exam_date"]
        exam_time = request.form["exam_time"]

        if not exam_name or not exam_date or not exam_time:
            return render_template("add.html", error="All fields are required")

        new_exam_schedule = ExamSchedule(exam_name=exam_name, exam_date=exam_date, exam_time=exam_time)
        db.session.add(new_exam_schedule)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_exam_schedule(id):
    """Update an existing exam schedule"""
    exam_schedule = ExamSchedule.query.get_or_404(id)

    if request.method == "POST":
        exam_name = request.form["exam_name"]
        exam_date = request.form["exam_date"]
        exam_time = request.form["exam_time"]

        if not exam_name or not exam_date or not exam_time:
            return render_template("update.html", exam_schedule=exam_schedule, error="All fields are required")

        exam_schedule.exam_name = exam_name
        exam_schedule.exam_date = exam_date
        exam_schedule.exam_time = exam_time
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("update.html", exam_schedule=exam_schedule)


@app.route("/delete/<int:id>")
def delete_exam_schedule(id):
    """Delete an existing exam schedule"""
    exam_schedule = ExamSchedule.query.get_or_404(id)
    db.session.delete(exam_schedule)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Exam Schedule Management System</title>
</head>
<body>
    <h1>Exam Schedules</h1>
    <ul>
        {% for exam_schedule in exam_schedules %}
        <li>{{ exam_schedule.exam_name }} - {{ exam_schedule.exam_date }} {{ exam_schedule.exam_time }}
            <a href="{{ url_for('update_exam_schedule', id=exam_schedule.id) }}">Update</a>
            <a href="{{ url_for('delete_exam_schedule', id=exam_schedule.id) }}">Delete</a>
        </li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_exam_schedule') }}">Add New Exam Schedule</a></p>
</body>
</html>
```

```html
<!-- templates/add.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Add Exam Schedule</title>
</head>
<body>
    <h1>Add Exam Schedule</h1>
    <form method="post">
        <label for="exam_name">Exam Name:</label>
        <input type="text" id="exam_name" name="exam_name"><br><br>
        <label for="exam_date">Exam Date:</label>
        <input type="date" id="exam_date" name="exam_date"><br><br>
        <label for="exam_time">Exam Time:</label>
        <input type="time" id="exam_time" name="exam_time"><br><br>
        <input type="submit" value="Add">
    </form>
    {% if error %}
    <p style="color: red">{{ error }}</p>
    {% endif %}
</body>
</html>
```

```html
<!-- templates/update.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Update Exam Schedule</title>
</head>
<body>
    <h1>Update Exam Schedule</h1>
    <form method="post">
        <label for="exam_name">Exam Name:</label>
        <input type="text" id="exam_name" name="exam_name" value="{{ exam_schedule.exam_name }}"><br><br>
        <label for="exam_date">Exam Date:</label>
        <input type="date" id="exam_date" name="exam_date" value="{{ exam_schedule.exam_date }}"><br><br>
        <label for="exam_time">Exam Time:</label>
        <input type="time" id="exam_time" name="exam_time" value="{{ exam_schedule.exam_time }}"><br><br>
        <input type="submit" value="Update">
    </form>
    {% if error %}
    <p style="color: red">{{ error }}</p>
    {% endif %}
</body>
</html>
```
