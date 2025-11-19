"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Generate code for a transportation scheduling system for elderly clients, ensuring integration with medical appointment reminders, as described in Home Care Assistance Barrie's service offerings.
Generated: DETERMINISTIC_90d667007282e925
Batch ID: 20250612_152020
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
from typing import List, Dict, Optional
from enum import Enum

class TransportationStatus(Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class AppointmentType(Enum):
    MEDICAL = "Medical"
    SOCIAL = "Social"
    OTHER = "Other"

class Client:
    def __init__(self, client_id: str, name: str, address: str, phone: str, medical_conditions: List[str]):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.phone = phone
        self.medical_conditions = medical_conditions

    def to_dict(self) -> Dict:
        return {
            "client_id": self.client_id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "medical_conditions": self.medical_conditions
        }

class Appointment:
    def __init__(self, appointment_id: str, client_id: str, appointment_type: AppointmentType, 
                 date_time: datetime.datetime, location: str, notes: str = ""):
        self.appointment_id = appointment_id
        self.client_id = client_id
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.location = location
        self.notes = notes

    def to_dict(self) -> Dict:
        return {
            "appointment_id": self.appointment_id,
            "client_id": self.client_id,
            "appointment_type": self.appointment_type.value,
            "date_time": self.date_time.isoformat(),
            "location": self.location,
            "notes": self.notes
        }

class TransportationSchedule:
    def __init__(self, schedule_id: str, client_id: str, appointment_id: str, 
                 pickup_time: datetime.datetime, status: TransportationStatus = TransportationStatus.SCHEDULED):
        self.schedule_id = schedule_id
        self.client_id = client_id
        self.appointment_id = appointment_id
        self.pickup_time = pickup_time
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "schedule_id": self.schedule_id,
            "client_id": self.client_id,
            "appointment_id": self.appointment_id,
            "pickup_time": self.pickup_time.isoformat(),
            "status": self.status.value
        }

class TransportationScheduler:
    def __init__(self):
        self.clients: Dict[str, Client] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.schedules: Dict[str, TransportationSchedule] = {}

    def add_client(self, client: Client) -> None:
        if client.client_id in self.clients:
            raise ValueError(f"Client with ID {client.client_id} already exists")
        self.clients[client.client_id] = client

    def add_appointment(self, appointment: Appointment) -> None:
        if appointment.client_id not in self.clients:
            raise ValueError(f"Client with ID {appointment.client_id} not found")
        if appointment.appointment_id in self.appointments:
            raise ValueError(f"Appointment with ID {appointment.appointment_id} already exists")
        self.appointments[appointment.appointment_id] = appointment

    def schedule_transportation(self, schedule: TransportationSchedule) -> None:
        if schedule.client_id not in self.clients:
            raise ValueError(f"Client with ID {schedule.client_id} not found")
        if schedule.appointment_id not in self.appointments:
            raise ValueError(f"Appointment with ID {schedule.appointment_id} not found")
        if schedule.schedule_id in self.schedules:
            raise ValueError(f"Schedule with ID {schedule.schedule_id} already exists")
        
        appointment = self.appointments[schedule.appointment_id]
        if schedule.pickup_time > appointment.date_time:
            raise ValueError("Pickup time cannot be after appointment time")
        
        self.schedules[schedule.schedule_id] = schedule

    def get_client_schedules(self, client_id: str) -> List[TransportationSchedule]:
        if client_id not in self.clients:
            raise ValueError(f"Client with ID {client_id} not found")
        return [s for s in self.schedules.values() if s.client_id == client_id]

    def update_schedule_status(self, schedule_id: str, status: TransportationStatus) -> None:
        if schedule_id not in self.schedules:
            raise ValueError(f"Schedule with ID {schedule_id} not found")
        self.schedules[schedule_id].status = status

    def get_upcoming_medical_reminders(self, days_ahead: int = 1) -> List[Dict]:
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days_ahead)
        
        reminders = []
        for schedule in self.schedules.values():
            appointment = self.appointments[schedule.appointment_id]
            if (appointment.appointment_type == AppointmentType.MEDICAL and 
                now <= appointment.date_time <= end_date):
                client = self.clients[schedule.client_id]
                reminders.append({
                    "client": client.to_dict(),
                    "appointment": appointment.to_dict(),
                    "schedule": schedule.to_dict(),
                    "reminder_time": appointment.date_time - datetime.timedelta(hours=1)
                })
        return reminders

    def save_to_file(self, filename: str) -> None:
        data = {
            "clients": [client.to_dict() for client in self.clients.values()],
            "appointments": [app.to_dict() for app in self.appointments.values()],
            "schedules": [sched.to_dict() for sched in self.schedules.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.clients = {}
        self.appointments = {}
        self.schedules = {}
        
        for client_data in data["clients"]:
            client = Client(
                client_data["client_id"],
                client_data["name"],
                client_data["address"],
                client_data["phone"],
                client_data["medical_conditions"]
            )
            self.clients[client.client_id] = client
        
        for app_data in data["appointments"]:
            appointment = Appointment(
                app_data["appointment_id"],
                app_data["client_id"],
                AppointmentType(app_data["appointment_type"]),
                datetime.datetime.fromisoformat(app_data["date_time"]),
                app_data["location"],
                app_data.get("notes", "")
            )
            self.appointments[appointment.appointment_id] = appointment
        
        for sched_data in data["schedules"]:
            schedule = TransportationSchedule(
                sched_data["schedule_id"],
                sched_data["client_id"],
                sched_data["appointment_id"],
                datetime.datetime.fromisoformat(sched_data["pickup_time"]),
                TransportationStatus(sched_data["status"])
            )
            self.schedules[schedule.schedule_id] = schedule

# Example usage
if __name__ == "__main__":
    scheduler = TransportationScheduler()
    
    # Add a client
    client = Client(
        "client1",
        "John Doe",
        "123 Main St, Barrie, ON",
        "555-123-4567",
        ["Diabetes", "High Blood Pressure"]
    )
    scheduler.add_client(client)
    
    # Add a medical appointment
    appointment = Appointment(
        "app1",
        "client1",
        AppointmentType.MEDICAL,
        datetime.datetime.now() + datetime.timedelta(days=1),
        "Barrie Medical Center",
        "Annual checkup with Dr. Smith"
    )
    scheduler.add_appointment(appointment)
    
    # Schedule transportation
    schedule = TransportationSchedule(
        "sched1",
        "client1",
        "app1",
        datetime.datetime.now() + datetime.timedelta(days=1) - datetime.timedelta(minutes=30)
    )
    scheduler.schedule_transportation(schedule)
    
    # Get reminders
    reminders = scheduler.get_upcoming_medical_reminders()
    print("Upcoming medical reminders:")
    for reminder in reminders:
        print(f"Client: {reminder['client']['name']}")
        print(f"Appointment: {reminder['appointment']['location']} at {reminder['appointment']['date_time']}")
        print(f"Pickup: {reminder['schedule']['pickup_time']}")
        print("---")
    
    # Save to file
    scheduler.save_to_file("transportation_schedule.json")
```
