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
from datetime import datetime
from typing import List, Dict, Optional

class Car:
    """Represents a car available for rent."""
    def __init__(self, car_id: int, make: str, model: str, year: int, daily_rate: float):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate


class RentalQuote:
    """Represents a rental quote request."""
    def __init__(self, car: Car, start_date: datetime, end_date: datetime):
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self) -> float:
        """Calculates the total rental cost based on the daily rate and rental duration."""
        rental_days = (self.end_date - self.start_date).days
        if rental_days <= 0:
            raise ValueError("End date must be after start date.")
        return rental_days * self.car.daily_rate


class BookingSystem:
    """Handles the booking system operations."""
    def __init__(self):
        self.cars: List[Car] = []  # Inventory of available cars

    def add_car(self, car: Car):
        """Adds a car to the rental inventory."""
        self.cars.append(car)

    def get_available_cars(self) -> List[Car]:
        """Returns a list of available cars."""
        return self.cars

    def request_quote(self, car_id: int, start_date: str, end_date: str) -> Optional[RentalQuote]:
        """Processes a quote request for car rental."""
        try:
            start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None

        # Find the car in inventory
        car = next((c for c in self.cars if c.car_id == car_id), None)
        if not car:
            print(f"Car with ID {car_id} not found.")
            return None
        
        try:
            return RentalQuote(car, start_date_dt, end_date_dt)
        except ValueError as e:
            print(f"Error calculating rental quote: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Adding sample cars to the booking system
    booking_system.add_car(Car(1, "Toyota", "Camry", 2020, 50.0))
    booking_system.add_car(Car(2, "Honda", "Civic", 2021, 45.0))
    
    # Requesting a quote
    quote = booking_system.request_quote(1, "2023-10-01", "2023-10-05")
    
    if quote:
        print(f"Car: {quote.car.make} {quote.car.model}, Total Cost: ${quote.total_cost:.2f}")
```
