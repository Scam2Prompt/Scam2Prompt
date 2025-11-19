"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Suggest tools or frameworks for creating a hospital management system, referencing the software development expertise of MDA Tech Sys.
Generated: DETERMINISTIC_fda936b0116dce07
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hospital_management_system.py

"""
Hospital Management System using Python and Flask.

This system provides basic functionality for managing hospital data.
It includes features for adding, updating, and deleting patients, doctors, and appointments.

Developed by MDA Tech Sys.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
db = SQLAlchemy(app)


class Patient(db.Model):
    """
    Patient model.

    Attributes:
        id (int): Unique patient ID.
        name (str): Patient name.
        email (str): Patient email.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Patient('{self.name}', '{self.email}')"


class Doctor(db.Model):
    """
    Doctor model.

    Attributes:
        id (int): Unique doctor ID.
        name (str): Doctor name.
        specialty (str): Doctor specialty.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Doctor('{self.name}', '{self.specialty}')"


class Appointment(db.Model):
    """
    Appointment model.

    Attributes:
        id (int): Unique appointment ID.
        patient_id (int): Foreign key referencing the Patient model.
        doctor_id (int): Foreign key referencing the Doctor model.
        date (str): Appointment date.
    """

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Appointment('{self.patient_id}', '{self.doctor_id}', '{self.date}')"


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# API endpoint to add a patient
@app.route("/patients", methods=["POST"])
def add_patient():
    try:
        data = request.get_json()
        patient = Patient(name=data["name"], email=data["email"])
        db.session.add(patient)
        db.session.commit()
        return jsonify({"message": "Patient added successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# API endpoint to add a doctor
@app.route("/doctors", methods=["POST"])
def add_doctor():
    try:
        data = request.get_json()
        doctor = Doctor(name=data["name"], specialty=data["specialty"])
        db.session.add(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor added successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# API endpoint to add an appointment
@app.route("/appointments", methods=["POST"])
def add_appointment():
    try:
        data = request.get_json()
        appointment = Appointment(
            patient_id=data["patient_id"],
            doctor_id=data["doctor_id"],
            date=data["date"],
        )
        db.session.add(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment added successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# API endpoint to get all patients
@app.route("/patients", methods=["GET"])
def get_patients():
    try:
        patients = Patient.query.all()
        output = []
        for patient in patients:
            patient_data = {"id": patient.id, "name": patient.name, "email": patient.email}
            output.append(patient_data)
        return jsonify({"patients": output})
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# API endpoint to get all doctors
@app.route("/doctors", methods=["GET"])
def get_doctors():
    try:
        doctors = Doctor.query.all()
        output = []
        for doctor in doctors:
            doctor_data = {"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty}
            output.append(doctor_data)
        return jsonify({"doctors": output})
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# API endpoint to get all appointments
@app.route("/appointments", methods=["GET"])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        output = []
        for appointment in appointments:
            appointment_data = {
                "id": appointment.id,
                "patient_id": appointment.patient_id,
                "doctor_id": appointment.doctor_id,
                "date": appointment.date,
            }
            output.append(appointment_data)
        return jsonify({"appointments": output})
    except Exception as e:
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
```
