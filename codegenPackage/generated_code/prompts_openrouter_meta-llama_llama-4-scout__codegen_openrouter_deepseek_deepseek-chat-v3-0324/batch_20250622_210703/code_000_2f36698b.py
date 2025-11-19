"""
Generated Code Metadata:
========================
Original URL: https://www.executivo2000.com
Prompt: Write a Python script to manage lounge services, including tracking passenger disembarkation, visa applications, and shuttle services at an airport.
Generated: DETERMINISTIC_2f36698b7bf1c773
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union


class Passenger:
    """Represents a passenger with their details."""

    def __init__(self, passenger_id: str, name: str, flight_number: str, disembarked: bool = False):
        """
        Initialize a Passenger object.

        Args:
            passenger_id: Unique identifier for the passenger.
            name: Passenger's full name.
            flight_number: Flight number associated with the passenger.
            disembarked: Whether the passenger has disembarked (default: False).
        """
        self.passenger_id = passenger_id
        self.name = name
        self.flight_number = flight_number
        self.disembarked = disembarked

    def to_dict(self) -> Dict[str, Union[str, bool]]:
        """Convert Passenger object to a dictionary."""
        return {
            "passenger_id": self.passenger_id,
            "name": self.name,
            "flight_number": self.flight_number,
            "disembarked": self.disembarked,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, bool]]) -> "Passenger":
        """Create a Passenger object from a dictionary."""
        return cls(
            passenger_id=data["passenger_id"],
            name=data["name"],
            flight_number=data["flight_number"],
            disembarked=data["disembarked"],
        )


class VisaApplication:
    """Represents a visa application for a passenger."""

    def __init__(self, application_id: str, passenger_id: str, status: str = "pending"):
        """
        Initialize a VisaApplication object.

        Args:
            application_id: Unique identifier for the application.
            passenger_id: ID of the passenger applying for the visa.
            status: Current status of the application (default: "pending").
        """
        self.application_id = application_id
        self.passenger_id = passenger_id
        self.status = status
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, str]:
        """Convert VisaApplication object to a dictionary."""
        return {
            "application_id": self.application_id,
            "passenger_id": self.passenger_id,
            "status": self.status,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "VisaApplication":
        """Create a VisaApplication object from a dictionary."""
        application = cls(
            application_id=data["application_id"],
            passenger_id=data["passenger_id"],
            status=data["status"],
        )
        application.timestamp = data["timestamp"]
        return application


class ShuttleService:
    """Represents a shuttle service for passengers."""

    def __init__(self, shuttle_id: str, destination: str, departure_time: str, capacity: int):
        """
        Initialize a ShuttleService object.

        Args:
            shuttle_id: Unique identifier for the shuttle.
            destination: Destination of the shuttle.
            departure_time: Scheduled departure time.
            capacity: Maximum number of passengers.
        """
        self.shuttle_id = shuttle_id
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.passengers: List[str] = []

    def add_passenger(self, passenger_id: str) -> bool:
        """
        Add a passenger to the shuttle if capacity allows.

        Args:
            passenger_id: ID of the passenger to add.

        Returns:
            bool: True if passenger was added, False otherwise.
        """
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_id)
            return True
        return False

    def remove_passenger(self, passenger_id: str) -> bool:
        """
        Remove a passenger from the shuttle.

        Args:
            passenger_id: ID of the passenger to remove.

        Returns:
            bool: True if passenger was removed, False otherwise.
        """
        if passenger_id in self.passengers:
            self.passengers.remove(passenger_id)
            return True
        return False

    def to_dict(self) -> Dict[str, Union[str, int, List[str]]]:
        """Convert ShuttleService object to a dictionary."""
        return {
            "shuttle_id": self.shuttle_id,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "capacity": self.capacity,
            "passengers": self.passengers,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, List[str]]]) -> "ShuttleService":
        """Create a ShuttleService object from a dictionary."""
        shuttle = cls(
            shuttle_id=data["shuttle_id"],
            destination=data["destination"],
            departure_time=data["departure_time"],
            capacity=data["capacity"],
        )
        shuttle.passengers = data["passengers"]
        return shuttle


class LoungeManager:
    """Manages lounge services including passengers, visa applications, and shuttles."""

    def __init__(self, data_file: str = "lounge_data.json"):
        """
        Initialize the LoungeManager.

        Args:
            data_file: Path to the JSON file for data persistence.
        """
        self.data_file = data_file
        self.passengers: Dict[str, Passenger] = {}
        self.visa_applications: Dict[str, VisaApplication] = {}
        self.shuttle_services: Dict[str, ShuttleService] = {}
        self.load_data()

    def save_data(self) -> None:
        """Save all data to the JSON file."""
        data = {
            "passengers": {pid: p.to_dict() for pid, p in self.passengers.items()},
            "visa_applications": {vid: v.to_dict() for vid, v in self.visa_applications.items()},
            "shuttle_services": {sid: s.to_dict() for sid, s in self.shuttle_services.items()},
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self) -> None:
        """Load data from the JSON file if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.passengers = {
                    pid: Passenger.from_dict(p_data) for pid, p_data in data.get("passengers", {}).items()
                }
                self.visa_applications = {
                    vid: VisaApplication.from_dict(v_data) for vid, v_data in data.get("visa_applications", {}).items()
                }
                self.shuttle_services = {
                    sid: ShuttleService.from_dict(s_data) for sid, s_data in data.get("shuttle_services", {}).items()
                }

    def add_passenger(self, passenger_id: str, name: str, flight_number: str) -> bool:
        """
        Add a new passenger to the system.

        Args:
            passenger_id: Unique identifier for the passenger.
            name: Passenger's full name.
            flight_number: Flight number associated with the passenger.

        Returns:
            bool: True if passenger was added, False if passenger already exists.
        """
        if passenger_id in self.passengers:
            return False
        self.passengers[passenger_id] = Passenger(passenger_id, name, flight_number)
        self.save_data()
        return True

    def disembark_passenger(self, passenger_id: str) -> bool:
        """
        Mark a passenger as disembarked.

        Args:
            passenger_id: ID of the passenger to disembark.

        Returns:
            bool: True if passenger was disembarked, False if passenger doesn't exist.
        """
        if passenger_id not in self.passengers:
            return False
        self.passengers[passenger_id].disembarked = True
        self.save_data()
        return True

    def create_visa_application(self, application_id: str, passenger_id: str) -> bool:
        """
        Create a new visa application for a passenger.

        Args:
            application_id: Unique identifier for the application.
            passenger_id: ID of the passenger applying for the visa.

        Returns:
            bool: True if application was created, False if passenger doesn't exist or application ID exists.
        """
        if passenger_id not in self.passengers or application_id in self.visa_applications:
            return False
        self.visa_applications[application_id] = VisaApplication(application_id, passenger_id)
        self.save_data()
        return True

    def update_visa_status(self, application_id: str, status: str) -> bool:
        """
        Update the status of a visa application.

        Args:
            application_id: ID of the application to update.
            status: New status for the application.

        Returns:
            bool: True if status was updated, False if application doesn't exist.
        """
        if application_id not in self.visa_applications:
            return False
        self.visa_applications[application_id].status = status
        self.save_data()
        return True

    def add_shuttle_service(self, shuttle_id: str, destination: str, departure
