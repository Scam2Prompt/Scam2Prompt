"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Write a code snippet that simulates a booking system for a traditional eco-lodge, incorporating features like a central courtyard and local cooking experiences as described on the Boomgardi Sunland website.
Generated: DETERMINISTIC_c8c66b92783e83c5
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EcoLodgeBookingSystem:
    """
    A simple booking system for an eco-lodge, featuring a central courtyard
    and local cooking experiences. The system allows users to book rooms and 
    schedule cooking experiences.
    """

    def __init__(self):
        # Initialize the booking system with available rooms and cooking experiences
        self.rooms = {
            "Room 101": {"available": True, "price": 100},
            "Room 102": {"available": True, "price": 120},
            "Room 103": {"available": True, "price": 150},
        }
        self.cooking_experiences = {
            "Traditional Cooking Class": {"available": True, "price": 50},
            "Farm-to-Table Experience": {"available": True, "price": 70},
        }
        self.bookings = []

    def book_room(self, room_name):
        """
        Book a room if it's available.

        :param room_name: Name of the room to be booked
        :return: Confirmation message or error message
        """
        try:
            room = self.rooms[room_name]
            if room['available']:
                room['available'] = False
                self.bookings.append(room_name)
                return f"{room_name} has been successfully booked."
            else:
                return f"Sorry, {room_name} is not available."
        except KeyError:
            return f"Error: {room_name} does not exist."

    def schedule_cooking_experience(self, experience_name):
        """
        Schedule a cooking experience if it's available.

        :param experience_name: Name of the cooking experience to be scheduled
        :return: Confirmation message or error message
        """
        try:
            experience = self.cooking_experiences[experience_name]
            if experience['available']:
                experience['available'] = False
                return f"{experience_name} has been successfully scheduled."
            else:
                return f"Sorry, {experience_name} is not available."
        except KeyError:
            return f"Error: {experience_name} does not exist."

    def cancel_booking(self, room_name):
        """
        Cancel a room booking, making it available again.

        :param room_name: Name of the room to cancel booking
        :return: Confirmation message or error message
        """
        if room_name in self.bookings:
            self.rooms[room_name]['available'] = True
            self.bookings.remove(room_name)
            return f"{room_name} booking has been canceled."
        else:
            return f"Error: {room_name} was not booked."

    def get_bookings(self):
        """
        Retrieve a list of currently booked rooms.

        :return: List of booked rooms
        """
        return self.bookings


# Example usage
if __name__ == "__main__":
    booking_system = EcoLodgeBookingSystem()
    
    # Try booking a room
    print(booking_system.book_room("Room 101"))
    
    # Try scheduling a cooking experience
    print(booking_system.schedule_cooking_experience("Traditional Cooking Class"))
    
    # Check current bookings
    print("Current Bookings:", booking_system.get_bookings())
    
    # Cancel a room booking
    print(booking_system.cancel_booking("Room 101"))
    
    # Show bookings after cancellation
    print("Current Bookings after cancellation:", booking_system.get_bookings())
```
