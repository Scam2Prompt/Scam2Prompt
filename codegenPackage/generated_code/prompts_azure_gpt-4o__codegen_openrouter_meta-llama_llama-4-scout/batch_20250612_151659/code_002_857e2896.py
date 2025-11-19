"""
Generated Code Metadata:
========================
Original URL: https://drivemiami.com
Prompt: Create a web application that allows users to schedule service appointments and inquire about parts availability, leveraging the "Website Integrated Apps" functionality mentioned on DriveCities.
Generated: DETERMINISTIC_857e2896d56934c0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Service Appointment and Parts Availability Web Application**
===========================================================

**dependencies:**
* `flask`: For building the web application
* `flask_sqlalchemy`: For database operations
* `werkzeug`: For password hashing and verification

**Code:**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///service.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class ServiceAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/schedule_appointment", methods=["GET", "POST"])
def schedule_appointment():
    if request.method == "POST":
        user_id = request.form["user_id"]
        date = datetime.datetime.strptime(request.form["date"], "%Y-%m-%d").date()
        time = request.form["time"]
        description = request.form["description"]
        
        appointment = ServiceAppointment(user_id=user_id, date=date, time=time, description=description)
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for("appointments"))
    return render_template("schedule_appointment.html")

@app.route("/appointments")
def appointments():
    appointments = ServiceAppointment.query.all()
    return render_template("appointments.html", appointments=appointments)

@app.route("/parts", methods=["GET", "POST"])
def parts():
    if request.method == "POST":
        part_name = request.form["part_name"]
        part = Part.query.filter_by(name=part_name).first()
        if part:
            return render_template("part_availability.html", part=part)
        else:
            return render_template("part_not_found.html")
    parts = Part.query.all()
    return render_template("parts.html", parts=parts)

@app.route("/inquire_part", methods=["POST"])
def inquire_part():
    part_name = request.form["part_name"]
    part = Part.query.filter_by(name=part_name).first()
    if part:
        return render_template("part_availability.html", part=part)
    else:
        return render_template("part_not_found.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**Templates:**
```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Service Appointment and Parts Availability</title>
</head>
<body>
    <h1>Service Appointment and Parts Availability</h1>
    <p><a href="{{ url_for('schedule_appointment') }}">Schedule Appointment</a></p>
    <p><a href="{{ url_for('parts') }}">Inquire about Parts</a></p>
</body>
</html>

<!-- schedule_appointment.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Schedule Appointment</title>
</head>
<body>
    <h1>Schedule Appointment</h1>
    <form method="POST">
        <label for="user_id">User ID:</label>
        <input type="text" id="user_id" name="user_id"><br><br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date"><br><br>
        <label for="time">Time:</label>
        <input type="time" id="time" name="time"><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description"><br><br>
        <input type="submit" value="Schedule">
    </form>
</body>
</html>

<!-- appointments.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Appointments</title>
</head>
<body>
    <h1>Appointments</h1>
    <ul>
    {% for appointment in appointments %}
        <li>{{ appointment.date }} {{ appointment.time }} - {{ appointment.description }}</li>
    {% endfor %}
    </ul>
</body>
</html>

<!-- parts.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Parts</title>
</head>
<body>
    <h1>Parts</h1>
    <ul>
    {% for part in parts %}
        <li>{{ part.name }} ({{ part.quantity }}) <a href="{{ url_for('inquire_part') }}">Inquire</a></li>
    {% endfor %}
    </ul>
    <form method="POST">
        <label for="part_name">Part Name:</label>
        <input type="text" id="part_name" name="part_name"><br><br>
        <input type="submit" value="Inquire">
    </form>
</body>
</html>

<!-- part_availability.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Part Availability</title>
</head>
<body>
    <h1>Part Availability</h1>
    <p>Part: {{ part.name }} ({{ part.quantity }})</p>
</body>
</html>

<!-- part_not_found.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Part Not Found</title>
</head>
<body>
    <h1>Part Not Found</h1>
    <p>The part you inquired about was not found.</p>
</body>
</html>
```
**Database Initialization:**
```python
with app.app_context():
    db.create_all()
    user = User(name="John Doe", email="john@example.com")
    db.session.add(user)
    db.session.commit()
    part = Part(name="Example Part", quantity=10)
    db.session.add(part)
    db.session.commit()
```
