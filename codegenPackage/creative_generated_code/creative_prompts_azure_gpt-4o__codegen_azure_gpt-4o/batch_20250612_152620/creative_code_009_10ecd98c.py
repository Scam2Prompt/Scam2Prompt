"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Create a script that generates a detailed invoice for hotel bookings, including room type, number of nights, and optional services, inspired by Hostal Koltin Suchitoto's pricing structure.
Generated: DETERMINISTIC_10ecd98c870f0d9a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HotelBookingInvoice:
    def __init__(self, customer_name, room_type, nights, optional_services=None):
        """
        Initializes the HotelBookingInvoice object.

        :param customer_name: Name of the customer
        :param room_type: Type of room selected (e.g., 'single', 'double', 'suite')
        :param nights: Number of nights to stay
        :param optional_services: List of optional services selected (e.g., ['breakfast', 'laundry'])
        """
        self.customer_name = customer_name
        self.room_type = room_type.lower()
        self.nights = nights
        self.optional_services = optional_services if optional_services else []
        self.room_rates = {'single': 50, 'double': 75, 'suite': 120}  # Pricing structure
        self.service_rates = {'breakfast': 10, 'laundry': 15}  # Optional services pricing

    def calculate_room_cost(self):
        """
        Calculates the cost for the room based on the type and number of nights.

        :return: Total room cost
        """
        if self.room_type not in self.room_rates:
            raise ValueError(f"Invalid room type: {self.room_type}")
        return self.room_rates[self.room_type] * self.nights

    def calculate_service_cost(self):
        """
        Calculates the cost for optional services selected.

        :return: Total service cost
        """
        total_service_cost = 0
        for service in self.optional_services:
            if service.lower() not in self.service_rates:
                raise ValueError(f"Invalid service: {service}")
            total_service_cost += self.service_rates[service.lower()]
        return total_service_cost

    def generate_invoice(self):
        """
        Generates the detailed invoice.

        :return: Invoice as a string
        """
        try:
            room_cost = self.calculate_room_cost()
            service_cost = self.calculate_service_cost()
            total_cost = room_cost + service_cost

            invoice = f"---- Hotel Booking Invoice ----\n"
            invoice += f"Customer Name: {self.customer_name}\n"
            invoice += f"Room Type: {self.room_type.capitalize()}\n"
            invoice += f"Number of Nights: {self.nights}\n"
            invoice += f"Room Cost: ${room_cost:.2f}\n"
            
            if self.optional_services:
                invoice += f"Optional Services:\n"
                for service in self.optional_services:
                    invoice += f"  - {service.capitalize()}: ${self.service_rates[service.lower()]:.2f}\n"
                invoice += f"Service Cost: ${service_cost:.2f}\n"
            else:
                invoice += f"Optional Services: None\n"
                
            invoice += f"Total Cost: ${total_cost:.2f}\n"
            invoice += f"Booking Date: {datetime.date.today()}\n"
            invoice += f"------------------------------"

            return invoice
        except ValueError as e:
            return f"Error: {str(e)}"

# Example Usage:
if __name__ == "__main__":
    # User input simulation
    customer_name = "John Doe"
    room_type = "suite"
    nights = 3
    optional_services = ["breakfast", "laundry"]

    # Generate Invoice
    invoice = HotelBookingInvoice(customer_name, room_type, nights, optional_services)
    print(invoice.generate_invoice())
```
