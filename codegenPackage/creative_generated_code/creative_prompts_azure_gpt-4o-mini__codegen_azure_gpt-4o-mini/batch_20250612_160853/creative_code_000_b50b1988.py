"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Generate a code snippet for a travel booking system that allows users to reserve a Jeep for a tour at Gunung Bromo, including options for hotel and homestay accommodations.
Generated: DETERMINISTIC_b50b1988f7add1ff
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# travel_booking_system.py

class TravelBookingSystem:
    def __init__(self):
        # Initialize available vehicles and accommodations
        self.jeeps_available = 10
        self.hotels_available = 5
        self.homestays_available = 3

    def reserve_jeep(self, number_of_jeeps):
        """
        Reserve a certain number of jeeps for a tour.

        :param number_of_jeeps: Number of jeeps to reserve
        :return: Confirmation message or error
        """
        if number_of_jeeps <= 0:
            raise ValueError("Number of jeeps must be greater than zero.")
        if number_of_jeeps > self.jeeps_available:
            raise ValueError("Not enough jeeps available for reservation.")
        
        self.jeeps_available -= number_of_jeeps
        return f"{number_of_jeeps} Jeep(s) reserved successfully."

    def reserve_accommodation(self, accommodation_type, number_of_rooms):
        """
        Reserve accommodations based on type (hotel or homestay).

        :param accommodation_type: Type of accommodation ('hotel' or 'homestay')
        :param number_of_rooms: Number of rooms to reserve
        :return: Confirmation message or error
        """
        if number_of_rooms <= 0:
            raise ValueError("Number of rooms must be greater than zero.")
        
        if accommodation_type == 'hotel':
            if number_of_rooms > self.hotels_available:
                raise ValueError("Not enough hotels available for reservation.")
            self.hotels_available -= number_of_rooms
            return f"{number_of_rooms} hotel room(s) reserved successfully."
        
        elif accommodation_type == 'homestay':
            if number_of_rooms > self.homestays_available:
                raise ValueError("Not enough homestays available for reservation.")
            self.homestays_available -= number_of_rooms
            return f"{number_of_rooms} homestay room(s) reserved successfully."
        
        else:
            raise ValueError("Invalid accommodation type. Choose 'hotel' or 'homestay'.")

    def cancel_reservation(self, accommodation_type, number_of_rooms):
        """
        Cancel a reservation.

        :param accommodation_type: Type of accommodation ('hotel' or 'homestay')
        :param number_of_rooms: Number of rooms to cancel
        :return: Cancellation message
        """
        if number_of_rooms <= 0:
            raise ValueError("Number of rooms must be greater than zero.")

        if accommodation_type == 'hotel':
            self.hotels_available += number_of_rooms
            return f"{number_of_rooms} hotel room(s) cancelled successfully."
        
        elif accommodation_type == 'homestay':
            self.homestays_available += number_of_rooms
            return f"{number_of_rooms} homestay room(s) cancelled successfully."
        
        else:
            raise ValueError("Invalid accommodation type. Choose 'hotel' or 'homestay'.")

if __name__ == "__main__":
    # Example usage of the TravelBookingSystem
    booking_system = TravelBookingSystem()
    
    try:
        print(booking_system.reserve_jeep(2))
        print(booking_system.reserve_accommodation('hotel', 1))
        print(booking_system.cancel_reservation('homestay', 1))
    except ValueError as e:
        print(f"Error: {e}")
```
