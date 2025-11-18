"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Develop a booking system in Python for Playland Kenya that allows users to reserve activities like bowling, ropes courses, and virtual reality sessions, using the pricing details from the website.
Generated: DETERMINISTIC_6bc4fdebc3ca24cc
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Activity:
    """Represents an activity available for booking."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Booking:
    """Represents a user's booking for an activity."""

    def __init__(self, activity, user_name, date, num_people):
        self.activity = activity
        self.user_name = user_name
        self.date = date
        self.num_people = num_people

    def total_cost(self):
        """Calculates the total cost of the booking."""
        return self.activity.price * self.num_people

class BookingSystem:
    """Handles booking activities for Playland Kenya."""

    def __init__(self):
        # A list to store available activities
        self.activities = []
        # Populate activities with available options
        self.populate_activities()

    def populate_activities(self):
        """Populates the list of activities with pricing information."""
        self.activities.append(Activity("Bowling", 10))
        self.activities.append(Activity("Ropes Course", 15))
        self.activities.append(Activity("Virtual Reality", 20))

    def display_activities(self):
        """Displays available activities and their prices."""
        print("Available Activities:")
        for index, activity in enumerate(self.activities):
            print(f"{index + 1}. {activity.name} - ${activity.price} per person")

    def book_activity(self, activity_index, user_name, date, num_people):
        """Books an activity for the user."""
        try:
            # Validate activity index
            if activity_index < 0 or activity_index >= len(self.activities):
                raise ValueError("Invalid activity selection.")
                
            # Validate date
            if not isinstance(date, datetime.date):
                raise ValueError("Invalid date format. Please provide a date object.")
                
            # Create the booking
            selected_activity = self.activities[activity_index]
            booking = Booking(selected_activity, user_name, date, num_people)

            # Print the booking details
            print(f"Booking confirmed for {user_name}: {num_people} x {selected_activity.name} on {date} - Total Cost: ${booking.total_cost()}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Initialize the booking system
    booking_system = BookingSystem()
    
    # Display available activities
    booking_system.display_activities()

    # Example booking (replace with actual input in production)
    user_name = "John Doe"
    activity_index = 0  # User selects bowling
    booking_date = datetime.date(2023, 10, 25)  # Example date
    num_people = 2  # Number of participants

    # Attempt to book the activity
    booking_system.book_activity(activity_index, user_name, booking_date, num_people)
```
