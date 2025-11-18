"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://askcardiologist.in
Prompt: Write Python code to create a REST API for booking appointments with Dr. S. Nagendra Boopathy, including endpoints for patient details, available time slots, and confirmation emails.
Generated: DETERMINISTIC_c5b4c08598f6579a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Mock database for appointments and patients
appointments = []
patients = {}
available_slots = [
    {"date": (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
     "slots": ["09:00 AM", "10:00 AM", "11:00 AM", "02:00 PM", "03:00 PM"]}
    for i in range(7)
]

# Endpoint to add patient details
@app.route('/api/patient', methods=['POST'])
def add_patient():
    try:
        data = request.json
        if not data or not all(key in data for key in ("name", "email", "phone")):
            return jsonify({"error": "Invalid patient data"}), 400
        
        patient_id = len(patients) + 1
        patients[patient_id] = {
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"]
        }
        return jsonify({"message": "Patient added", "patient_id": patient_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get available time slots
@app.route('/api/available_slots', methods=['GET'])
def get_available_slots():
    try:
        return jsonify({"available_slots": available_slots}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to book an appointment
@app.route('/api/book_appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        if not data or not all(key in data for key in ("patient_id", "date", "time")):
            return jsonify({"error": "Invalid appointment data"}), 400
        
        # Validate patient ID
        patient = patients.get(data["patient_id"])
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
        
        # Validate time slot
        for slot in available_slots:
            if slot["date"] == data["date"] and data["time"] in slot["slots"]:
                slot["slots"].remove(data["time"])  # Remove the booked slot
                appointment_id = len(appointments) + 1
                appointment = {
                    "appointment_id": appointment_id,
                    "patient_id": data["patient_id"],
                    "date": data["date"],
                    "time": data["time"]
                }
                appointments.append(appointment)
                
                # Send confirmation email
                send_email_confirmation(patient["email"], appointment)
                
                return jsonify({"message": "Appointment booked", "appointment_id": appointment_id}), 201
        
        return jsonify({"error": "Invalid date or time slot"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def send_email_confirmation(email, appointment):
    try:
        subject = "Appointment Confirmation"
        body = (f"Dear Patient,\n\nYour appointment with Dr. S. Nagendra Boopathy has been "
                f"confirmed.\nDetails:\nDate: {appointment['date']}\nTime: {appointment['time']}\n\n"
                "Thank you!")
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "no-reply@hospital.com"
        msg['To'] = email
        
        # Simulating email sending (replace with actual SMTP server details in production)
        smtp = smtplib.SMTP('localhost')
        smtp.send_message(msg)
        smtp.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
