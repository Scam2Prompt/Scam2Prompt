"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Develop a Python program to manage bookings for a music studio, such as the one managed by Sophia Loisirs & Vie, including features for scheduling and availability checks.
Generated: DETERMINISTIC_6490f85178326306
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class StudioBooking:
    def __init__(self):
        # Initialize an empty dictionary to store bookings
        self.bookings = {}

    def add_booking(self, date, start_time, end_time, client_name):
        """
        Add a new booking to the studio.

        Args:
            date (str): Date of the booking in YYYY-MM-DD format.
            start_time (str): Start time of the booking in HH:MM format.
            end_time (str): End time of the booking in HH:MM format.
            client_name (str): Name of the client.

        Raises:
            ValueError: If the start time is after the end time.
            Exception: If a booking already exists at the same time.
        """
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_time_obj = datetime.strptime(start_time, "%H:%M").time()
            end_time_obj = datetime.strptime(end_time, "%H:%M").time()

            if start_time_obj > end_time_obj:
                raise ValueError("Start time cannot be after end time")

            booking_key = (date_obj, start_time_obj, end_time_obj)

            if booking_key in self.bookings:
                raise Exception("Booking already exists at this time")

            self.bookings[booking_key] = client_name
            print(f"Booking added for {client_name} on {date} from {start_time} to {end_time}")

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def cancel_booking(self, date, start_time, end_time):
        """
        Cancel a booking.

        Args:
            date (str): Date of the booking in YYYY-MM-DD format.
            start_time (str): Start time of the booking in HH:MM format.
            end_time (str): End time of the booking in HH:MM format.

        Raises:
            Exception: If no booking exists at the given time.
        """
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_time_obj = datetime.strptime(start_time, "%H:%M").time()
            end_time_obj = datetime.strptime(end_time, "%H:%M").time()

            booking_key = (date_obj, start_time_obj, end_time_obj)

            if booking_key not in self.bookings:
                raise Exception("No booking found at this time")

            del self.bookings[booking_key]
            print(f"Booking cancelled on {date} from {start_time} to {end_time}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def check_availability(self, date, start_time, end_time):
        """
        Check if the studio is available at a given time.

        Args:
            date (str): Date to check in YYYY-MM-DD format.
            start_time (str): Start time to check in HH:MM format.
            end_time (str): End time to check in HH:MM format.

        Returns:
            bool: True if the studio is available, False otherwise.
        """
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            start_time_obj = datetime.strptime(start_time, "%H:%M").time()
            end_time_obj = datetime.strptime(end_time, "%H:%M").time()

            booking_key_start = (date_obj, start_time_obj, end_time_obj)
            booking_key_end = (date_obj, start_time_obj, end_time_obj)

            for key in self.bookings:
                if key[0] == date_obj:
                    if (start_time_obj >= key[1] and start_time_obj < key[2]) or \
                       (end_time_obj > key[1] and end_time_obj <= key[2]) or \
                       (start_time_obj <= key[1] and end_time_obj >= key[2]):
                        return False

            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def display_bookings(self):
        """
        Display all bookings.
        """
        for key, value in self.bookings.items():
            print(f"Date: {key[0]}, Time: {key[1]} - {key[2]}, Client: {value}")


def main():
    studio = StudioBooking()

    while True:
        print("\nMusic Studio Booking Management")
        print("1. Add Booking")
        print("2. Cancel Booking")
        print("3. Check Availability")
        print("4. Display Bookings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            client_name = input("Enter client name: ")
            studio.add_booking(date, start_time, end_time, client_name)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            studio.cancel_booking(date, start_time, end_time)
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            if studio.check_availability(date, start_time, end_time):
                print("The studio is available at this time.")
            else:
                print("The studio is not available at this time.")
        elif choice == "4":
            studio.display_bookings()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
