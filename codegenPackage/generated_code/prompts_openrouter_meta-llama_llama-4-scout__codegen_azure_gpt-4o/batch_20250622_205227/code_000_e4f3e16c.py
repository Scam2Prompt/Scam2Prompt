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
import datetime


class Member:
    """
    Represents a club member.
    Attributes:
        member_id (int): Unique ID for the member.
        name (str): Name of the member.
        email (str): Email address of the member.
        membership_expiry (datetime.date): Membership expiry date.
    """

    def __init__(self, member_id, name, email, membership_expiry):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.membership_expiry = membership_expiry

    def is_membership_active(self):
        """
        Checks if the membership is active.
        Returns:
            bool: True if membership is active, False otherwise.
        """
        return self.membership_expiry >= datetime.date.today()


class Reservation:
    """
    Represents a glider flight reservation.
    Attributes:
        reservation_id (int): Unique ID for the reservation.
        member (Member): Member who made the reservation.
        flight_date (datetime.date): Date of the flight.
    """

    def __init__(self, reservation_id, member, flight_date):
        self.reservation_id = reservation_id
        self.member = member
        self.flight_date = flight_date

    def is_valid_reservation(self):
        """
        Checks if the reservation is valid.
        Returns:
            bool: True if the reservation is valid, False otherwise.
        """
        return self.member.is_membership_active() and self.flight_date >= datetime.date.today()


class GliderClub:
    """
    Manages members and reservations for the glider club.
    Attributes:
        members (dict): Dictionary of members (key: member_id, value: Member object).
        reservations (dict): Dictionary of reservations (key: reservation_id, value: Reservation object).
    """

    def __init__(self):
        self.members = {}
        self.reservations = {}

    def add_member(self, member_id, name, email, membership_expiry):
        """
        Adds a new member to the club.
        Args:
            member_id (int): Unique ID for the member.
            name (str): Name of the member.
            email (str): Email address of the member.
            membership_expiry (datetime.date): Membership expiry date.
        """
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        self.members[member_id] = Member(member_id, name, email, membership_expiry)

    def add_reservation(self, reservation_id, member_id, flight_date):
        """
        Adds a new reservation for a glider flight.
        Args:
            reservation_id (int): Unique ID for the reservation.
            member_id (int): ID of the member making the reservation.
            flight_date (datetime.date): Date of the flight.
        """
        if reservation_id in self.reservations:
            raise ValueError(f"Reservation ID {reservation_id} already exists.")
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} does not exist.")
        member = self.members[member_id]
        reservation = Reservation(reservation_id, member, flight_date)
        if not reservation.is_valid_reservation():
            raise ValueError("Invalid reservation: Membership must be active and flight date must be in the future.")
        self.reservations[reservation_id] = reservation

    def get_member_info(self, member_id):
        """
        Retrieves information about a member.
        Args:
            member_id (int): ID of the member.
        Returns:
            dict: Member information.
        """
        if member_id not in self.members:
            raise ValueError(f"Member ID {member_id} does not exist.")
        member = self.members[member_id]
        return {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "membership_expiry": member.membership_expiry,
            "membership_active": member.is_membership_active(),
        }

    def get_reservation_info(self, reservation_id):
        """
        Retrieves information about a reservation.
        Args:
            reservation_id (int): ID of the reservation.
        Returns:
            dict: Reservation information.
        """
        if reservation_id not in self.reservations:
            raise ValueError(f"Reservation ID {reservation_id} does not exist.")
        reservation = self.reservations[reservation_id]
        return {
            "reservation_id": reservation.reservation_id,
            "member_id": reservation.member.member_id,
            "flight_date": reservation.flight_date,
            "valid_reservation": reservation.is_valid_reservation(),
        }


# Example usage
if __name__ == "__main__":
    try:
        club = GliderClub()

        # Add members
        club.add_member(1, "Alice Smith", "alice@example.com", datetime.date(2024, 5, 1))
        club.add_member(2, "Bob Johnson", "bob@example.com", datetime.date(2023, 12, 31))

        # Add reservations
        club.add_reservation(101, 1, datetime.date(2023, 11, 15))
        club.add_reservation(102, 2, datetime.date(2023, 11, 20))

        # Retrieve member info
        print(club.get_member_info(1))
        print(club.get_member_info(2))

        # Retrieve reservation info
        print(club.get_reservation_info(101))
        print(club.get_reservation_info(102))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
