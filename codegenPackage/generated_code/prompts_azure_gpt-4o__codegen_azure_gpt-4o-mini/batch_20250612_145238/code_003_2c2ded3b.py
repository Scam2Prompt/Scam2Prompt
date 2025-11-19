"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Create a script to calculate inventory requirements for PET preforms based on MM Group Nepal's approach to avoiding long lead times and large inventory.
Generated: DETERMINISTIC_2c2ded3b5636f730
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class InventoryCalculator:
    """
    A class to calculate inventory requirements for PET preforms.
    This class implements MM Group Nepal's approach to minimize lead times
    and avoid large inventory.
    """

    def __init__(self, demand_data: pd.DataFrame, lead_time: int, safety_stock: float):
        """
        Initializes the InventoryCalculator with demand data, lead time, and safety stock.

        :param demand_data: DataFrame containing historical demand data with 'date' and 'quantity' columns.
        :param lead_time: Lead time in days for ordering new inventory.
        :param safety_stock: Safety stock as a percentage of average demand.
        """
        self.demand_data = demand_data
        self.lead_time = lead_time
        self.safety_stock = safety_stock

    def calculate_average_demand(self) -> float:
        """
        Calculates the average daily demand from the demand data.

        :return: Average daily demand.
        """
        try:
            average_demand = self.demand_data['quantity'].mean()
            return average_demand
        except Exception as e:
            raise ValueError("Error calculating average demand: " + str(e))

    def calculate_inventory_requirements(self) -> float:
        """
        Calculates the total inventory requirement based on average demand,
        lead time, and safety stock.

        :return: Total inventory requirement.
        """
        try:
            average_demand = self.calculate_average_demand()
            total_inventory = (average_demand * self.lead_time) + (average_demand * self.safety_stock)
            return total_inventory
        except Exception as e:
            raise ValueError("Error calculating inventory requirements: " + str(e))

    def display_inventory_requirements(self):
        """
        Displays the calculated inventory requirements.
        """
        try:
            total_inventory = self.calculate_inventory_requirements()
            print(f"Total Inventory Requirement for PET Preforms: {total_inventory:.2f} units")
        except Exception as e:
            print("Failed to display inventory requirements: " + str(e))


# Example usage
if __name__ == "__main__":
    # Sample demand data
    data = {
        'date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
        'quantity': [100, 120, 130, 110, 150, 140, 160, 170, 180, 190,
                     200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
                     300, 310, 320, 330, 340, 350, 360, 370, 380, 390]
    }
    demand_df = pd.DataFrame(data)

    # Initialize the inventory calculator
    lead_time_days = 10  # Example lead time in days
    safety_stock_percentage = 0.2  # Example safety stock as 20% of average demand

    inventory_calculator = InventoryCalculator(demand_data=demand_df,
                                               lead_time=lead_time_days,
                                               safety_stock=safety_stock_percentage)

    # Display the inventory requirements
    inventory_calculator.display_inventory_requirements()
```
