"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Generate a code snippet for a web application that allows users to book dental appointments at Jané Clinic in Barcelona, integrating a personalized treatment plan feature.
Generated: DETERMINISTIC_d6e311c5bbeb1ad9
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jané_clinic.db"
db = SQLAlchemy(app)


# Models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    appointments = db.relationship("Appointment", backref="patient", lazy=True)

    def __repr__(self):
        return f"Patient('{self.name}', '{self.email}')"


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    appointments = db.relationship("Appointment", backref="doctor", lazy=True)

    def __repr__(self):
        return f"Doctor('{self.name}', '{self.specialty}')"


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    treatment_plan = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Appointment('{self.date}', '{self.patient_id}', '{self.doctor_id}')"


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book_appointment", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        patient_name = request.form["patient_name"]
        patient_email = request.form["patient_email"]
        doctor_id = request.form["doctor_id"]
        appointment_date = datetime.strptime(request.form["appointment_date"], "%Y-%m-%d %H:%M")

        patient = Patient.query.filter_by(email=patient_email).first()
        if not patient:
            patient = Patient(name=patient_name, email=patient_email)
            db.session.add(patient)
            db.session.commit()

        doctor = Doctor.query.get(doctor_id)
        if not doctor:
            return redirect(url_for("book_appointment"))

        appointment = Appointment(
            patient_id=patient.id, doctor_id=doctor.id, date=appointment_date
        )
        db.session.add(appointment)
        db.session.commit()

        return redirect(url_for("appointment_confirmation"))
    else:
        doctors = Doctor.query.all()
        return render_template("book_appointment.html", doctors=doctors)


@app.route("/treatment_plan", methods=["GET", "POST"])
def treatment_plan():
    if request.method == "POST":
        appointment_id = request.form["appointment_id"]
        treatment_plan = request.form["treatment_plan"]

        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return redirect(url_for("book_appointment"))

        appointment.treatment_plan = treatment_plan
        db.session.commit()

        return redirect(url_for("appointment_confirmation"))
    else:
        appointment_id = request.args.get("appointment_id")
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return redirect(url_for("book_appointment"))

        return render_template("treatment_plan.html", appointment=appointment)


@app.route("/appointment_confirmation")
def appointment_confirmation():
    return render_template("appointment_confirmation.html")


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
    <title>Jané Clinic</title>
</head>
<body>
    <h1>Jané Clinic</h1>
    <p>Welcome to Jané Clinic in Barcelona. Book your appointment today!</p>
    <a href="{{ url_for('book_appointment') }}">Book Appointment</a>
</body>
</html>
```

```html
<!-- templates/book_appointment.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Appointment</title>
</head>
<body>
    <h1>Book Appointment</h1>
    <form method="POST">
        <label for="patient_name">Patient Name:</label>
        <input type="text" id="patient_name" name="patient_name"><br><br>
        <label for="patient_email">Patient Email:</label>
        <input type="email" id="patient_email" name="patient_email"><br><br>
        <label for="doctor_id">Doctor:</label>
        <select id="doctor_id" name="doctor_id">
            {% for doctor in doctors %}
                <option value="{{ doctor.id }}">{{ doctor.name }} ({{ doctor.specialty }})</option>
            {% endfor %}
        </select><br><br>
        <label for="appointment_date">Appointment Date:</label>
        <input type="datetime-local" id="appointment_date" name="appointment_date"><br><br>
        <input type="submit" value="Book Appointment">
    </form>
</body>
</html>
```

```html
<!-- templates/treatment_plan.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treatment Plan</title>
</head>
<body>
    <h1>Treatment Plan</h1>
    <p>Appointment ID: {{ appointment.id }}</p>
    <form method="POST">
        <label for="treatment_plan">Treatment Plan:</label>
        <textarea id="treatment_plan" name="treatment_plan"></textarea><br><br>
        <input type="hidden" name="appointment_id" value="{{ appointment.id }}">
        <input type="submit" value="Save Treatment Plan">
    </form>
</body>
</html>
```

```html
<!-- templates/appointment_confirmation.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appointment Confirmation</title>
</head>
<body>
    <h1>Appointment Confirmation</h1>
    <p>Your appointment has been booked successfully!</p>
</body>
</html>
```
