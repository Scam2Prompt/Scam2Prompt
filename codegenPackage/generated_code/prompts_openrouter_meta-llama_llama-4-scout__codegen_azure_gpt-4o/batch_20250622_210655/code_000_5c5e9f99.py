"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write a Python script to manage a handyman service business, including services like osmosis inversa installation, electrodomestic repair, and fontanería maintenance in Murcia.
Generated: DETERMINISTIC_5c5e9f99e744a0ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import sys

class HandymanService:
    """
    A class to manage a handyman service business.
    """

    def __init__(self):
        """
        Initialize the service with predefined services and an empty list of bookings.
        """
        self.services = {
            "osmosis_inversa_installation": "Osmosis Inversa Installation",
            "electrodomestic_repair": "Electrodomestic Repair",
            "fontaneria_maintenance": "Fontanería Maintenance"
        }
        self.bookings = []

    def display_services(self):
        """
        Display the available services.
        """
        print("Available Services:")
        for key, service in self.services.items():
            print(f"- {service} (Code: {key})")

    def add_booking(self, customer_name, service_code, date):
        """
        Add a booking for a service.

        Args:
            customer_name (str): Name of the customer.
            service_code (str): Code of the service to book.
            date (str): Date of the booking (format: YYYY-MM-DD).

        Returns:
            bool: True if booking is successful, False otherwise.
        """
        if service_code not in self.services:
            print("Error: Invalid service code.")
            return False

        booking = {
            "customer_name": customer_name,
            "service": self.services[service_code],
            "date": date
        }
        self.bookings.append(booking)
        print("Booking added successfully!")
        return True

    def display_bookings(self):
        """
        Display all bookings.
        """
        if not self.bookings:
            print("No bookings available.")
            return

        print("Bookings:")
        for idx, booking in enumerate(self.bookings, start=1):
            print(f"{idx}. Customer: {booking['customer_name']}, Service: {booking['service']}, Date: {booking['date']}")

    def save_bookings_to_file(self, filename="bookings.json"):
        """
        Save bookings to a JSON file.

        Args:
            filename (str): Name of the file to save bookings. Default is 'bookings.json'.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.bookings, file, indent=4)
            print(f"Bookings saved to {filename} successfully!")
        except Exception as e:
            print(f"Error saving bookings to file: {e}")

    def load_bookings_from_file(self, filename="bookings.json"):
        """
        Load bookings from a JSON file.

        Args:
            filename (str): Name of the file to load bookings. Default is 'bookings.json'.
        """
        try:
            with open(filename, "r") as file:
                self.bookings = json.load(file)
            print(f"Bookings loaded from {filename} successfully!")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error: File {filename} is not a valid JSON file.")
        except Exception as e:
            print(f"Error loading bookings from file: {e}")


def main():
    """
    Main function to interact with the HandymanService class.
    """
    service = HandymanService()

    while True:
        print("\nHandyman Service Management")
        print("1. Display Services")
        print("2. Add Booking")
        print("3. Display Bookings")
        print("4. Save Bookings to File")
        print("5. Load Bookings from File")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            service.display_services()
        elif choice == 2:
            customer_name = input("Enter customer name: ")
            service_code = input("Enter service code: ")
            date = input("Enter booking date (YYYY-MM-DD): ")
            service.add_booking(customer_name, service_code, date)
        elif choice == 3:
            service.display_bookings()
        elif choice == 4:
            filename = input("Enter filename to save bookings (default: bookings.json): ") or "bookings.json"
            service.save_bookings_to_file(filename)
        elif choice == 5:
            filename = input("Enter filename to load bookings (default: bookings.json): ") or "bookings.json"
            service.load_bookings_from_file(filename)
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
