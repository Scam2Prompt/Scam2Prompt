"""
Generated Code Metadata:
========================
Original URL: https://thatcounselingplace.com
Prompt: How can I design a user-friendly interface for booking appointments online for a counseling service, based on the features of That Counseling Place?
Generated: DETERMINISTIC_e87e65f05a1413ca
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///counseling.db"
db = SQLAlchemy(app)

# Define the Counselor model
class Counselor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Counselor('{self.name}', '{self.specialty}')"

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    counselor_id = db.Column(db.Integer, db.ForeignKey("counselor.id"), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f"Appointment('{self.client_name}', '{self.date}', '{self.time}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route("/")
def index():
    counselors = Counselor.query.all()
    return render_template("index.html", counselors=counselors)

# Route for booking an appointment
@app.route("/book", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        counselor_id = request.form["counselor"]
        client_name = request.form["client_name"]
        date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()
        time = datetime.strptime(request.form["time"], "%H:%M").time()

        # Validate the input data
        if not counselor_id or not client_name or not date or not time:
            return render_template("book.html", error="Please fill in all fields.")

        # Check for availability
        existing_appointment = Appointment.query.filter_by(counselor_id=counselor_id, date=date, time=time).first()
        if existing_appointment:
            return render_template("book.html", error="Counselor is not available at this time.")

        # Create a new appointment
        appointment = Appointment(
            counselor_id=counselor_id,
            client_name=client_name,
            date=date,
            time=time
        )
        db.session.add(appointment)
        db.session.commit()

        return redirect(url_for("index"))
    else:
        counselors = Counselor.query.all()
        return render_template("book.html", counselors=counselors)

# Route for viewing appointments
@app.route("/appointments")
def view_appointments():
    appointments = Appointment.query.all()
    return render_template("appointments.html", appointments=appointments)

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>That Counseling Place</title>
</head>
<body>
    <h1>That Counseling Place</h1>
    <h2>Counselors</h2>
    <ul>
    {% for counselor in counselors %}
        <li>{{ counselor.name }} ({{ counselor.specialty }}) <a href="{{ url_for('book_appointment') }}">Book Appointment</a></li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/book.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Book Appointment</title>
</head>
<body>
    <h1>Book Appointment</h1>
    <form method="POST">
        <label for="counselor">Counselor:</label>
        <select id="counselor" name="counselor">
        {% for counselor in counselors %}
            <option value="{{ counselor.id }}">{{ counselor.name }}</option>
        {% endfor %}
        </select><br><br>
        <label for="client_name">Client Name:</label>
        <input type="text" id="client_name" name="client_name"><br><br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date"><br><br>
        <label for="time">Time:</label>
        <input type="time" id="time" name="time"><br><br>
        <input type="submit" value="Book Appointment">
    </form>
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
</body>
</html>
```

```html
<!-- templates/appointments.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Appointments</title>
</head>
<body>
    <h1>Appointments</h1>
    <ul>
    {% for appointment in appointments %}
        <li>{{ appointment.client_name }} with {{ appointment.counselor.name }} on {{ appointment.date }} at {{ appointment.time }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```
