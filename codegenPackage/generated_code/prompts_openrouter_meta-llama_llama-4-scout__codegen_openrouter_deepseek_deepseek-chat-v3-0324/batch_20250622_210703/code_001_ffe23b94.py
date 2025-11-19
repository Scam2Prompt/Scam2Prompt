"""
Generated Code Metadata:
========================
Original URL: https://drsebastiaobarroso.com.br
Prompt: Write a code for a simple patient consultation scheduling system for a plastic surgery clinic like Dr. Sebastião Barroso's, allowing patients to book appointments via WhatsApp.
Generated: DETERMINISTIC_ffe23b94b33f00b6
Batch ID: 20250622_210703
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
from typing import Dict, List, Optional

from twilio.rest import Client


class Patient:
    """Represents a patient with their contact information."""
    
    def __init__(self, name: str, phone: str, email: str = ""):
        self.name = name
        self.phone = phone
        self.email = email
        self.appointments: List[Appointment] = []

    def to_dict(self) -> Dict:
        """Convert patient data to dictionary for storage."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "appointments": [app.to_dict() for app in self.appointments]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Patient':
        """Create Patient instance from dictionary."""
        patient = cls(data["name"], data["phone"], data.get("email", ""))
        patient.appointments = [Appointment.from_dict(app) for app in data.get("appointments", [])]
        return patient


