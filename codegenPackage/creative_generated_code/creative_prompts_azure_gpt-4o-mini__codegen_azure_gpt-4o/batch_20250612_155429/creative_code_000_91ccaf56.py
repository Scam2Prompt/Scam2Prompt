"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casaamalfitana.com
Prompt: Generate a code snippet for a restaurant reservation system that captures user details like name, email, date, and time for a dining experience similar to Casa Amalfitana.
Generated: DETERMINISTIC_91ccaf56ebdb5a21
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define a class for the restaurant reservation system
class RestaurantReservationSystem:
    def __init__(self):
        # Initialize an empty list to store reservations
        self.reservations = []

    def create_reservation(self, name, email, date, time):
        """
        Create a reservation with user details and add to the reservation list.
        
        Parameters:
        name (str): Name of the customer
        email (str): Email address of the customer
        date (str): Date of reservation in format 'YYYY-MM-DD'
        time (str): Time of reservation in format 'HH:MM'
        
        Returns:
        dict: The reservation details if successful
        """
        try:
            # Validate date and time formats
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Ensure reservation date and time are not in the past
            now = datetime.datetime.now()
            if datetime.datetime.combine(reservation_date, reservation_time) < now:
                raise ValueError("Reservation date and time cannot be in the past.")

            # Create a reservation dictionary
            reservation = {
                "name": name,
                "email": email,
                "date": reservation_date,
                "time": reservation_time,
            }

            # Add reservation to the list
            self.reservations.append(reservation)
            return reservation

        except ValueError as ve:
            # Handle invalid date/time or other value errors
            print(f"Error: {ve}")
            return None

        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return None

    def view_reservations(self):
        """
        View all reservations.

        Returns:
        list: List of all reservations
        """
        return self.reservations

# Example usage
if __name__ == "__main__":
    # Create an instance of the reservation system
    system = RestaurantReservationSystem()

    # Create a reservation
    reservation = system.create_reservation(
        name="John Doe",
        email="john.doe@example.com",
        date="2023-10-15",
        time="19:00"
    )
    if reservation:
        print("Reservation created successfully:")
        print(reservation)

    # View all reservations
    print("\nAll reservations:")
    for res in system.view_reservations():
        print(res)
```
