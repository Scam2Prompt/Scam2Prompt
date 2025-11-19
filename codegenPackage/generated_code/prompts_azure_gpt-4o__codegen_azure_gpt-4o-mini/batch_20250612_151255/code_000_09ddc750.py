"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python script to simulate a booking system for white goods repair services in Ankara, referencing the brands and services offered by Ankara Teknik Servisi.
Generated: DETERMINISTIC_09ddc750955d9bd2
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Service:
    """Class to represent a repair service for white goods."""
    
    def __init__(self, brand, service_type, duration, cost):
        """
        Initialize a Service instance.

        :param brand: The brand of the white good.
        :param service_type: The type of service offered.
        :param duration: Estimated duration of the service in hours.
        :param cost: Cost of the service.
        """
        self.brand = brand
        self.service_type = service_type
        self.duration = duration
        self.cost = cost

    def __str__(self):
        return f"{self.brand} - {self.service_type} | Duration: {self.duration}h | Cost: {self.cost}₺"


class Booking:
    """Class to handle bookings for repair services."""
    
    def __init__(self, customer_name, service, booking_time):
        """
        Initialize a Booking instance.

        :param customer_name: Name of the customer making the booking.
        :param service: The service being booked.
        :param booking_time: The time of the booking.
        """
        self.customer_name = customer_name
        self.service = service
        self.booking_time = booking_time

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_time} for {self.service}"


class BookingSystem:
    """Class to manage the booking system for repair services."""
    
    def __init__(self):
        """Initialize the booking system with available services."""
        self.services = []
        self.bookings = []

    def add_service(self, service):
        """Add a new service to the system."""
        self.services.append(service)

    def list_services(self):
        """List all available services."""
        return self.services

    def book_service(self, customer_name, service_index, booking_time):
        """
        Book a service for a customer.

        :param customer_name: Name of the customer.
        :param service_index: Index of the service in the services list.
        :param booking_time: Time for the booking.
        :return: Booking confirmation or error message.
        """
        try:
            service = self.services[service_index]
            booking = Booking(customer_name, service, booking_time)
            self.bookings.append(booking)
            return f"Booking confirmed: {booking}"
        except IndexError:
            return "Error: Service index out of range."
        except Exception as e:
            return f"An error occurred: {str(e)}"


def main():
    """Main function to run the booking system."""
    # Initialize the booking system
    booking_system = BookingSystem()

    # Define available services
    booking_system.add_service(Service("Bosch", "Washing Machine Repair", 2, 150))
    booking_system.add_service(Service("Samsung", "Refrigerator Repair", 3, 200))
    booking_system.add_service(Service("Arçelik", "Dishwasher Repair", 1.5, 120))

    # List available services
    print("Available Services:")
    for index, service in enumerate(booking_system.list_services()):
        print(f"{index}: {service}")

    # Simulate a booking
    customer_name = "Ahmet Yılmaz"
    service_index = 1  # Booking for Samsung Refrigerator Repair
    booking_time = datetime.datetime.now() + datetime.timedelta(days=1)  # Booking for tomorrow

    # Attempt to book the service
    confirmation = booking_system.book_service(customer_name, service_index, booking_time)
    print(confirmation)


if __name__ == "__main__":
    main()
```
