"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Generate a code snippet for a booking system that allows users to select a Jeep tour in Bali, including options for sunrise and sunset tours at Mount Batur.
Generated: DETERMINISTIC_3b41e6b2204cf7db
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class JeepTourBookingSystem:
    """
    A booking system for Jeep tours in Bali, including sunrise and sunset tours at Mount Batur.
    """

    def __init__(self):
        # Initialize available tours and bookings
        self.tours = {
            "Sunrise Tour": {
                "description": "Experience the stunning sunrise at Mount Batur with a Jeep adventure.",
                "start_time": "04:00 AM",
                "end_time": "08:00 AM",
                "price": 75.00  # USD
            },
            "Sunset Tour": {
                "description": "Enjoy a picturesque sunset at Mount Batur with a Jeep adventure.",
                "start_time": "04:00 PM",
                "end_time": "08:00 PM",
                "price": 75.00  # USD
            }
        }
        self.bookings = []  # List to store bookings

    def display_tours(self):
        """
        Display available tours to the user.
        """
        print("Available Jeep Tours in Bali:\n")
        for tour_name, tour_details in self.tours.items():
            print(f"{tour_name}:")
            print(f"  Description: {tour_details['description']}")
            print(f"  Start Time: {tour_details['start_time']}")
            print(f"  End Time: {tour_details['end_time']}")
            print(f"  Price: ${tour_details['price']:.2f}")
            print()

    def book_tour(self, user_name, tour_name, num_people):
        """
        Book a tour for the user.
        
        Args:
            user_name (str): Name of the user.
            tour_name (str): Name of the tour to book.
            num_people (int): Number of people for the booking.
        
        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate tour name
            if tour_name not in self.tours:
                return f"Error: '{tour_name}' is not a valid tour name."

            # Validate number of people
            if num_people <= 0:
                return "Error: Number of people must be greater than zero."

            # Calculate total cost
            tour = self.tours[tour_name]
            total_cost = tour["price"] * num_people

            # Create booking record
            booking = {
                "user_name": user_name,
                "tour_name": tour_name,
                "num_people": num_people,
                "total_cost": total_cost,
                "booking_time": datetime.datetime.now()
            }
            self.bookings.append(booking)

            # Return confirmation message
            return (
                f"Booking confirmed for {user_name}!\n"
                f"Tour: {tour_name}\n"
                f"Number of People: {num_people}\n"
                f"Total Cost: ${total_cost:.2f}\n"
                f"Booking Time: {booking['booking_time'].strftime('%Y-%m-%d %H:%M:%S')}"
            )
        except Exception as e:
            return f"An error occurred while booking the tour: {str(e)}"

    def view_bookings(self):
        """
        Display all bookings.
        """
        if not self.bookings:
            print("No bookings have been made yet.")
            return

        print("Current Bookings:\n")
        for booking in self.bookings:
            print(f"User: {booking['user_name']}")
            print(f"Tour: {booking['tour_name']}")
            print(f"Number of People: {booking['num_people']}")
            print(f"Total Cost: ${booking['total_cost']:.2f}")
            print(f"Booking Time: {booking['booking_time'].strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 40)


# Example Usage
if __name__ == "__main__":
    # Initialize the booking system
    system = JeepTourBookingSystem()

    # Display available tours
    system.display_tours()

    # User attempts to book a tour
    print(system.book_tour("John Doe", "Sunrise Tour", 2))
    
    # View all bookings
    system.view_bookings()
```
