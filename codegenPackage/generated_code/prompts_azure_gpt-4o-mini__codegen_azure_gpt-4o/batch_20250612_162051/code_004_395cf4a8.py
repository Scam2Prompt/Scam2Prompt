"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Illustrate how to implement a booking system for dumpster rentals using the service areas and pricing details provided by Purple Dumpster.
Generated: DETERMINISTIC_395cf4a8e63ec1ce
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

class DumpsterRentalSystem:
    """
    A booking system for dumpster rentals.
    """

    def __init__(self):
        # Initialize service areas and pricing details
        self.service_areas = {
            "Downtown": 100,  # Price per day in USD
            "Suburbs": 80,
            "Industrial Zone": 120,
        }
        self.bookings = []  # List to store bookings

    def list_service_areas(self):
        """
        List all available service areas and their pricing.
        """
        print("Available Service Areas and Pricing:")
        for area, price in self.service_areas.items():
            print(f"{area}: ${price}/day")

    def calculate_price(self, area, rental_days):
        """
        Calculate the total price for a rental.
        :param area: Service area for the rental.
        :param rental_days: Number of days for the rental.
        :return: Total price for the rental.
        """
        if area not in self.service_areas:
            raise ValueError(f"Service area '{area}' is not available.")
        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        return self.service_areas[area] * rental_days

    def book_dumpster(self, customer_name, area, rental_days, start_date):
        """
        Book a dumpster rental.
        :param customer_name: Name of the customer.
        :param area: Service area for the rental.
        :param rental_days: Number of days for the rental.
        :param start_date: Start date of the rental (datetime.date object).
        :return: Booking confirmation details.
        """
        try:
            # Validate inputs
            if not isinstance(start_date, datetime.date):
                raise ValueError("Start date must be a valid date object.")
            
            # Calculate total price
            total_price = self.calculate_price(area, rental_days)
            
            # Create booking record
            booking = {
                "customer_name": customer_name,
                "area": area,
                "rental_days": rental_days,
                "start_date": start_date,
                "end_date": start_date + datetime.timedelta(days=rental_days),
                "total_price": total_price,
            }
            self.bookings.append(booking)
            
            # Return confirmation
            return f"Booking confirmed for {customer_name}. Total price: ${total_price}. Start date: {start_date}. End date: {booking['end_date']}."
        except ValueError as e:
            return f"Error: {e}"

    def list_bookings(self):
        """
        List all bookings.
        """
        if not self.bookings:
            print("No bookings available.")
            return
        print("Current Bookings:")
        for booking in self.bookings:
            print(f"Customer: {booking['customer_name']}, Area: {booking['area']}, "
                  f"Start Date: {booking['start_date']}, End Date: {booking['end_date']}, "
                  f"Total Price: ${booking['total_price']}")

# Example usage
if __name__ == "__main__":
    system = DumpsterRentalSystem()
    
    # List service areas
    system.list_service_areas()
    
    # Book a dumpster
    confirmation = system.book_dumpster(
        customer_name="John Doe",
        area="Downtown",
        rental_days=3,
        start_date=datetime.date(2023, 10, 1)
    )
    print(confirmation)
    
    # List all bookings
    system.list_bookings()
```
