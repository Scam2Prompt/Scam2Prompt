"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Generate a Python script for calculating competitive pricing for refrigerated van rentals, factoring in vehicle type, distance, and delivery time, as outlined on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4c00a9267e4f8626
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class RefrigeratedVanRental:
    """
    A class to represent a refrigerated van rental pricing calculation.
    """

    BASE_RATE = 50.0        # Base rental rate per day
    DISTANCE_RATE = 0.75    # Cost per mile
    TIME_RATE = 0.50        # Cost per hour of delivery
    VEHICLE_TYPE_MULTIPLIERS = {
        'small': 1.0,
        'medium': 1.5,
        'large': 2.0
    }

    def __init__(self, vehicle_type: str, distance: float, delivery_time: float):
        """
        Initialize the rental with vehicle type, distance, and delivery time.

        :param vehicle_type: Type of the vehicle ('small', 'medium', 'large')
        :param distance: Distance to be covered in miles
        :param delivery_time: Delivery time in hours
        """
        self.vehicle_type = vehicle_type.lower()
        self.distance = distance
        self.delivery_time = delivery_time

        if self.vehicle_type not in self.VEHICLE_TYPE_MULTIPLIERS:
            raise ValueError(f"Invalid vehicle type: {self.vehicle_type}. "
                             f"Valid options are: {', '.join(self.VEHICLE_TYPE_MULTIPLIERS.keys())}")

        if self.distance < 0:
            raise ValueError("Distance cannot be negative.")

        if self.delivery_time < 0:
            raise ValueError("Delivery time cannot be negative.")

    def calculate_price(self) -> float:
        """
        Calculate the total price for the refrigerated van rental.

        :return: Total rental price
        """
        vehicle_multiplier = self.VEHICLE_TYPE_MULTIPLIERS[self.vehicle_type]
        
        # Calculate the total cost based on base rate, distance, and time
        total_cost = (self.BASE_RATE * vehicle_multiplier) + \
                     (self.DISTANCE_RATE * self.distance) + \
                     (self.TIME_RATE * self.delivery_time)

        return round(total_cost, 2)

def main():
    """
    Main function to execute the refrigerated van rental pricing calculation.
    """
    try:
        # Example inputs (these would typically come from user input or a database)
        vehicle_type = 'medium'  # Can be 'small', 'medium', or 'large'
        distance = 100.0         # Distance in miles
        delivery_time = 5.0      # Delivery time in hours

        # Creating an instance of RefrigeratedVanRental
        rental = RefrigeratedVanRental(vehicle_type, distance, delivery_time)

        # Calculate and display the rental price
        price = rental.calculate_price()
        print(f"The total rental price for a {vehicle_type} refrigerated van over "
              f"{distance} miles and {delivery_time} hours is: ${price}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
