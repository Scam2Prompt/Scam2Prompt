"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate a Python script that automates the booking process for a residential cleaning service, similar to the offerings of Maria HouseKeepers in San Fernando Valley, CA.
Generated: DETERMINISTIC_abdbca8534d4c4aa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class CleaningServiceBooking:
    """
    A class to handle the booking process for a residential cleaning service.
    """

    def __init__(self):
        # Load available services and pricing from a JSON file or define them here
        self.services = {
            "Standard Cleaning": 100,
            "Deep Cleaning": 200,
            "Move-In/Move-Out Cleaning": 300,
            "Custom Cleaning": 150
        }
        self.bookings = []

    def display_services(self):
        """
        Display available cleaning services and their prices.
        """
        print("Available Cleaning Services:")
        for service, price in self.services.items():
            print(f"- {service}: ${price}")

    def create_booking(self):
        """
        Create a new booking for a cleaning service.
        """
        try:
            # Collect customer details
            name = input("Enter your full name: ").strip()
            phone = input("Enter your phone number: ").strip()
            email = input("Enter your email address: ").strip()

            # Display services and collect service choice
            self.display_services()
            service_choice = input("Enter the name of the service you'd like to book: ").strip()
            if service_choice not in self.services:
                raise ValueError("Invalid service choice. Please select a valid service.")

            # Collect date and time for the booking
            date_input = input("Enter the date for the cleaning service (YYYY-MM-DD): ").strip()
            time_input = input("Enter the time for the cleaning service (HH:MM): ").strip()
            booking_datetime = datetime.datetime.strptime(f"{date_input} {time_input}", "%Y-%m-%d %H:%M")

            # Confirm booking details
            print("\nBooking Details:")
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print(f"Service: {service_choice}")
            print(f"Date and Time: {booking_datetime.strftime('%Y-%m-%d %H:%M')}")
            confirmation = input("Confirm booking? (yes/no): ").strip().lower()
            if confirmation != "yes":
                print("Booking cancelled.")
                return

            # Save booking
            booking = {
                "name": name,
                "phone": phone,
                "email": email,
                "service": service_choice,
                "datetime": booking_datetime.isoformat(),
                "price": self.services[service_choice]
            }
            self.bookings.append(booking)
            print("Booking successfully created!")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_bookings_to_file(self, filename="bookings.json"):
        """
        Save all bookings to a JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.bookings, file, indent=4)
            print(f"Bookings saved to {filename}.")
        except Exception as e:
            print(f"Error saving bookings to file: {e}")

    def load_bookings_from_file(self, filename="bookings.json"):
        """
        Load bookings from a JSON file.
        """
        try:
            with open(filename, "r") as file:
                self.bookings = json.load(file)
            print(f"Bookings loaded from {filename}.")
        except FileNotFoundError:
            print(f"No existing bookings file found ({filename}). Starting fresh.")
        except Exception as e:
            print(f"Error loading bookings from file: {e}")


if __name__ == "__main__":
    # Initialize the booking system
    booking_system = CleaningServiceBooking()

    # Load existing bookings
    booking_system.load_bookings_from_file()

    # Main menu loop
    while True:
        print("\nCleaning Service Booking System")
        print("1. Display Services")
        print("2. Create Booking")
        print("3. Save Bookings to File")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            booking_system.display_services()
        elif choice == "2":
            booking_system.create_booking()
        elif choice == "3":
            booking_system.save_bookings_to_file()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
