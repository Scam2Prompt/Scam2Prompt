"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Write a Python script to manage appointment scheduling and call answering for a construction subcontractor business using a virtual receptionist service.
Generated: DETERMINISTIC_836cbc4bc1274171
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional
import os
import uuid
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class CallStatus(Enum):
    ANSWERED = "Answered"
    MISSED = "Missed"
    VOICEMAIL = "Voicemail"


class Appointment:
    def __init__(
        self,
        client_name: str,
        date_time: datetime.datetime,
        description: str,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED,
        appointment_id: Optional[str] = None,
    ):
        self.appointment_id = appointment_id or str(uuid.uuid4())
        self.client_name = client_name
        self.date_time = date_time
        self.description = description
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "appointment_id": self.appointment_id,
            "client_name": self.client_name,
            "date_time": self.date_time.isoformat(),
            "description": self.description,
            "status": self.status.value,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Appointment":
        return cls(
            appointment_id=data["appointment_id"],
            client_name=data["client_name"],
            date_time=datetime.datetime.fromisoformat(data["date_time"]),
            description=data["description"],
            status=AppointmentStatus(data["status"]),
        )


class CallRecord:
    def __init__(
        self,
        caller_name: str,
        phone_number: str,
        call_time: datetime.datetime,
        status: CallStatus,
        notes: str = "",
        call_id: Optional[str] = None,
    ):
        self.call_id = call_id or str(uuid.uuid4())
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.call_time = call_time
        self.status = status
        self.notes = notes

    def to_dict(self) -> Dict:
        return {
            "call_id": self.call_id,
            "caller_name": self.caller_name,
            "phone_number": self.phone_number,
            "call_time": self.call_time.isoformat(),
            "status": self.status.value,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "CallRecord":
        return cls(
            call_id=data["call_id"],
            caller_name=data["caller_name"],
            phone_number=data["phone_number"],
            call_time=datetime.datetime.fromisoformat(data["call_time"]),
            status=CallStatus(data["status"]),
            notes=data.get("notes", ""),
        )


class AppointmentManager:
    def __init__(self, data_file: str = "appointments.json"):
        self.data_file = data_file
        self.appointments: Dict[str, Appointment] = {}
        self.load_appointments()

    def load_appointments(self) -> None:
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.appointments = {
                        appt["appointment_id"]: Appointment.from_dict(appt)
                        for appt in data
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading appointments: {e}")
                self.appointments = {}

    def save_appointments(self) -> None:
        try:
            with open(self.data_file, "w") as f:
                json.dump(
                    [appt.to_dict() for appt in self.appointments.values()],
                    f,
                    indent=2,
                )
        except IOError as e:
            print(f"Error saving appointments: {e}")

    def add_appointment(self, appointment: Appointment) -> None:
        self.appointments[appointment.appointment_id] = appointment
        self.save_appointments()

    def update_appointment_status(
        self, appointment_id: str, status: AppointmentStatus
    ) -> None:
        if appointment_id in self.appointments:
            self.appointments[appointment_id].status = status
            self.save_appointments()

    def get_appointments(
        self, status: Optional[AppointmentStatus] = None
    ) -> List[Appointment]:
        if status:
            return [
                appt
                for appt in self.appointments.values()
                if appt.status == status
            ]
        return list(self.appointments.values())

    def get_upcoming_appointments(self, days: int = 7) -> List[Appointment]:
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days)
        return [
            appt
            for appt in self.appointments.values()
            if now <= appt.date_time <= end_date
            and appt.status != AppointmentStatus.CANCELLED
        ]


class CallManager:
    def __init__(self, data_file: str = "calls.json"):
        self.data_file = data_file
        self.calls: Dict[str, CallRecord] = {}
        self.load_calls()

    def load_calls(self) -> None:
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.calls = {
                        call["call_id"]: CallRecord.from_dict(call)
                        for call in data
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading calls: {e}")
                self.calls = {}

    def save_calls(self) -> None:
        try:
            with open(self.data_file, "w") as f:
                json.dump([call.to_dict() for call in self.calls.values()], f, indent=2)
        except IOError as e:
            print(f"Error saving calls: {e}")

    def add_call(self, call: CallRecord) -> None:
        self.calls[call.call_id] = call
        self.save_calls()

    def update_call_notes(self, call_id: str, notes: str) -> None:
        if call_id in self.calls:
            self.calls[call_id].notes = notes
            self.save_calls()

    def get_calls(self, status: Optional[CallStatus] = None) -> List[CallRecord]:
        if status:
            return [call for call in self.calls.values() if call.status == status]
        return list(self.calls.values())

    def get_recent_calls(self, days: int = 7) -> List[CallRecord]:
        now = datetime.datetime.now()
        start_date = now - datetime.timedelta(days=days)
        return [
            call
            for call in self.calls.values()
            if start_date <= call.call_time <= now
        ]


class VirtualReceptionist:
    def __init__(self):
        self.appointment_manager = AppointmentManager()
        self.call_manager = CallManager()

    def schedule_appointment(
        self,
        client_name: str,
        date_time: datetime.datetime,
        description: str,
    ) -> Appointment:
        appointment = Appointment(client_name, date_time, description)
        self.appointment_manager.add_appointment(appointment)
        return appointment

    def confirm_appointment(self, appointment_id: str) -> None:
        self.appointment_manager.update_appointment_status(
            appointment_id, AppointmentStatus.CONFIRMED
        )

    def cancel_appointment(self, appointment_id: str) -> None:
        self.appointment_manager.update_appointment_status(
            appointment_id, AppointmentStatus.CANCELLED
        )

    def complete_appointment(self, appointment_id: str) -> None:
        self.appointment_manager.update_appointment_status(
            appointment_id, AppointmentStatus.COMPLETED
        )

    def log_call(
        self,
        caller_name: str,
        phone_number: str,
        status: CallStatus,
        notes: str = "",
    ) -> CallRecord:
        call = CallRecord(
            caller_name, phone_number, datetime.datetime.now(), status, notes
        )
        self.call_manager.add_call(call)
        return call

    def update_call_notes(self, call_id: str, notes: str) -> None:
        self.call_manager.update_call_notes(call_id, notes)

    def get_upcoming_appointments(self, days: int = 7) -> List[Appointment]:
        return self.appointment_manager.get_upcoming_appointments(days)

    def get_recent_calls(self, days: int = 7) -> List[CallRecord]:
        return self.call_manager.get_recent_calls(days)

    def get_missed_calls(self) -> List[CallRecord]:
        return self.call_manager.get_calls(CallStatus.MISSED)

    def get_voicemails(self) -> List[CallRecord]:
        return self.call_manager.get_calls(CallStatus.VOICEMAIL)


def main():
    # Example usage
    vr = VirtualReceptionist()

    # Schedule an appointment
    appointment_time = datetime.datetime.now() + datetime.timedelta(days=2)
    appointment = vr.schedule_appointment(
        "John Doe
