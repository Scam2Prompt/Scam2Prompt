"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Write a Python script to manage glider flight reservations and membership information for a club like AAVE.
Generated: DETERMINISTIC_e4f3e16c2223e516
Batch ID: 20250622_205227
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

# Constants
DATA_FILE = "glider_club_data.json"
DATE_FORMAT = "%Y-%m-%d"

class GliderClubManager:
    """
    A class to manage glider flight reservations and membership information for a club.
    """

    def __init__(self):
        """
        Initialize the GliderClubManager and load existing data from file.
        """
        self.data = {
            "members": {},
            "gliders": {},
            "reservations": []
        }
        self._load_data()

    def _load_data(self) -> None:
        """
        Load data from the JSON file if it exists.
        """
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                self.data = json.load(file)

    def _save_data(self) -> None:
        """
        Save the current data to the JSON file.
        """
        with open(DATA_FILE, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_member(self, member_id: str, name: str, email: str, join_date: str) -> bool:
        """
        Add a new member to the club.

        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Email address of the member
            join_date: Date when the member joined (YYYY-MM-DD)

        Returns:
            bool: True if member was added successfully, False if member already exists
        """
        if member_id in self.data["members"]:
            return False

        try:
            datetime.strptime(join_date, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.data["members"][member_id] = {
            "name": name,
            "email": email,
            "join_date": join_date,
            "is_active": True
        }
        self._save_data()
        return True

    def update_member(self, member_id: str, **kwargs) -> bool:
        """
        Update member information.

        Args:
            member_id: ID of the member to update
            **kwargs: Fields to update (name, email, is_active)

        Returns:
            bool: True if update was successful, False if member doesn't exist
        """
        if member_id not in self.data["members"]:
            return False

        member = self.data["members"][member_id]
        for key, value in kwargs.items():
            if key in member:
                if key == "join_date":
                    try:
                        datetime.strptime(value, DATE_FORMAT)
                    except ValueError:
                        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
                member[key] = value

        self._save_data()
        return True

    def add_glider(self, glider_id: str, model: str, capacity: int, maintenance_due: str) -> bool:
        """
        Add a new glider to the club's inventory.

        Args:
            glider_id: Unique identifier for the glider
            model: Model name of the glider
            capacity: Number of passengers
            maintenance_due: Next maintenance date (YYYY-MM-DD)

        Returns:
            bool: True if glider was added successfully, False if glider already exists
        """
        if glider_id in self.data["gliders"]:
            return False

        try:
            datetime.strptime(maintenance_due, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.data["gliders"][glider_id] = {
            "model": model,
            "capacity": capacity,
            "maintenance_due": maintenance_due,
            "is_available": True
        }
        self._save_data()
        return True

    def update_glider(self, glider_id: str, **kwargs) -> bool:
        """
        Update glider information.

        Args:
            glider_id: ID of the glider to update
            **kwargs: Fields to update (model, capacity, maintenance_due, is_available)

        Returns:
            bool: True if update was successful, False if glider doesn't exist
        """
        if glider_id not in self.data["gliders"]:
            return False

        glider = self.data["gliders"][glider_id]
        for key, value in kwargs.items():
            if key in glider:
                if key == "maintenance_due":
                    try:
                        datetime.strptime(value, DATE_FORMAT)
                    except ValueError:
                        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
                glider[key] = value

        self._save_data()
        return True

    def make_reservation(self, member_id: str, glider_id: str, date: str) -> bool:
        """
        Make a flight reservation.

        Args:
            member_id: ID of the member making the reservation
            glider_id: ID of the glider to reserve
            date: Date of the reservation (YYYY-MM-DD)

        Returns:
            bool: True if reservation was successful, False if not
        """
        try:
            datetime.strptime(date, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if member_id not in self.data["members"]:
            raise ValueError("Member does not exist.")

        if glider_id not in self.data["gliders"]:
            raise ValueError("Glider does not exist.")

        if not self.data["members"][member_id]["is_active"]:
            raise ValueError("Member is not active.")

        if not self.data["gliders"][glider_id]["is_available"]:
            raise ValueError("Glider is not available.")

        # Check if glider is already reserved for this date
        for reservation in self.data["reservations"]:
            if reservation["glider_id"] == glider_id and reservation["date"] == date:
                raise ValueError("Glider already reserved for this date.")

        self.data["reservations"].append({
            "member_id": member_id,
            "glider_id": glider_id,
            "date": date,
            "status": "confirmed"
        })
        self._save_data()
        return True

    def cancel_reservation(self, member_id: str, glider_id: str, date: str) -> bool:
        """
        Cancel an existing reservation.

        Args:
            member_id: ID of the member who made the reservation
            glider_id: ID of the reserved glider
            date: Date of the reservation (YYYY-MM-DD)

        Returns:
            bool: True if cancellation was successful, False if reservation wasn't found
        """
        for i, reservation in enumerate(self.data["reservations"]):
            if (reservation["member_id"] == member_id and
                reservation["glider_id"] == glider_id and
                reservation["date"] == date):
                del self.data["reservations"][i]
                self._save_data()
                return True
        return False

    def get_member_reservations(self, member_id: str) -> List[Dict]:
        """
        Get all reservations for a specific member.

        Args:
            member_id: ID of the member

        Returns:
            List[Dict]: List of reservation dictionaries
        """
        return [r for r in self.data["reservations"] if r["member_id"] == member_id]

    def get_glider_schedule(self, glider_id: str) -> List[Dict]:
        """
        Get all reservations for a specific glider.

        Args:
            glider_id: ID of the glider

        Returns:
            List[Dict]: List of reservation dictionaries
        """
        return [r for r in self.data["reservations"] if r["glider_id"] == glider_id]

    def get_daily_schedule(self, date: str) -> List[Dict]:
        """
        Get all reservations for a specific date.

        Args:
            date: Date to check (YYYY-MM-DD)

        Returns:
            List[Dict]: List of reservation dictionaries
        """
        try:
            datetime.strptime(date, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        return [r for r in self.data["reservations"] if r["date"] == date]

    def check_glider_availability(self, glider_id: str, date: str) -> bool:
        """
        Check if a glider is available on a specific date.

        Args:
            glider_id: ID of the glider to check
            date: Date to check (YYYY-MM-DD)

        Returns:
            bool: True if available, False if not
        """
        if glider_id not in self.data["gliders"]:
            raise ValueError("Glider does not exist.")

        if not self.data["gliders"][glider_id]["is_available"]:
            return False

        for reservation in self.data["reservations"]:
            if reservation["glider_id"] == glider_id and reservation["date"] == date:
