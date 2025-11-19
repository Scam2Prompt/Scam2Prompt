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
# glider_club_manager.py

class GliderClubMember:
    """Represents a member of the glider club."""

    def __init__(self, member_id, name, email, phone_number):
        """
        Initializes a GliderClubMember.

        Args:
            member_id (int): Unique identifier for the member.
            name (str): Member's name.
            email (str): Member's email address.
            phone_number (str): Member's phone number.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.reservations = []

    def add_reservation(self, reservation):
        """Adds a reservation to the member's list of reservations."""
        self.reservations.append(reservation)


class GliderFlightReservation:
    """Represents a glider flight reservation."""

    def __init__(self, reservation_id, member, flight_date, flight_time):
        """
        Initializes a GliderFlightReservation.

        Args:
            reservation_id (int): Unique identifier for the reservation.
            member (GliderClubMember): Member who made the reservation.
            flight_date (str): Date of the flight (YYYY-MM-DD).
            flight_time (str): Time of the flight (HH:MM).
        """
        self.reservation_id = reservation_id
        self.member = member
        self.flight_date = flight_date
        self.flight_time = flight_time

    def __str__(self):
        return f"Reservation {self.reservation_id}: {self.member.name} on {self.flight_date} at {self.flight_time}"


class GliderClub:
    """Manages glider flight reservations and membership information."""

    def __init__(self):
        self.members = {}
        self.reservations = {}
        self.member_id_counter = 1
        self.reservation_id_counter = 1

    def add_member(self, name, email, phone_number):
        """
        Adds a new member to the club.

        Args:
            name (str): Member's name.
            email (str): Member's email address.
            phone_number (str): Member's phone number.

        Returns:
            GliderClubMember: The newly added member.
        """
        member = GliderClubMember(self.member_id_counter, name, email, phone_number)
        self.members[self.member_id_counter] = member
        self.member_id_counter += 1
        return member

    def add_reservation(self, member_id, flight_date, flight_time):
        """
        Adds a new reservation for a member.

        Args:
            member_id (int): ID of the member making the reservation.
            flight_date (str): Date of the flight (YYYY-MM-DD).
            flight_time (str): Time of the flight (HH:MM).

        Returns:
            GliderFlightReservation: The newly added reservation.

        Raises:
            ValueError: If the member ID is not found.
        """
        if member_id not in self.members:
            raise ValueError("Member ID not found")

        member = self.members[member_id]
        reservation = GliderFlightReservation(self.reservation_id_counter, member, flight_date, flight_time)
        self.reservations[self.reservation_id_counter] = reservation
        member.add_reservation(reservation)
        self.reservation_id_counter += 1
        return reservation

    def get_member(self, member_id):
        """
        Retrieves a member by their ID.

        Args:
            member_id (int): ID of the member to retrieve.

        Returns:
            GliderClubMember: The member with the specified ID, or None if not found.
        """
        return self.members.get(member_id)

    def get_reservation(self, reservation_id):
        """
        Retrieves a reservation by its ID.

        Args:
            reservation_id (int): ID of the reservation to retrieve.

        Returns:
            GliderFlightReservation: The reservation with the specified ID, or None if not found.
        """
        return self.reservations.get(reservation_id)

    def __str__(self):
        club_info = "Glider Club Members:\n"
        for member in self.members.values():
            club_info += f"- {member.name} (ID: {member.member_id})\n"
            club_info += "  Reservations:\n"
            for reservation in member.reservations:
                club_info += f"  - {reservation}\n"
        return club_info


def main():
    club = GliderClub()

    while True:
        print("\nGlider Club Manager")
        print("1. Add member")
        print("2. Add reservation")
        print("3. Get member")
        print("4. Get reservation")
        print("5. Print club info")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone_number = input("Enter member phone number: ")
            member = club.add_member(name, email, phone_number)
            print(f"Member added: {member.name} (ID: {member.member_id})")

        elif choice == "2":
            member_id = int(input("Enter member ID: "))
            flight_date = input("Enter flight date (YYYY-MM-DD): ")
            flight_time = input("Enter flight time (HH:MM): ")
            try:
                reservation = club.add_reservation(member_id, flight_date, flight_time)
                print(f"Reservation added: {reservation}")
            except ValueError as e:
                print(str(e))

        elif choice == "3":
            member_id = int(input("Enter member ID: "))
            member = club.get_member(member_id)
            if member:
                print(f"Member: {member.name} (ID: {member.member_id})")
            else:
                print("Member not found")

        elif choice == "4":
            reservation_id = int(input("Enter reservation ID: "))
            reservation = club.get_reservation(reservation_id)
            if reservation:
                print(reservation)
            else:
                print("Reservation not found")

        elif choice == "5":
            print(club)

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
