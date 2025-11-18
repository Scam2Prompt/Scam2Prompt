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


class BookingSystem:
    """
    A booking system for Playland Kenya that allows users to reserve activities.
    """

    def __init__(self):
        # Activity pricing details as per Playland Kenya's website
        self.activities = {
            "bowling": 800,  # Price in KES
            "ropes_course": 1000,  # Price in KES
            "virtual_reality": 600  # Price in KES
        }
        # Track reservations
        self.reservations = []

    def list_activities(self):
        """
        List available activities and their prices.
        """
        print("Available Activities (Prices in KES):")
        for activity, price in self.activities.items():
            print(f"- {activity.title()}: {price} KES")

    def book_activity(self, user_name, activity_name, date, time):
        """
        Book an activity for a user.
        :param user_name: Name of the user
        :param activity_name: Name of the activity to book
        :param date: Date for the booking (YYYY-MM-DD)
        :param time: Time for the booking (HH:MM)
        """
        try:
            # Validate activity
            if activity_name not in self.activities:
                raise ValueError(f"Activity '{activity_name}' is not available.")

            # Validate date and time format
            reservation_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            reservation_time = datetime.datetime.strptime(time, "%H:%M").time()

            # Create reservation entry
            reservation = {
                "user_name": user_name,
                "activity": activity_name,
                "date": reservation_date,
                "time": reservation_time,
                "price": self.activities[activity_name]
            }

            # Store the reservation
            self.reservations.append(reservation)

            print(f"Reservation successful for {user_name}!")
            print(f"Details: {activity_name.title()} on {date} at {time} for {self.activities[activity_name]} KES")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_reservations(self):
        """
        View all reservations in the system.
        """
        if not self.reservations:
            print("No reservations have been made yet.")
            return

        print("Reservations:")
        for idx, reservation in enumerate(self.reservations, start=1):
            print(f"{idx}. {reservation['user_name']} - {reservation['activity'].title()} on "
                  f"{reservation['date']} at {reservation['time']} - {reservation['price']} KES")


# Main execution
if __name__ == "__main__":
    system = BookingSystem()

    while True:
        print("\n--- Playland Kenya Booking System ---")
        print("1. View Activities")
        print("2. Book an Activity")
        print("3. View Reservations")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                system.list_activities()
            elif choice == 2:
                user_name = input("Enter your name: ").strip()
                activity_name = input("Enter the activity name (e.g., bowling): ").strip().lower()
                date = input("Enter the date (YYYY-MM-DD): ").strip()
                time = input("Enter the time (HH:MM): ").strip()
                system.book_activity(user_name, activity_name, date, time)
            elif choice == 3:
                system.view_reservations()
            elif choice == 4:
                print("Thank you for using the Playland Kenya Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
```
