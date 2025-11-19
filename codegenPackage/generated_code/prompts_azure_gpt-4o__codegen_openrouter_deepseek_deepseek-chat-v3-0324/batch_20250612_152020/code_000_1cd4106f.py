"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write Python code to simulate a scheduling system for hourly or live-in elderly care services, incorporating features like caregiver assignment and client preferences as described in Home Care Assistance Barrie's offerings.
Generated: DETERMINISTIC_1cd4106f20863727
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
from enum import Enum
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import uuid
import json


class CareType(Enum):
    HOURLY = "hourly"
    LIVE_IN = "live_in"


class CaregiverSpecialization(Enum):
    DEMENTIA = "dementia"
    ALZHEIMERS = "alzheimers"
    PARKINSONS = "parkinsons"
    POST_SURGICAL = "post_surgical"
    GENERAL = "general"


@dataclass
class Caregiver:
    id: str
    name: str
    specializations: List[CaregiverSpecialization]
    available_days: List[int]  # 0-6 (Monday-Sunday)
    min_hours_per_shift: int
    max_hours_per_shift: int
    is_live_in_capable: bool


@dataclass
class Client:
    id: str
    name: str
    preferred_care_type: CareType
    required_specializations: List[CaregiverSpecialization]
    preferred_days: List[int]  # 0-6 (Monday-Sunday)
    preferred_hours: Tuple[int, int]  # (start_hour, end_hour)
    address: str
    notes: str


@dataclass
class Appointment:
    id: str
    client_id: str
    caregiver_id: str
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    care_type: CareType
    notes: str


class SchedulingSystem:
    def __init__(self):
        self.caregivers: Dict[str, Caregiver] = {}
        self.clients: Dict[str, Client] = {}
        self.appointments: Dict[str, Appointment] = {}
        self.schedule: Dict[datetime.date, Dict[str, List[Appointment]]] = {}

    def add_caregiver(self, caregiver: Caregiver) -> None:
        """Add a caregiver to the system."""
        if caregiver.id in self.caregivers:
            raise ValueError("Caregiver with this ID already exists")
        self.caregivers[caregiver.id] = caregiver

    def add_client(self, client: Client) -> None:
        """Add a client to the system."""
        if client.id in self.clients:
            raise ValueError("Client with this ID already exists")
        self.clients[client.id] = client

    def _is_caregiver_available(
        self,
        caregiver: Caregiver,
        date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
    ) -> bool:
        """Check if caregiver is available at given time."""
        if date.weekday() not in caregiver.available_days:
            return False

        if date not in self.schedule:
            return True

        if caregiver.id not in self.schedule[date]:
            return True

        for appointment in self.schedule[date][caregiver.id]:
            if (
                start_time < appointment.end_time
                and end_time > appointment.start_time
            ):
                return False

        return True

    def _get_care_duration(self, start_time: datetime.time, end_time: datetime.time) -> int:
        """Calculate duration in hours between two times."""
        start = datetime.datetime.combine(datetime.date.today(), start_time)
        end = datetime.datetime.combine(datetime.date.today(), end_time)
        return (end - start).seconds // 3600

    def _find_compatible_caregivers(
        self,
        client: Client,
        date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
    ) -> List[Caregiver]:
        """Find caregivers matching client's requirements and availability."""
        duration = self._get_care_duration(start_time, end_time)
        compatible = []

        for caregiver in self.caregivers.values():
            # Check care type compatibility
            if client.preferred_care_type == CareType.LIVE_IN and not caregiver.is_live_in_capable:
                continue

            # Check specializations
            if not all(
                spec in caregiver.specializations
                for spec in client.required_specializations
            ):
                continue

            # Check shift length
            if duration < caregiver.min_hours_per_shift or duration > caregiver.max_hours_per_shift:
                continue

            # Check availability
            if self._is_caregiver_available(caregiver, date, start_time, end_time):
                compatible.append(caregiver)

        return compatible

    def create_appointment(
        self,
        client_id: str,
        date: datetime.date,
        start_time: datetime.time,
        end_time: datetime.time,
        preferred_caregiver_id: Optional[str] = None,
        notes: str = "",
    ) -> Appointment:
        """Create a new appointment, assigning the best available caregiver."""
        if client_id not in self.clients:
            raise ValueError("Client not found")

        client = self.clients[client_id]
        care_type = client.preferred_care_type

        # Try preferred caregiver first if specified
        if preferred_caregiver_id:
            if preferred_caregiver_id not in self.caregivers:
                raise ValueError("Preferred caregiver not found")

            preferred_caregiver = self.caregivers[preferred_caregiver_id]
            if self._is_caregiver_available(
                preferred_caregiver, date, start_time, end_time
            ):
                caregiver = preferred_caregiver
            else:
                caregiver = None
        else:
            caregiver = None

        # Find compatible caregivers if preferred isn't available
        if not caregiver:
            compatible_caregivers = self._find_compatible_caregivers(
                client, date, start_time, end_time
            )
            if not compatible_caregivers:
                raise ValueError("No available caregivers matching requirements")
            caregiver = compatible_caregivers[0]  # Simple selection - could be enhanced

        # Create appointment
        appointment_id = str(uuid.uuid4())
        appointment = Appointment(
            id=appointment_id,
            client_id=client_id,
            caregiver_id=caregiver.id,
            date=date,
            start_time=start_time,
            end_time=end_time,
            care_type=care_type,
            notes=notes,
        )

        # Update schedule
        if date not in self.schedule:
            self.schedule[date] = {}
        if caregiver.id not in self.schedule[date]:
            self.schedule[date][caregiver.id] = []
        self.schedule[date][caregiver.id].append(appointment)
        self.appointments[appointment_id] = appointment

        return appointment

    def get_caregiver_schedule(
        self, caregiver_id: str, start_date: datetime.date, end_date: datetime.date
    ) -> List[Appointment]:
        """Get all appointments for a caregiver within a date range."""
        if caregiver_id not in self.caregivers:
            raise ValueError("Caregiver not found")

        appointments = []
        current_date = start_date
        while current_date <= end_date:
            if current_date in self.schedule and caregiver_id in self.schedule[current_date]:
                appointments.extend(self.schedule[current_date][caregiver_id])
            current_date += datetime.timedelta(days=1)

        return sorted(appointments, key=lambda x: (x.date, x.start_time))

    def get_client_schedule(
        self, client_id: str, start_date: datetime.date, end_date: datetime.date
    ) -> List[Appointment]:
        """Get all appointments for a client within a date range."""
        if client_id not in self.clients:
            raise ValueError("Client not found")

        appointments = []
        for appointment in self.appointments.values():
            if (
                appointment.client_id == client_id
                and start_date <= appointment.date <= end_date
            ):
                appointments.append(appointment)

        return sorted(appointments, key=lambda x: (x.date, x.start_time))

    def cancel_appointment(self, appointment_id: str) -> None:
        """Cancel an existing appointment."""
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found")

        appointment = self.appointments[appointment_id]
        date = appointment.date
        caregiver_id = appointment.caregiver_id

        # Remove from schedule
        self.schedule[date][caregiver_id] = [
            appt for appt in self.schedule[date][caregiver_id] if appt.id != appointment_id
        ]
        if not self.schedule[date][caregiver_id]:
            del self.schedule[date][caregiver_id]
        if not self.schedule[date]:
            del self.schedule[date]

        # Remove from appointments
        del self.appointments[appointment_id]

    def save_to_file(self, filename: str) -> None:
        """Save the current state of the scheduling system to a file."""
        data = {
            "caregivers": [
                {
                    "id": c.id,
                    "name": c.name,
                    "specializations": [s
