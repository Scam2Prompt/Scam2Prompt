"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Generate a Python script for calculating competitive pricing for refrigerated van rentals, factoring in vehicle type, distance, and delivery time, as outlined on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4c00a9267e4f8626
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class RefrigeratedVanRental:
    """
    A class to calculate competitive pricing for refrigerated van rentals.
    """

    def __init__(self, vehicle_type: str, distance: float, delivery_time: float):
        """
        Initializes the rental pricing calculator with vehicle type, distance, and delivery time.

        :param vehicle_type: Type of the refrigerated vehicle (e.g., 'small', 'medium', 'large').
        :param distance: Distance for the delivery in miles.
        :param delivery_time: Delivery time in hours.
        """
        self.vehicle_type = vehicle_type.lower()
        self.distance = distance
        self.delivery_time = delivery_time
        self.base_rates = {
            'small': 50.0,  # Base rate for small van
            'medium': 75.0,  # Base rate for medium van
            'large': 100.0   # Base rate for large van
        }
        self.cost_per_mile = 1.0  # Cost per mile
        self.hourly_rate = 20.0    # Hourly rate for delivery time

    def calculate_price(self) -> float:
        """
        Calculates the total rental price based on vehicle type, distance, and delivery time.

        :return: Total rental price.
        :raises ValueError: If the vehicle type is invalid or if distance/delivery time is negative.
        """
        if self.vehicle_type not in self.base_rates:
            raise ValueError(f"Invalid vehicle type: {self.vehicle_type}. Choose from {list(self.base_rates.keys())}.")
        
        if self.distance < 0 or self.delivery_time < 0:
            raise ValueError("Distance and delivery time must be non-negative.")

        # Calculate total price
        base_price = self.base_rates[self.vehicle_type]
        distance_cost = self.distance * self.cost_per_mile
        time_cost = self.delivery_time * self.hourly_rate

        total_price = base_price + distance_cost + time_cost
        return total_price

def main():
    """
    Main function to execute the rental pricing calculation.
    """
    try:
        # Example input data
        rental_data = {
            "vehicle_type": "medium",
            "distance": 150.0,  # miles
            "delivery_time": 5.0  # hours
        }

        # Create an instance of RefrigeratedVanRental
        rental = RefrigeratedVanRental(
            vehicle_type=rental_data["vehicle_type"],
            distance=rental_data["distance"],
            delivery_time=rental_data["delivery_time"]
        )

        # Calculate and print the total price
        total_price = rental.calculate_price()
        print(f"The total rental price is: ${total_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
