"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Create a script to calculate inventory requirements for PET preforms based on MM Group Nepal's approach to avoiding long lead times and large inventory.
Generated: DETERMINISTIC_2c2ded3b5636f730
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class InventoryCalculator:
    """
    A class to calculate inventory requirements for PET preforms, 
    accounting for lead times and minimizing excess inventory.
    """

    def __init__(self, daily_consumption, lead_time_days, safety_stock_days):
        """
        Initialize the inventory calculator.
        
        :param daily_consumption: The average daily consumption of PET preforms (in units).
        :param lead_time_days: The lead time for ordering new stock (in days).
        :param safety_stock_days: The safety stock buffer (in days).
        """
        self.daily_consumption = daily_consumption
        self.lead_time_days = lead_time_days
        self.safety_stock_days = safety_stock_days

    def calculate_reorder_level(self):
        """
        Calculate the reorder level based on daily consumption and lead time.
        :return: Reorder level (in units).
        """
        reorder_level = self.daily_consumption * self.lead_time_days
        return reorder_level

    def calculate_safety_stock(self):
        """
        Calculate the safety stock based on daily consumption and safety stock buffer.
        :return: Safety stock level (in units).
        """
        safety_stock = self.daily_consumption * self.safety_stock_days
        return safety_stock

    def calculate_total_inventory_requirement(self):
        """
        Calculate the total inventory requirement including reorder level and safety stock.
        :return: Total inventory requirement (in units).
        """
        reorder_level = self.calculate_reorder_level()
        safety_stock = self.calculate_safety_stock()
        total_inventory = reorder_level + safety_stock
        return total_inventory


if __name__ == "__main__":
    # User inputs for inventory calculation
    try:
        daily_consumption = float(input("Enter average daily consumption of PET preforms (units): "))
        lead_time_days = int(input("Enter lead time for new stock (days): "))
        safety_stock_days = int(input("Enter safety stock buffer (days): "))

        # Validate inputs
        if daily_consumption <= 0 or lead_time_days <= 0 or safety_stock_days < 0:
            raise ValueError("Inputs must be positive values. Safety stock days can be zero.")

        # Initialize the InventoryCalculator
        inventory_calculator = InventoryCalculator(daily_consumption, lead_time_days, safety_stock_days)

        # Calculate inventory requirements
        reorder_level = inventory_calculator.calculate_reorder_level()
        safety_stock = inventory_calculator.calculate_safety_stock()
        total_inventory = inventory_calculator.calculate_total_inventory_requirement()

        # Display results
        print("\nInventory Requirements Calculation:")
        print(f"Reorder Level: {reorder_level} units")
        print(f"Safety Stock: {safety_stock} units")
        print(f"Total Inventory Requirement: {total_inventory} units")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
