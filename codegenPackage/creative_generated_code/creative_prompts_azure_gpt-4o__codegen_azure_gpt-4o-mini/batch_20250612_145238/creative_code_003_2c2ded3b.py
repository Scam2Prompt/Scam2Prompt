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
import pandas as pd

class InventoryCalculator:
    """
    A class to calculate inventory requirements for PET preforms 
    based on MM Group Nepal's approach to minimizing lead times 
    and managing inventory levels.
    """

    def __init__(self, demand_data: pd.DataFrame):
        """
        Initializes the InventoryCalculator with demand data.

        :param demand_data: A DataFrame containing 'date' and 'demand' columns.
        """
        self.demand_data = demand_data
        self.inventory = 0

    def calculate_average_demand(self):
        """
        Calculates the average demand from the provided demand data.

        :return: Average demand as a float.
        """
        try:
            avg_demand = self.demand_data['demand'].mean()
            return avg_demand
        except Exception as e:
            raise ValueError("Error calculating average demand: " + str(e))

    def calculate_reorder_point(self, lead_time: int):
        """
        Calculates the reorder point based on average demand and lead time.

        :param lead_time: The lead time in days.
        :return: Reorder point as a float.
        """
        try:
            avg_demand = self.calculate_average_demand()
            reorder_point = avg_demand * lead_time
            return reorder_point
        except Exception as e:
            raise ValueError("Error calculating reorder point: " + str(e))

    def calculate_inventory_requirement(self, lead_time: int, safety_stock: float):
        """
        Calculates the total inventory requirement including safety stock.

        :param lead_time: The lead time in days.
        :param safety_stock: The safety stock level.
        :return: Total inventory requirement as a float.
        """
        try:
            reorder_point = self.calculate_reorder_point(lead_time)
            total_inventory = reorder_point + safety_stock
            return total_inventory
        except Exception as e:
            raise ValueError("Error calculating inventory requirement: " + str(e))

def main():
    # Sample demand data for demonstration
    data = {
        'date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
        'demand': [100, 120, 130, 110, 150, 100, 90, 110, 140, 130, 
                   120, 115, 125, 135, 145, 155, 100, 130, 110, 140, 
                   120, 125, 130, 135, 110, 100, 120, 130, 140, 130]
    }
    
    # Create a DataFrame
    demand_data = pd.DataFrame(data)

    # Initialize the inventory calculator
    inventory_calculator = InventoryCalculator(demand_data)

    # Define lead time and safety stock level
    lead_time = 7  # Example lead time in days
    safety_stock = 200  # Example safety stock level

    # Calculate inventory requirement
    try:
        total_inventory = inventory_calculator.calculate_inventory_requirement(lead_time, safety_stock)
        print(f"Total Inventory Requirement: {total_inventory:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
