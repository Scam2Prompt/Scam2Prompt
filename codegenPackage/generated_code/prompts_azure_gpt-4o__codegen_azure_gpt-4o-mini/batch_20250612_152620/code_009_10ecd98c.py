"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Create a script that generates a detailed invoice for hotel bookings, including room type, number of nights, and optional services, inspired by Hostal Koltin Suchitoto's pricing structure.
Generated: DETERMINISTIC_10ecd98c870f0d9a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Invoice:
    def __init__(self, guest_name, room_type, number_of_nights, optional_services=None):
        """
        Initialize the Invoice object with guest details and booking information.

        :param guest_name: Name of the guest
        :param room_type: Type of room booked
        :param number_of_nights: Number of nights booked
        :param optional_services: List of optional services selected by the guest
        """
        self.guest_name = guest_name
        self.room_type = room_type
        self.number_of_nights = number_of_nights
        self.optional_services = optional_services if optional_services else []
        self.room_rates = {
            'single': 50,
            'double': 80,
            'suite': 120
        }
        self.service_rates = {
            'breakfast': 10,
            'airport_transfer': 30,
            'spa': 50
        }
        self.invoice_date = datetime.now()

    def calculate_room_cost(self):
        """
        Calculate the total cost for the room based on the type and number of nights.

        :return: Total room cost
        """
        if self.room_type not in self.room_rates:
            raise ValueError(f"Invalid room type: {self.room_type}")
        return self.room_rates[self.room_type] * self.number_of_nights

    def calculate_service_cost(self):
        """
        Calculate the total cost for optional services selected.

        :return: Total service cost
        """
        total_service_cost = 0
        for service in self.optional_services:
            if service not in self.service_rates:
                raise ValueError(f"Invalid service: {service}")
            total_service_cost += self.service_rates[service]
        return total_service_cost

    def generate_invoice(self):
        """
        Generate a detailed invoice as a dictionary.

        :return: Invoice details
        """
        try:
            room_cost = self.calculate_room_cost()
            service_cost = self.calculate_service_cost()
            total_cost = room_cost + service_cost

            invoice_details = {
                'guest_name': self.guest_name,
                'room_type': self.room_type,
                'number_of_nights': self.number_of_nights,
                'room_cost': room_cost,
                'optional_services': self.optional_services,
                'service_cost': service_cost,
                'total_cost': total_cost,
                'invoice_date': self.invoice_date.strftime('%Y-%m-%d %H:%M:%S')
            }
            return invoice_details
        except ValueError as e:
            print(f"Error generating invoice: {e}")
            return None

def main():
    # Example usage of the Invoice class
    guest_name = "John Doe"
    room_type = "double"
    number_of_nights = 3
    optional_services = ["breakfast", "spa"]

    invoice = Invoice(guest_name, room_type, number_of_nights, optional_services)
    invoice_details = invoice.generate_invoice()

    if invoice_details:
        print(json.dumps(invoice_details, indent=4))

if __name__ == "__main__":
    main()
```
