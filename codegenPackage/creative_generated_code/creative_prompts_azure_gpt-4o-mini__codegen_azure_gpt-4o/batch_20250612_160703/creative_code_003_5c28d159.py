"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medex.trakmd.dev
Prompt: Generate a sample patient portal interface that allows users to connect with doctors online, inspired by trakMD’s features.
Generated: DETERMINISTIC_5c28d159044b46a4
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Mock data for demonstration purposes
patients = [
    {"id": 1, "name": "Alice Johnson", "age": 30, "email": "alice@example.com"},
    {"id": 2, "name": "Bob Smith", "age": 40, "email": "bob@example.com"},
]

doctors = [
    {"id": 1, "name": "Dr. Emily Carter", "specialization": "Cardiology", "availability": "10 AM - 2 PM"},
    {"id": 2, "name": "Dr. Michael Brown", "specialization": "Dermatology", "availability": "1 PM - 5 PM"},
]

appointments = []


# Define routes for the patient portal

@app.route("/")
def home():
    """
    Home route displaying options for Patients and Doctors.
    """
    return render_template("home.html")


@app.route("/patients")
def list_patients():
    """
    Display a list of all registered patients.
    """
    return render_template("patients.html", patients=patients)


@app.route("/doctors")
def list_doctors():
    """
    Display a list of all available doctors.
    """
    return render_template("doctors.html", doctors=doctors)


@app.route("/appointment", methods=["GET", "POST"])
def book_appointment():
    """
    Allow patients to book an appointment with a doctor.
    """
    if request.method == "POST":
        try:
            patient_id = int(request.form["patient_id"])
            doctor_id = int(request.form["doctor_id"])
            appointment_date = request.form["appointment_date"]

            # Validate input
            if not any(p["id"] == patient_id for p in patients):
                return jsonify({"error": "Invalid patient ID"}), 400

            if not any(d["id"] == doctor_id for d in doctors):
                return jsonify({"error": "Invalid doctor ID"}), 400

            # Create and store the appointment
            appointments.append({
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "appointment_date": appointment_date
            })

            return redirect(url_for("view_appointments"))
        except ValueError:
            return jsonify({"error": "Invalid input"}), 400
    return render_template("appointment.html", patients=patients, doctors=doctors)


@app.route("/appointments")
def view_appointments():
    """
    Display all booked appointments.
    """
    return render_template("appointments.html", appointments=appointments)


# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors gracefully.
    """
    return render_template("404.html"), 404


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### HTML Templates

#### `templates/home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Patient Portal</title>
</head>
<body>
    <h1>Welcome to the Patient Portal</h1>
    <a href="/patients">View Patients</a><br>
    <a href="/doctors">View Doctors</a><br>
    <a href="/appointment">Book Appointment</a><br>
    <a href="/appointments">View Appointments</a><br>
</body>
</html>
```

#### `templates/patients.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Patients</title>
</head>
<body>
    <h1>List of Patients</h1>
    <ul>
        {% for patient in patients %}
            <li>{{ patient.name }} (Age: {{ patient.age }}, Email: {{ patient.email }})</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/doctors.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Doctors</title>
</head>
<body>
    <h1>List of Doctors</h1>
    <ul>
        {% for doctor in doctors %}
            <li>{{ doctor.name }} (Specialization: {{ doctor.specialization }}, Availability: {{ doctor.availability }})</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/appointment.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Book Appointment</title>
</head>
<body>
    <h1>Book an Appointment</h1>
    <form method="POST">
        <label for="patient_id">Patient ID:</label>
        <input type="number" id="patient_id" name="patient_id"><br>

        <label for="doctor_id">Doctor ID:</label>
        <input type="number" id="doctor_id" name="doctor_id"><br>

        <label for="appointment_date">Appointment Date:</label>
        <input type="date" id="appointment_date" name="appointment_date"><br>

        <button type="submit">Book</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/appointments.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Appointments</title>
</head>
<body>
    <h1>List of Appointments</h1>
    <ul>
        {% for appointment in appointments %}
            <li>Patient ID: {{ appointment.patient_id }}, Doctor ID: {{ appointment.doctor_id }}, Appointment Date: {{ appointment.appointment_date }}</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Back to Home</a>
</body>
</html>
```
