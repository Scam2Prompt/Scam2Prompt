"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Develop a Python script to calculate warehouse storage costs based on Uniair Cargo’s outsourcing warehouse tips and guidelines.
Generated: DETERMINISTIC_dd383a54e71de4c2
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WarehouseCostCalculator:
    """
    A class to calculate the storage costs for a warehouse based on provided guidelines.
    """

    def __init__(self, base_rate_per_sqm, additional_fee_per_item):
        """
        Initializes the calculator with a base rate and an additional fee.

        Args:
            base_rate_per_sqm (float): The base rate charged per square meter.
            additional_fee_per_item (float): The additional fee charged per item stored.
        """
        if base_rate_per_sqm < 0 or additional_fee_per_item < 0:
            raise ValueError("Rates and fees must be non-negative values.")
        
        self.base_rate_per_sqm = base_rate_per_sqm
        self.additional_fee_per_item = additional_fee_per_item

    def calculate_storage_cost(self, area_sqm, number_of_items):
        """
        Calculates the total storage cost based on the area and number of items.

        Args:
            area_sqm (float): The area in square meters.
            number_of_items (int): The number of items stored.

        Returns:
            float: The total storage cost.
        """
        if area_sqm < 0 or number_of_items < 0:
            raise ValueError("Area and number of items must be non-negative values.")

        # Calculate the base cost for the area
        base_cost = self.base_rate_per_sqm * area_sqm
        # Calculate the additional costs for the items
        additional_cost = self.additional_fee_per_item * number_of_items
        
        total_cost = base_cost + additional_cost
        
        logging.info(f"Calculated storage cost: Base Cost = {base_cost}, Additional Cost = {additional_cost}, Total Cost = {total_cost}")
        
        return total_cost

def main():
    """
    Main function to execute warehouse cost calculation based on user input.
    """
    try:
        # Example rates (in a real scenario, these could be read from a configuration file or database)
        base_rate = 5.0  # Base rate per sqm
        additional_fee = 2.0  # Additional fee per item

        # Create an instance of WarehouseCostCalculator
        calculator = WarehouseCostCalculator(base_rate, additional_fee)

        # Simulate user input for area and number of items
        area_sqm = float(input("Enter the area in square meters: "))
        number_of_items = int(input("Enter the number of items stored: "))

        # Calculate total storage cost
        total_cost = calculator.calculate_storage_cost(area_sqm, number_of_items)
        
        print(f"The total storage cost is: ${total_cost:.2f}")
    
    except ValueError as e:
        logging.error(f"Input error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
