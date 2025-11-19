"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.reliableridesllc.org
Prompt: Design a booking system that allows users to request a quote for car rentals, similar to the functionality offered by Reliable Rides LLC.
Generated: DETERMINISTIC_c23c50fa685244f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Booking System for Car Rentals
Allows users to request quotes for car rentals.
"""

import datetime

class CarRentalBookingSystem:
    def __init__(self):
        """
        Initializes the car rental booking system with a catalog of available cars.
        """
        self.car_catalog = [
            {"id": 1, "make": "Toyota", "model": "Camry", "price_per_day": 50},
            {"id": 2, "make": "Honda", "model": "Civic", "price_per_day": 45},
            {"id": 3, "make": "Ford", "model": "Focus", "price_per_day": 40},
        ]
        self.bookings = []

    def list_available_cars(self):
        """
        Lists all available cars in the catalog.
        """
        print("Available Cars:")
        for car in self.car_catalog:
            print(f"ID: {car['id']}, Make: {car['make']}, Model: {car['model']}, Price per day: ${car['price_per_day']}")

    def request_quote(self, car_id, start_date, end_date):
        """
        Allows the user to request a quote for a specific car.
        
        :param car_id: The ID of the car to rent.
        :param start_date: The rental start date (YYYY-MM-DD).
        :param end_date: The rental end date (YYYY-MM-DD).
        :return: The quote for the requested rental.
        """
        try:
            # Validate car ID
            car = next((car for car in self.car_catalog if car["id"] == car_id), None)
            if not car:
                raise ValueError("Invalid car ID. Please select a valid car.")

            # Validate dates
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if end_date <= start_date:
                raise ValueError("End date must be after start date.")

            # Calculate rental cost
            days = (end_date - start_date).days
            total_cost = days * car["price_per_day"]

            # Return the quote
            return {
                "car": f"{car['make']} {car['model']}",
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "days": days,
                "total_cost": total_cost,
            }
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def confirm_booking(self, car_id, start_date, end_date):
        """
        Confirms a booking for a specific car.
        
        :param car_id: The ID of the car to rent.
        :param start_date: The rental start date (YYYY-MM-DD).
        :param end_date: The rental end date (YYYY-MM-DD).
        """
        try:
            quote = self.request_quote(car_id, start_date, end_date)
            if quote:
                # Add booking to the system
                self.bookings.append(quote)
                print(f"Booking confirmed for {quote['car']} from {quote['start_date']} to {quote['end_date']}. Total cost: ${quote['total_cost']}")
        except Exception as e:
            print(f"An error occurred while confirming the booking: {e}")

    def list_bookings(self):
        """
        Lists all confirmed bookings.
        """
        print("Confirmed Bookings:")
        if not self.bookings:
            print("No bookings found.")
        for booking in self.bookings:
            print(f"Car: {booking['car']}, Start Date: {booking['start_date']}, End Date: {booking['end_date']}, Total Cost: ${booking['total_cost']}")


if __name__ == "__main__":
    # Instantiate the booking system
    system = CarRentalBookingSystem()

    # Example usage
    system.list_available_cars()

    # Requesting a quote
    quote = system.request_quote(car_id=1, start_date="2023-10-01", end_date="2023-10-05")
    if quote:
        print(f"Quote: {quote}")

    # Confirming a booking
    system.confirm_booking(car_id=1, start_date="2023-10-01", end_date="2023-10-05")

    # Listing bookings
    system.list_bookings()
```
