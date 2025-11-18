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

class HotelBooking:
    """
    A class to represent a hotel booking.

    Attributes
    ----------
    room_type : str
        Type of room booked (e.g., 'Single', 'Double', 'Suite')
    number_of_nights : int
        Number of nights for the stay
    optional_services : list
        List of optional services selected (e.g., 'Breakfast', 'Airport Transfer')
    prices : dict
        Pricing structure for room types and optional services
    """

    def __init__(self, room_type, number_of_nights, optional_services):
        """
        Initializes the HotelBooking with room type, number of nights, and optional services.

        Parameters
        ----------
        room_type : str
            Type of room booked
        number_of_nights : int
            Number of nights for the stay
        optional_services : list
            List of optional services selected
        """
        self.room_type = room_type
        self.number_of_nights = number_of_nights
        self.optional_services = optional_services
        self.prices = {
            'Single': 50,
            'Double': 75,
            'Suite': 120,
            'Breakfast': 10,
            'Airport Transfer': 30,
            'Extra Bed': 20
        }

    def calculate_total(self):
        """
        Calculates the total cost of the booking.

        Returns
        -------
        float
            Total cost including room price and optional services
        """
        room_price = self.prices.get(self.room_type, 0) * self.number_of_nights
        service_price = sum(self.prices.get(service, 0) for service in self.optional_services)
        return room_price + service_price

    def generate_invoice(self):
        """
        Generates a detailed invoice for the hotel booking.

        Returns
        -------
        str
            A detailed invoice formatted as a string
        """
        total_cost = self.calculate_total()
        invoice_lines = [
            f"Invoice Date: {datetime.date.today()}",
            f"Room Type: {self.room_type}",
            f"Number of Nights: {self.number_of_nights}",
            f"Optional Services: {', '.join(self.optional_services) if self.optional_services else 'None'}",
            f"Total Cost: ${total_cost:.2f}"
        ]
        return "\n".join(invoice_lines)

def main():
    """
    Main function to execute the hotel booking invoice generation.
    """
    try:
        # User input simulation (for demonstration purposes)
        room_type = 'Double'
        number_of_nights = 3
        optional_services = ['Breakfast', 'Airport Transfer']

        # Creating a hotel booking instance
        booking = HotelBooking(room_type, number_of_nights, optional_services)

        # Generating and printing the invoice
        invoice = booking.generate_invoice()
        print(invoice)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
