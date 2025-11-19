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
from typing import List, Dict, Optional

class Member:
    """Class to represent a club member."""
    
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict:
        """Convert member information to a dictionary."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email
        }

class Reservation:
    """Class to represent a flight reservation."""
    
    def __init__(self, reservation_id: int, member_id: int, flight_date: str):
        self.reservation_id = reservation_id
        self.member_id = member_id
        self.flight_date = flight_date

    def to_dict(self) -> Dict:
        """Convert reservation information to a dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "member_id": self.member_id,
            "flight_date": self.flight_date
        }

class Club:
    """Class to manage members and reservations."""
    
    def __init__(self):
        self.members: List[Member] = []
        self.reservations: List[Reservation] = []

    def add_member(self, name: str, email: str) -> Member:
        """Add a new member to the club."""
        member_id = len(self.members) + 1
        new_member = Member(member_id, name, email)
        self.members.append(new_member)
        return new_member

    def remove_member(self, member_id: int) -> bool:
        """Remove a member from the club."""
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return True
        return False

    def make_reservation(self, member_id: int, flight_date: str) -> Reservation:
        """Create a flight reservation for a member."""
        reservation_id = len(self.reservations) + 1
        new_reservation = Reservation(reservation_id, member_id, flight_date)
        self.reservations.append(new_reservation)
        return new_reservation

    def cancel_reservation(self, reservation_id: int) -> bool:
        """Cancel a flight reservation."""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                self.reservations.remove(reservation)
                return True
        return False

    def save_data(self, filename: str) -> None:
        """Save members and reservations to a JSON file."""
        data = {
            "members": [member.to_dict() for member in self.members],
            "reservations": [reservation.to_dict() for reservation in self.reservations]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename: str) -> None:
        """Load members and reservations from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.members = [Member(**member) for member in data.get("members", [])]
                self.reservations = [Reservation(**reservation) for reservation in data.get("reservations", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

if __name__ == "__main__":
    club = Club()
    club.load_data("club_data.json")  # Load existing data if available

    # Example usage
    member = club.add_member("John Doe", "john@example.com")
    reservation = club.make_reservation(member.member_id, "2023-10-15")
    
    # Save data after modifications
    club.save_data("club_data.json")
```
