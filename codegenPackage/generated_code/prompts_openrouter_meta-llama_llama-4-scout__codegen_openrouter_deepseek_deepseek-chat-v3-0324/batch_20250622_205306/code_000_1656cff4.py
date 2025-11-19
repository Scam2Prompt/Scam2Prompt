"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and reminders, for a clinic like Studio Dentistico dott.ssa Vira Palazzo in Rome.
Generated: DETERMINISTIC_1656cff4b9bdc04c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
import smtplib
from email.mime.text import MIMEText
from typing import Dict, List, Optional, Tuple

class Patient:
    """Represents a patient with personal and contact information."""
    def __init__(self, patient_id: str, name: str, surname: str, phone: str, email: str):
        self.patient_id = patient_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def to_dict(self) -> Dict:
        """Convert patient object to dictionary for serialization."""
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Patient':
        """Create patient object from dictionary."""
        return cls(
            patient_id=data['patient_id'],
            name=data['name'],
            surname=data['surname'],
            phone=data['phone'],
            email=data['email']
        )

class Appointment:
    """Represents a dental appointment with patient and time details."""
    def __init__(self, appointment_id: str, patient: Patient, date_time: datetime.datetime, 
                 duration: int, notes: str = ""):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date_time = date_time
        self.duration = duration  # Duration in minutes
        self.notes = notes

    def to_dict(self) -> Dict:
        """Convert appointment object to dictionary for serialization."""
        return {
            'appointment_id': self.appointment_id,
            'patient': self.patient.to_dict(),
            'date_time': self.date_time.isoformat(),
            'duration': self.duration,
            'notes': self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        """Create appointment object from dictionary."""
        return cls(
            appointment_id=data['appointment_id'],
            patient=Patient.from_dict(data['patient']),
            date_time=datetime.datetime.fromisoformat(data['date_time']),
            duration=data['duration'],
            notes=data.get('notes', "")
        )

class DentalClinic:
    """Manages dental clinic appointments and patient records."""
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.patients_file = os.path.join(data_dir, "patients.json")
        self.appointments_file = os.path.join(data_dir, "appointments.json")
        self._ensure_data_dir_exists()
        self.patients = self._load_patients()
        self.appointments = self._load_appointments()

    def _ensure_data_dir_exists(self):
        """Ensure data directory exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _load_patients(self) -> Dict[str, Patient]:
        """Load patients from JSON file."""
        try:
            if os.path.exists(self.patients_file):
                with open(self.patients_file, 'r') as f:
                    patients_data = json.load(f)
                    return {p['patient_id']: Patient.from_dict(p) for p in patients_data}
            return {}
        except Exception as e:
            print(f"Error loading patients: {e}")
            return {}

    def _load_appointments(self) -> Dict[str, Appointment]:
        """Load appointments from JSON file."""
        try:
            if os.path.exists(self.appointments_file):
                with open(self.appointments_file, 'r') as f:
                    appointments_data = json.load(f)
                    return {a['appointment_id']: Appointment.from_dict(a) for a in appointments_data}
            return {}
        except Exception as e:
            print(f"Error loading appointments: {e}")
            return {}

    def _save_patients(self):
        """Save patients to JSON file."""
        try:
            with open(self.patients_file, 'w') as f:
                json.dump([p.to_dict() for p in self.patients.values()], f, indent=2)
        except Exception as e:
            print(f"Error saving patients: {e}")

    def _save_appointments(self):
        """Save appointments to JSON file."""
        try:
            with open(self.appointments_file, 'w') as f:
                json.dump([a.to_dict() for a in self.appointments.values()], f, indent=2)
        except Exception as e:
            print(f"Error saving appointments: {e}")

    def add_patient(self, patient: Patient) -> bool:
        """Add a new patient to the system."""
        if patient.patient_id in self.patients:
            print(f"Patient with ID {patient.patient_id} already exists.")
            return False
        self.patients[patient.patient_id] = patient
        self._save_patients()
        return True

    def get_patient(self, patient_id: str) -> Optional[Patient]:
        """Retrieve a patient by ID."""
        return self.patients.get(patient_id)

    def schedule_appointment(self, appointment: Appointment) -> bool:
        """Schedule a new appointment."""
        # Check for time conflicts
        for existing_appointment in self.appointments.values():
            existing_start = existing_appointment.date_time
            existing_end = existing_start + datetime.timedelta(minutes=existing_appointment.duration)
            new_start = appointment.date_time
            new_end = new_start + datetime.timedelta(minutes=appointment.duration)
            
            if (new_start < existing_end) and (new_end > existing_start):
                print(f"Time conflict with appointment {existing_appointment.appointment_id}")
                return False

        self.appointments[appointment.appointment_id] = appointment
        self._save_appointments()
        return True

    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an existing appointment."""
        if appointment_id not in self.appointments:
            print(f"Appointment with ID {appointment_id} not found.")
            return False
        del self.appointments[appointment_id]
        self._save_appointments()
        return True

    def get_appointments_for_day(self, date: datetime.date) -> List[Appointment]:
        """Get all appointments for a specific day."""
        return [
            app for app in self.appointments.values()
            if app.date_time.date() == date
        ]

    def get_upcoming_appointments(self, days: int = 7) -> List[Appointment]:
        """Get appointments scheduled within the next specified days."""
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days)
        return [
            app for app in self.appointments.values()
            if now <= app.date_time <= end_date
        ]

    def send_reminders(self, smtp_server: str, smtp_port: int, 
                       sender_email: str, sender_password: str, 
                       days_before: int = 1) -> Tuple[int, int]:
        """Send email reminders for upcoming appointments."""
        now = datetime.datetime.now()
        reminder_date = now + datetime.timedelta(days=days_before)
        appointments_to_remind = [
            app for app in self.appointments.values()
            if app.date_time.date() == reminder_date.date()
        ]

        success_count = 0
        failure_count = 0

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            for appointment in appointments_to_remind:
                patient = appointment.patient
                subject = f"Reminder: Dental Appointment on {appointment.date_time.strftime('%Y-%m-%d at %H:%M')}"
                body = f"""Dear {patient.name} {patient.surname},

This is a reminder for your dental appointment at Studio Dentistico dott.ssa Vira Palazzo on:
{appointment.date_time.strftime('%A, %B %d, %Y at %H:%M')}

Duration: {appointment.duration} minutes
Notes: {appointment.notes}

Please arrive 10 minutes before your scheduled time.

If you need to reschedule or cancel, please contact us at +39 06 1234567.

Best regards,
Studio Dentistico dott.ssa Vira Palazzo
"""

                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = patient.email

                try:
                    server.sendmail(sender_email, [patient.email], msg.as_string())
                    success_count += 1
                except Exception as e:
                    print(f"Failed to send reminder to {patient.email}: {e}")
                    failure_count += 1

            server.quit()
        except Exception as e:
            print(f"Error connecting to SMTP server: {e}")
            failure_count = len(appointments_to_remind)

        return success_count, failure_count

def generate_id(prefix: str = "ID") -> str:
    """Generate a simple unique ID with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d%
