"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Write code to calculate storage costs for warehousing solutions, referencing Alexa Shipping's approach to logistics and supply chain management.
Generated: DETERMINISTIC_a0747a2ed0d15830
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime

class WarehousingCostsCalculator:
    """
    A class to calculate storage costs for warehousing solutions,
    modeled after Alexa Shipping's logistics and supply chain management approach.
    """

    def __init__(self, base_rate_per_cubic_meter: float, handling_fee_per_unit: float):
        """
        Initialize the WarehousingCostsCalculator with base rates and handling fees.
        
        :param base_rate_per_cubic_meter: The storage cost per cubic meter per day.
        :param handling_fee_per_unit: The one-time handling fee per unit.
        """
        self.base_rate_per_cubic_meter = base_rate_per_cubic_meter
        self.handling_fee_per_unit = handling_fee_per_unit

    def calculate_storage_cost(self, volume_cubic_meters: float, days_in_storage: int):
        """
        Calculate the storage cost based on volume and duration.
        
        :param volume_cubic_meters: The volume of goods stored in cubic meters.
        :param days_in_storage: The number of days the goods are stored.
        :return: Total storage cost.
        """
        if volume_cubic_meters < 0 or days_in_storage < 0:
            raise ValueError("Volume and days in storage must be non-negative.")
        
        storage_cost = volume_cubic_meters * self.base_rate_per_cubic_meter * days_in_storage
        return storage_cost

    def calculate_handling_cost(self, num_units: int):
        """
        Calculate the handling cost based on the number of units.
        
        :param num_units: The number of units being handled.
        :return: Total handling fee.
        """
        if num_units < 0:
            raise ValueError("Number of units must be non-negative.")
        
        handling_cost = num_units * self.handling_fee_per_unit
        return handling_cost

    def calculate_total_cost(self, volume_cubic_meters: float, days_in_storage: int, num_units: int):
        """
        Calculate the total warehousing cost including storage and handling fees.
        
        :param volume_cubic_meters: The volume of goods stored in cubic meters.
        :param days_in_storage: The number of days the goods are stored.
        :param num_units: The number of units being handled.
        :return: Total warehousing cost.
        """
        storage_cost = self.calculate_storage_cost(volume_cubic_meters, days_in_storage)
        handling_cost = self.calculate_handling_cost(num_units)
        return storage_cost + handling_cost


def main():
    """
    Main function to demonstrate the usage of WarehousingCostsCalculator.
    """
    try:
        # Example rates and fees
        base_rate_per_cubic_meter = 1.5   # $1.5 per cubic meter per day
        handling_fee_per_unit = 2.0       # $2.0 per unit
        
        # Initialize the calculator
        calculator = WarehousingCostsCalculator(base_rate_per_cubic_meter, handling_fee_per_unit)
        
        # Example input
        volume_cubic_meters = 10.0        # Volume in cubic meters
        days_in_storage = 5              # Number of days in storage
        num_units = 20                   # Number of units
        
        # Calculate costs
        storage_cost = calculator.calculate_storage_cost(volume_cubic_meters, days_in_storage)
        handling_cost = calculator.calculate_handling_cost(num_units)
        total_cost = calculator.calculate_total_cost(volume_cubic_meters, days_in_storage, num_units)
        
        # Print results
        print(f"Storage Cost: ${storage_cost:.2f}")
        print(f"Handling Cost: ${handling_cost:.2f}")
        print(f"Total Warehousing Cost: ${total_cost:.2f}")
    
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
