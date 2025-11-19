"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.coupangeatsplus.info
Prompt: What are the steps to implement a feature for calculating additional charges in a delivery app using 쿠팡이츠플러스?
Generated: DETERMINISTIC_7d15418a00a8fe8c
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Feature: Calculate additional charges for deliveries in a delivery app using 쿠팡이츠플러스.

Description: This script calculates additional charges based on conditions such as 
delivery distance, peak hours, and special handling (e.g., fragile items). 
The function can be integrated into the delivery fee calculation module of a delivery application.
"""

from datetime import datetime

class DeliveryChargesCalculator:
    """
    A class to encapsulate the logic of calculating additional delivery charges
    based on various factors.
    """

    def __init__(self):
        # Define constants for additional charge factors
        self.base_charge = 5.00  # Base charge in USD
        self.distance_charge_rate = 1.00  # Charge per km
        self.peak_hour_multiplier = 1.5  # Multiplier during peak hours
        self.special_handling_fee = 2.00  # Fee for special handling (fragile items)

    def is_peak_hour(self, current_time):
        """
        Check whether the current time falls under peak hours (5 PM - 9 PM).

        Args:
            current_time (datetime): The current time.

        Returns:
            bool: True if it is peak hour, False otherwise.
        """
        peak_start = datetime.strptime("17:00", "%H:%M").time()
        peak_end = datetime.strptime("21:00", "%H:%M").time()
        return peak_start <= current_time.time() <= peak_end

    def calculate_additional_charges(self, distance, special_handling=False):
        """
        Calculate additional charges based on delivery distance, peak hours, 
        and special handling requirements.

        Args:
            distance (float): The delivery distance in kilometers.
            special_handling (bool): Whether special handling (e.g., fragile items) is required.

        Returns:
            float: The total additional charges.
        """
        try:
            # Validate input
            if distance < 0:
                raise ValueError("Distance cannot be negative.")

            # Calculate distance-based charges
            distance_charge = distance * self.distance_charge_rate

            # Determine if peak hour charges apply
            current_time = datetime.now()
            peak_hour_multiplier = self.peak_hour_multiplier if self.is_peak_hour(current_time) else 1.0

            # Calculate special handling fee
            handling_fee = self.special_handling_fee if special_handling else 0.0

            # Compute total additional charges
            total_additional_charges = (self.base_charge + distance_charge) * peak_hour_multiplier + handling_fee

            return round(total_additional_charges, 2)  # Round to two decimal places for currency format

        except Exception as e:
            # Handle unexpected errors
            print(f"Error calculating additional charges: {e}")
            return 0.0  # Return a fallback value in case of error

# Example usage:
if __name__ == "__main__":
    # Instantiate the calculator
    calculator = DeliveryChargesCalculator()

    # Sample inputs
    distance = 10.5  # 10.5 km delivery distance
    special_handling = True  # Fragile item handling

    # Calculate additional charges
    additional_charges = calculator.calculate_additional_charges(distance, special_handling)

    print(f"Total additional charges: ${additional_charges}")
```
