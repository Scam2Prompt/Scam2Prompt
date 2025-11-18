"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python script to simulate a booking system for white goods repair services in Ankara, referencing the brands and services offered by Ankara Teknik Servisi.
Generated: DETERMINISTIC_09ddc750955d9bd2
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Service:
    """Class to represent a repair service offered."""
    
    def __init__(self, brand, service_type, duration, cost):
        """
        Initialize a service.

        :param brand: Name of the brand for the service
        :param service_type: Type of repair service
        :param duration: Estimated duration of the service in hours
        :param cost: Cost of the service
        """
        self.brand = brand
        self.service_type = service_type
        self.duration = duration
        self.cost = cost

    def __str__(self):
        return f"{self.brand} - {self.service_type} | Duration: {self.duration} hrs | Cost: {self.cost} TL"


class Booking:
    """Class to handle bookings for repair services."""
    
    def __init__(self):
        """Initialize the booking system."""
        self.services = []
        self.bookings = []

    def add_service(self, service):
        """
        Add a service to the booking system.

        :param service: Service object to add
        """
        self.services.append(service)

    def list_services(self):
        """List all available services."""
        return "\n".join(str(service) for service in self.services)

    def book_service(self, service_index, customer_name, date_time):
        """
        Create a booking for a specified service.

        :param service_index: Index of the service in the services list
        :param customer_name: Name of the customer
        :param date_time: Desired booking date and time
        :return: Confirmation message or error
        """
        try:
            service = self.services[service_index]
            booking_time = date_time + datetime.timedelta(hours=service.duration)
            self.bookings.append({
                "customer_name": customer_name,
                "service": service,
                "booking_time": date_time,
                "completion_time": booking_time
            })
            return f"Booking confirmed for {customer_name} on {date_time.strftime('%Y-%m-%d %H:%M')}."
        except IndexError:
            return "Error: Service index is out of range."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"


def main():
    """Main function to simulate the booking system."""
    booking_system = Booking()

    # Adding services offered by Ankara Teknik Servisi
    booking_system.add_service(Service("Bosch", "Washing Machine Repair", 2, 150))
    booking_system.add_service(Service("Arçelik", "Refrigerator Repair", 3, 200))
    booking_system.add_service(Service("Siemens", "Dishwasher Repair", 2.5, 180))

    print("Available Services:")
    print(booking_system.list_services())

    # Simulating a booking
    try:
        customer_name = input("Enter customer's name: ")
        service_index = int(input("Enter service index to book (0-2): "))
        booking_date_str = input("Enter booking date and time (YYYY-MM-DD HH:MM): ")
        booking_date = datetime.datetime.strptime(booking_date_str, '%Y-%m-%d %H:%M')

        confirmation = booking_system.book_service(service_index, customer_name, booking_date)
        print(confirmation)
    except ValueError:
        print("Invalid input. Please ensure you enter the correct format for service index and date.")

if __name__ == "__main__":
    main()
```
