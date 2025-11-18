"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Write a script to simulate booking services on the Swell Creative Management website, including selecting services like packaging design or experiential marketing.
Generated: DETERMINISTIC_3d8c9f71e5bb03ae
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class BookingSystem:
    """
    A class to simulate booking services on a website like Swell Creative Management.

    Attributes:
        services (dict): A dictionary of available services and their prices.
    """

    def __init__(self):
        """
        Initializes the BookingSystem with available services.
        """
        self.services = {
            "Packaging Design": 1500,
            "Experiential Marketing": 2500,
            "Brand Strategy": 2000,
            "Product Photography": 1800
        }
        self.booked_services = []

    def display_services(self):
        """
        Displays the list of services available for booking.
        """
        print("\nAvailable Services:")
        for index, (service, price) in enumerate(self.services.items(), start=1):
            print(f"{index}. {service} - ${price}")

    def book_service(self, service_number):
        """
        Books a service based on its number in the list.

        Args:
            service_number (int): The number corresponding to the service to be booked.

        Raises:
            ValueError: If the service number is invalid.
        """
        try:
            service_name = list(self.services.keys())[service_number - 1]  # Adjust for zero-based indexing
            self.booked_services.append(service_name)
            print(f"Service '{service_name}' has been successfully booked.")
        except IndexError:
            raise ValueError("Invalid service number. Please select a valid option.")

    def display_booked_services(self):
        """
        Displays the list of services that have been booked.
        """
        if self.booked_services:
            print("\nYour Booked Services:")
            for service in self.booked_services:
                print(f"- {service}")
        else:
            print("\nNo services have been booked yet.")

    def run(self):
        """
        Runs the booking system, allowing the user to select and book services.
        """
        print("\nWelcome to Swell Creative Management Booking System")
        while True:
            self.display_services()
            print("\nOptions:")
            print("1. Book a service")
            print("2. View booked services")
            print("3. Exit")
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    try:
                        service_number = int(input("\nEnter the number of the service you'd like to book: "))
                        self.book_service(service_number)
                    except ValueError as e:
                        print(f"Error: {e}")
                elif choice == 2:
                    self.display_booked_services()
                elif choice == 3:
                    print("\nThank you for using the booking system. Goodbye!")
                    break
                else:
                    print("\nInvalid option. Please select a valid choice.")
            except ValueError:
                print("\nInvalid input. Please enter a number corresponding to the options.")

if __name__ == "__main__":
    try:
        booking_system = BookingSystem()
        booking_system.run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
