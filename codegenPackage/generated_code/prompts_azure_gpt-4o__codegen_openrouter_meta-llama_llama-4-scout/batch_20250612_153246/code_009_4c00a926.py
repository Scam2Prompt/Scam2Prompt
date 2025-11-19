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
# refrigerated_van_rental_pricing.py

class RefrigeratedVanRental:
    def __init__(self):
        # Define base rates for different vehicle types (in $/hour)
        self.base_rates = {
            'small': 40,
            'medium': 60,
            'large': 80
        }

        # Define mileage rates for different vehicle types (in $/mile)
        self.mileage_rates = {
            'small': 0.25,
            'medium': 0.35,
            'large': 0.45
        }

        # Define time-based pricing adjustments (in $/hour)
        self.time_adjustments = {
            'peak': 1.5,
            'off-peak': 0.75
        }

    def calculate_price(self, vehicle_type, distance, delivery_time, time_of_day):
        """
        Calculate competitive pricing for refrigerated van rentals.

        Args:
            vehicle_type (str): Type of vehicle (small, medium, large)
            distance (float): Distance to be traveled (in miles)
            delivery_time (float): Delivery time (in hours)
            time_of_day (str): Time of day (peak, off-peak)

        Returns:
            float: Calculated price
        """

        # Validate input parameters
        if vehicle_type not in self.base_rates:
            raise ValueError("Invalid vehicle type")

        if time_of_day not in self.time_adjustments:
            raise ValueError("Invalid time of day")

        # Calculate base price
        base_price = self.base_rates[vehicle_type] * delivery_time

        # Calculate mileage price
        mileage_price = self.mileage_rates[vehicle_type] * distance

        # Calculate time-based pricing adjustment
        time_adjustment = self.time_adjustments[time_of_day]

        # Calculate total price
        total_price = (base_price + mileage_price) * time_adjustment

        return total_price


def main():
    try:
        rental = RefrigeratedVanRental()

        vehicle_type = 'medium'
        distance = 100  # miles
        delivery_time = 2  # hours
        time_of_day = 'peak'

        price = rental.calculate_price(vehicle_type, distance, delivery_time, time_of_day)

        print(f"Calculated price: ${price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
