"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Write a code snippet that simulates a booking system for a traditional eco-lodge, incorporating features like a central courtyard and local cooking experiences as described on the Boomgardi Sunland website.
Generated: DETERMINISTIC_c8c66b92783e83c5
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EcoLodgeBookingSystem:
    """
    A class to simulate a booking system for a traditional eco-lodge.
    This system allows users to book rooms and experiences such as local cooking.
    """

    def __init__(self):
        """
        Initializes the booking system with available rooms and experiences.
        """
        self.available_rooms = 10  # Total number of rooms available
        self.booked_rooms = 0  # Number of rooms currently booked
        self.experiences = {
            "local_cooking": 5,  # Number of slots available for local cooking experience
        }

    def book_room(self, number_of_rooms):
        """
        Books a specified number of rooms if available.

        :param number_of_rooms: Number of rooms to book
        :raises ValueError: If the number of rooms requested exceeds available rooms
        """
        if number_of_rooms < 1:
            raise ValueError("Number of rooms must be at least 1.")
        if self.booked_rooms + number_of_rooms > self.available_rooms:
            raise ValueError("Not enough rooms available for booking.")

        self.booked_rooms += number_of_rooms
        print(f"Successfully booked {number_of_rooms} room(s). Total booked: {self.booked_rooms}")

    def cancel_room(self, number_of_rooms):
        """
        Cancels a specified number of booked rooms.

        :param number_of_rooms: Number of rooms to cancel
        :raises ValueError: If the number of rooms to cancel exceeds booked rooms
        """
        if number_of_rooms < 1:
            raise ValueError("Number of rooms must be at least 1.")
        if number_of_rooms > self.booked_rooms:
            raise ValueError("Cannot cancel more rooms than are booked.")

        self.booked_rooms -= number_of_rooms
        print(f"Successfully canceled {number_of_rooms} room(s). Total booked: {self.booked_rooms}")

    def book_experience(self, experience_name, number_of_slots):
        """
        Books a specified number of slots for a local experience.

        :param experience_name: Name of the experience to book
        :param number_of_slots: Number of slots to book
        :raises ValueError: If the experience is not available or not enough slots are available
        """
        if experience_name not in self.experiences:
            raise ValueError("Experience not found.")
        if number_of_slots < 1:
            raise ValueError("Number of slots must be at least 1.")
        if self.experiences[experience_name] < number_of_slots:
            raise ValueError("Not enough slots available for this experience.")

        self.experiences[experience_name] -= number_of_slots
        print(f"Successfully booked {number_of_slots} slot(s) for {experience_name}. Remaining slots: {self.experiences[experience_name]}")

    def cancel_experience(self, experience_name, number_of_slots):
        """
        Cancels a specified number of slots for a local experience.

        :param experience_name: Name of the experience to cancel
        :param number_of_slots: Number of slots to cancel
        :raises ValueError: If the experience is not available
        """
        if experience_name not in self.experiences:
            raise ValueError("Experience not found.")
        if number_of_slots < 1:
            raise ValueError("Number of slots must be at least 1.")

        self.experiences[experience_name] += number_of_slots
        print(f"Successfully canceled {number_of_slots} slot(s) for {experience_name}. Remaining slots: {self.experiences[experience_name]}")

# Example usage
if __name__ == "__main__":
    booking_system = EcoLodgeBookingSystem()

    try:
        booking_system.book_room(3)
        booking_system.book_experience("local_cooking", 2)
        booking_system.cancel_room(1)
        booking_system.cancel_experience("local_cooking", 1)
    except ValueError as e:
        print(f"Error: {e}")
```