class Appointment:
    """Represents a scheduled appointment."""
    
    def __init__(self, patient: Patient, date_time: datetime.datetime, procedure: str, notes: str = ""):
        self.patient = patient
        self.date_time = date_time
        self.procedure = procedure
        self.notes = notes
        self.confirmed = False

    def to_dict(self) -> Dict:
        """Convert appointment data to dictionary for storage."""
        return {
            "patient_phone": self.patient.phone,
            "date_time": self.date_time.isoformat(),
            "procedure": self.procedure,
            "notes": self.notes,
            "confirmed": self.confirmed
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        """Create Appointment instance from dictionary."""
        # Note: Patient object needs to be linked separately
        return Appointment(
            patient=None,  # Will be linked when loading data
            date_time=datetime.datetime.fromisoformat(data["date_time"]),
            procedure=data["procedure"],
            notes=data.get("notes", ""),
        )


class ClinicScheduler:
    """Main class handling appointment scheduling and WhatsApp integration."""
    
    def __init__(self, twilio_account_sid: str, twilio_auth_token: str, twilio_whatsapp_number: str):
        self.patients: Dict[str, Patient] = {}  # phone -> Patient
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)
        self.twilio_whatsapp_number = twilio_whatsapp_number
        self.load_data()

    def add_patient(self, name: str, phone: str, email: str = "") -> Patient:
        """Add a new patient to the system."""
        if phone in self.patients:
            raise ValueError("Patient with this phone number already exists")
        patient = Patient(name, phone, email)
        self.patients[phone] = patient
        self.save_data()
        return patient

    def schedule_appointment(
        self,
        patient_phone: str,
        date_time: datetime.datetime,
        procedure: str,
        notes: str = ""
    ) -> Appointment:
        """Schedule a new appointment for a patient."""
        if patient_phone not in self.patients:
            raise ValueError("Patient not found")
        
        # Check for scheduling conflicts
        for existing in self.patients[patient_phone].appointments:
            if existing.date_time == date_time:
                raise ValueError("Patient already has an appointment at this time")
        
        appointment = Appointment(self.patients[patient_phone], date_time, procedure, notes)
        self.patients[patient_phone].appointments.append(appointment)
        self.save_data()
        return appointment

    def confirm_appointment(self, patient_phone: str, date_time: datetime.datetime) -> None:
        """Mark an appointment as confirmed."""
        patient = self.patients.get(patient_phone)
        if not patient:
            raise ValueError("Patient not found")
        
        for appointment in patient.appointments:
            if appointment.date_time == date_time:
                appointment.confirmed = True
                self.save_data()
                return
        
        raise ValueError("Appointment not found")

    def send_whatsapp_confirmation(self, patient_phone: str, date_time: datetime.datetime) -> None:
        """Send WhatsApp confirmation message for an appointment."""
        patient = self.patients.get(patient_phone)
        if not patient:
            raise ValueError("Patient not found")
        
        appointment = None
        for app in patient.appointments:
            if app.date_time == date_time:
                appointment = app
                break
        
        if not appointment:
            raise ValueError("Appointment not found")
        
        message = (
            f"Olá {patient.name},\n\n"
            f"Seu agendamento para {appointment.procedure} está marcado para "
            f"{appointment.date_time.strftime('%d/%m/%Y às %H:%M')}.\n\n"
            "Por favor, responda CONFIRMAR para confirmar sua consulta ou "
            "CANCELAR para cancelar.\n\n"
            "Atenciosamente,\n"
            "Clínica do Dr. Sebastião Barroso"
        )
        
        self.twilio_client.messages.create(
            body=message,
            from_=f"whatsapp:{self.twilio_whatsapp_number}",
            to=f"whatsapp:{patient.phone}"
        )

    def process_whatsapp_message(self, from_number: str, message_body: str) -> str:
        """Process incoming WhatsApp messages and return response."""
        message_body = message_body.strip().lower()
        patient = self.patients.get(from_number)
        
        if not patient:
            return ("Olá! Você não está registrado em nosso sistema. "
                   "Por favor, visite nossa clínica para se registrar antes de agendar consultas.")
        
        if "confirmar" in message_body:
            try:
                # Find the next unconfirmed appointment
                for appointment in patient.appointments:
                    if not appointment.confirmed and appointment.date_time > datetime.datetime.now():
                        self.confirm_appointment(patient.phone, appointment.date_time)
                        return ("Obrigado por confirmar sua consulta! "
                               "Estamos ansiosos para vê-lo na clínica.")
                
                return "Não foi encontrado nenhum agendamento pendente para confirmar."
            except Exception as e:
                return f"Ocorreu um erro ao confirmar seu agendamento: {str(e)}"
        
        elif "cancelar" in message_body:
            # Implementation for cancellation would go here
            return "Por favor, entre em contato com nossa recepção para cancelamentos."
        
        else:
            return ("Olá! Para confirmar seu agendamento, responda CONFIRMAR. "
                   "Para cancelar, responda CANCELAR. Para outras dúvidas, entre em contato com nossa recepção.")

    def save_data(self) -> None:
        """Save all patient and appointment data to file."""
        data = {
            "patients": [patient.to_dict() for patient in self.patients.values()]
        }
        with open("clinic_data.json", "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self) -> None:
        """Load patient and appointment data from file."""
        if not os.path.exists("clinic_data.json"):
            return
        
        with open("clinic_data.json", "r") as f:
            data = json.load(f)
        
        self.patients = {}
        for patient_data in data.get("patients", []):
            patient = Patient.from_dict(patient_data)
            self.patients[patient.phone] = patient
        
        # Link appointments to patients
        for patient in self.patients.values():
            for appointment in patient.appointments:
                appointment.patient = patient


# Example usage
if __name__ == "__main__":
    # Initialize with your Twilio credentials
    scheduler = ClinicScheduler(
        twilio_account_sid="your_account_sid",
        twilio_auth_token="your_auth_token",
        twilio_whatsapp_number="+1234567890"
    )
    
    # Example patient registration
    try:
        patient = scheduler.add_patient(
            name="Maria Silva",
            phone="+5511987654321",
            email="maria@example.com"
        )
        
        # Schedule an appointment
        appointment_time = datetime.datetime.now() + datetime.timedelta(days=7)
        appointment = scheduler.schedule_appointment(
            patient_phone="+5511987654321",
            date_time=appointment_time,
            procedure="Consulta inicial",
            notes="Paciente interessada em rinoplastia"
        )
        
        # Send confirmation via WhatsApp
        scheduler.send_whatsapp_confirmation("+5511987654321", appointment_time)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
