"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Generate code for a scheduling system that accommodates OSI-type programming for psychiatry and coaching across multiple time zones.
Generated: DETERMINISTIC_eb8b24803b136b93
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import pytz
from typing import List, Dict, Optional
from enum import Enum, auto
from dataclasses import dataclass
import uuid
import json
from abc import ABC, abstractmethod


class SessionType(Enum):
    PSYCHIATRY = auto()
    COACHING = auto()


class AvailabilityStatus(Enum):
    AVAILABLE = auto()
    BOOKED = auto()
    UNAVAILABLE = auto()


@dataclass
class TimeSlot:
    start_time: datetime.datetime
    end_time: datetime.datetime
    status: AvailabilityStatus = AvailabilityStatus.AVAILABLE
    session_type: Optional[SessionType] = None
    timezone: str = "UTC"

    def to_dict(self) -> Dict:
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "status": self.status.name,
            "session_type": self.session_type.name if self.session_type else None,
            "timezone": self.timezone
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TimeSlot':
        return cls(
            start_time=datetime.datetime.fromisoformat(data["start_time"]),
            end_time=datetime.datetime.fromisoformat(data["end_time"]),
            status=AvailabilityStatus[data["status"]],
            session_type=SessionType[data["session_type"]] if data["session_type"] else None,
            timezone=data["timezone"]
        )


class User(ABC):
    def __init__(self, user_id: str, name: str, email: str, timezone: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.timezone = timezone
        self.availability: List[TimeSlot] = []

    def add_availability(self, time_slot: TimeSlot) -> None:
        """Add a time slot to the user's availability."""
        self.availability.append(time_slot)

    def get_availability(self) -> List[TimeSlot]:
        """Get all availability slots."""
        return self.availability

    def convert_timezone(self, time_slot: TimeSlot, target_timezone: str) -> TimeSlot:
        """Convert a time slot to a different timezone."""
        source_tz = pytz.timezone(time_slot.timezone)
        target_tz = pytz.timezone(target_timezone)
        
        start_time = source_tz.localize(time_slot.start_time).astimezone(target_tz)
        end_time = source_tz.localize(time_slot.end_time).astimezone(target_tz)
        
        return TimeSlot(
            start_time=start_time.replace(tzinfo=None),
            end_time=end_time.replace(tzinfo=None),
            status=time_slot.status,
            session_type=time_slot.session_type,
            timezone=target_timezone
        )

    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "timezone": self.timezone,
            "availability": [slot.to_dict() for slot in self.availability]
        }

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict) -> 'User':
        pass


class Provider(User):
    def __init__(self, user_id: str, name: str, email: str, timezone: str, specialties: List[SessionType]):
        super().__init__(user_id, name, email, timezone)
        self.specialties = specialties

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data["specialties"] = [specialty.name for specialty in self.specialties]
        return data

    @classmethod
    def from_dict(cls, data: Dict) -> 'Provider':
        specialties = [SessionType[specialty] for specialty in data["specialties"]]
        provider = cls(
            user_id=data["user_id"],
            name=data["name"],
            email=data["email"],
            timezone=data["timezone"],
            specialties=specialties
        )
        provider.availability = [TimeSlot.from_dict(slot) for slot in data["availability"]]
        return provider


class Client(User):
    def __init__(self, user_id: str, name: str, email: str, timezone: str):
        super().__init__(user_id, name, email, timezone)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Client':
        client = cls(
            user_id=data["user_id"],
            name=data["name"],
            email=data["email"],
            timezone=data["timezone"]
        )
        client.availability = [TimeSlot.from_dict(slot) for slot in data["availability"]]
        return client


class Appointment:
    def __init__(self, appointment_id: str, provider: Provider, client: Client, time_slot: TimeSlot):
        self.appointment_id = appointment_id
        self.provider = provider
        self.client = client
        self.time_slot = time_slot
        self.created_at = datetime.datetime.utcnow()

    def to_dict(self) -> Dict:
        return {
            "appointment_id": self.appointment_id,
            "provider": self.provider.to_dict(),
            "client": self.client.to_dict(),
            "time_slot": self.time_slot.to_dict(),
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Appointment':
        provider = Provider.from_dict(data["provider"])
        client = Client.from_dict(data["client"])
        time_slot = TimeSlot.from_dict(data["time_slot"])
        return cls(
            appointment_id=data["appointment_id"],
            provider=provider,
            client=client,
            time_slot=time_slot
        )


class SchedulingSystem:
    def __init__(self):
        self.providers: Dict[str, Provider] = {}
        self.clients: Dict[str, Client] = {}
        self.appointments: Dict[str, Appointment] = {}

    def add_provider(self, provider: Provider) -> None:
        """Add a provider to the system."""
        self.providers[provider.user_id] = provider

    def add_client(self, client: Client) -> None:
        """Add a client to the system."""
        self.clients[client.user_id] = client

    def book_appointment(self, provider_id: str, client_id: str, time_slot: TimeSlot) -> Optional[Appointment]:
        """Book an appointment between a provider and client."""
        if provider_id not in self.providers or client_id not in self.clients:
            return None

        provider = self.providers[provider_id]
        client = self.clients[client_id]

        # Check if time slot is available
        for slot in provider.availability:
            if (slot.start_time == time_slot.start_time and 
                slot.end_time == time_slot.end_time and 
                slot.status == AvailabilityStatus.AVAILABLE):
                
                # Mark slot as booked
                slot.status = AvailabilityStatus.BOOKED
                appointment_id = str(uuid.uuid4())
                appointment = Appointment(appointment_id, provider, client, time_slot)
                self.appointments[appointment_id] = appointment
                return appointment

        return None

    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an appointment and free up the time slot."""
        if appointment_id not in self.appointments:
            return False

        appointment = self.appointments[appointment_id]
        provider = appointment.provider

        # Find and free the time slot
        for slot in provider.availability:
            if (slot.start_time == appointment.time_slot.start_time and 
                slot.end_time == appointment.time_slot.end_time):
                slot.status = AvailabilityStatus.AVAILABLE
                break

        del self.appointments[appointment_id]
        return True

    def get_provider_availability(self, provider_id: str, target_timezone: str = "UTC") -> List[TimeSlot]:
        """Get a provider's availability in a specific timezone."""
        if provider_id not in self.providers:
            return []

        provider = self.providers[provider_id]
        converted_slots = []
        for slot in provider.availability:
            converted_slots.append(provider.convert_timezone(slot, target_timezone))
        return converted_slots

    def save_to_file(self, filename: str) -> bool:
        """Save the scheduling system state to a file."""
        try:
            data = {
                "providers": [provider.to_dict() for provider in self.providers.values()],
                "clients": [client.to_dict() for client in self.clients.values()],
                "appointments": [appointment.to_dict() for appointment in self.appointments.values()]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load the scheduling system state from a file."""
        try:
            with
