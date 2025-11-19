"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Create a Python program to schedule and manage consultations for immigration law services, including support for Skype, phone, and in-person appointments.
Generated: DETERMINISTIC_042f32ce49be3dcf
Batch ID: 20250612_152924
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
from enum import Enum
from typing import Dict, List, Optional, Tuple


class ConsultationType(Enum):
    """Enumeration for consultation types."""
    SKYPE = "Skype"
    PHONE = "Phone"
    IN_PERSON = "In-Person"


class ConsultationStatus(Enum):
    """Enumeration for consultation statuses."""
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    RESCHEDULED = "Rescheduled"


class Consultation:
    """Class representing a consultation appointment."""

    def __init__(
        self,
        client_name: str,
        contact_info: str,
        consultation_type: ConsultationType,
        date_time: datetime.datetime,
        duration: int,
        notes: str = "",
    ):
        """Initialize a consultation instance.

        Args:
            client_name: Name of the client.
            contact_info: Contact information (email/phone).
            consultation_type: Type of consultation.
            date_time: Date and time of the consultation.
            duration: Duration in minutes.
            notes: Additional notes (default: "").
        """
        self.client_name = client_name
        self.contact_info = contact_info
        self.consultation_type = consultation_type
        self.date_time = date_time
        self.duration = duration
        self.notes = notes
        self.status = ConsultationStatus.SCHEDULED
        self.id = self._generate_id()

    def _generate_id(self) -> str:
        """Generate a unique ID for the consultation."""
        timestamp = int(self.date_time.timestamp())
        return f"CONS-{timestamp}-{hash(self.client_name)}"

    def to_dict(self) -> Dict:
        """Convert consultation to dictionary for serialization."""
        return {
            "id": self.id,
            "client_name": self.client_name,
            "contact_info": self.contact_info,
            "consultation_type": self.consultation_type.value,
            "date_time": self.date_time.isoformat(),
            "duration": self.duration,
            "notes": self.notes,
            "status": self.status.value,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Consultation":
        """Create a Consultation instance from a dictionary."""
        consultation = cls(
            client_name=data["client_name"],
            contact_info=data["contact_info"],
            consultation_type=ConsultationType(data["consultation_type"]),
            date_time=datetime.datetime.fromisoformat(data["date_time"]),
            duration=data["duration"],
            notes=data.get("notes", ""),
        )
        consultation.status = ConsultationStatus(data["status"])
        consultation.id = data["id"]
        return consultation


class ConsultationScheduler:
    """Class to manage consultation scheduling."""

    def __init__(self, storage_file: str = "consultations.json"):
        """Initialize the scheduler with storage file."""
        self.storage_file = storage_file
        self.consultations: Dict[str, Consultation] = {}
        self._load_consultations()

    def _load_consultations(self) -> None:
        """Load consultations from storage file."""
        if not os.path.exists(self.storage_file):
            return

        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                for consultation_data in data:
                    consultation = Consultation.from_dict(consultation_data)
                    self.consultations[consultation.id] = consultation
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load consultations: {e}")

    def _save_consultations(self) -> None:
        """Save consultations to storage file."""
        try:
            with open(self.storage_file, "w") as f:
                consultations_data = [
                    consultation.to_dict()
                    for consultation in self.consultations.values()
                ]
                json.dump(consultations_data, f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save consultations: {e}")

    def schedule_consultation(
        self,
        client_name: str,
        contact_info: str,
        consultation_type: ConsultationType,
        date_time: datetime.datetime,
        duration: int,
        notes: str = "",
    ) -> Consultation:
        """Schedule a new consultation.

        Args:
            client_name: Name of the client.
            contact_info: Contact information.
            consultation_type: Type of consultation.
            date_time: Date and time of the consultation.
            duration: Duration in minutes.
            notes: Additional notes.

        Returns:
            The scheduled consultation.

        Raises:
            ValueError: If the date is in the past or duration is invalid.
            RuntimeError: If there's a scheduling conflict.
        """
        if date_time < datetime.datetime.now():
            raise ValueError("Cannot schedule consultation in the past.")
        if duration <= 0:
            raise ValueError("Duration must be positive.")

        # Check for conflicts
        end_time = date_time + datetime.timedelta(minutes=duration)
        for consultation in self.consultations.values():
            if consultation.status == ConsultationStatus.CANCELLED:
                continue

            existing_end = consultation.date_time + datetime.timedelta(
                minutes=consultation.duration
            )
            if (
                date_time < existing_end
                and end_time > consultation.date_time
            ):
                raise RuntimeError(
                    "Scheduling conflict with existing consultation."
                )

        consultation = Consultation(
            client_name=client_name,
            contact_info=contact_info,
            consultation_type=consultation_type,
            date_time=date_time,
            duration=duration,
            notes=notes,
        )
        self.consultations[consultation.id] = consultation
        self._save_consultations()
        return consultation

    def get_consultation(self, consultation_id: str) -> Optional[Consultation]:
        """Get a consultation by ID.

        Args:
            consultation_id: ID of the consultation.

        Returns:
            The consultation if found, None otherwise.
        """
        return self.consultations.get(consultation_id)

    def get_all_consultations(self) -> List[Consultation]:
        """Get all consultations.

        Returns:
            List of all consultations.
        """
        return list(self.consultations.values())

    def get_upcoming_consultations(
        self, days_ahead: int = 7
    ) -> List[Consultation]:
        """Get upcoming consultations within the specified days.

        Args:
            days_ahead: Number of days to look ahead (default: 7).

        Returns:
            List of upcoming consultations.
        """
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days_ahead)
        return [
            consultation
            for consultation in self.consultations.values()
            if now <= consultation.date_time <= end_date
            and consultation.status == ConsultationStatus.SCHEDULED
        ]

    def update_consultation(
        self,
        consultation_id: str,
        date_time: Optional[datetime.datetime] = None,
        duration: Optional[int] = None,
        notes: Optional[str] = None,
        status: Optional[ConsultationStatus] = None,
    ) -> Consultation:
        """Update a consultation.

        Args:
            consultation_id: ID of the consultation to update.
            date_time: New date and time (optional).
            duration: New duration (optional).
            notes: New notes (optional).
            status: New status (optional).

        Returns:
            The updated consultation.

        Raises:
            ValueError: If consultation not found or invalid update.
        """
        consultation = self.consultations.get(consultation_id)
        if not consultation:
            raise ValueError("Consultation not found.")

        if date_time is not None:
            if date_time < datetime.datetime.now():
                raise ValueError("Cannot reschedule to past date.")
            consultation.date_time = date_time

        if duration is not None:
            if duration <= 0:
                raise ValueError("Duration must be positive.")
            consultation.duration = duration

        if notes is not None:
            consultation.notes = notes

        if status is not None:
            consultation.status = status

        self._save_consultations()
        return consultation

    def cancel_consultation(self, consultation_id: str) -> Consultation:
        """Cancel a consultation.

        Args:
            consultation_id: ID of the consultation to cancel.

        Returns:
            The cancelled consultation.

        Raises:
            ValueError: If consultation not found.
        """
        consultation = self.consultations.get(consultation_id)
        if not consultation:
            raise ValueError("Consultation not found.")

        consultation.status = ConsultationStatus.CANCELLED
        self._save_consultations()
        return consultation

    def reschedule_consultation(
        self,
        consultation_id: str,
        new_date_time: datetime.datetime,
        new_duration: Optional[int] = None,
    ) -> Consultation:
        """Reschedule a consultation.

        Args:
            consultation_id: ID of the consultation to reschedule.
            new_date_time: New date and time.
            new_duration: New duration (optional).

        Returns:
            The rescheduled consultation.

        Raises:
            ValueError: If consultation not found or invalid reschedule.
        """
        consultation = self.consultations.get(consultation_id)
        if not consultation:
            raise ValueError("Consultation not found.")

        if new_date_time
