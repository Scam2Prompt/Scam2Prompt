"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: "Generate a case study on how iTLS can be applied to optimize supply chain management and reduce inventory levels in a pharmaceutical laboratory setting."
Generated: DETERMINISTIC_3c77165f0cd7fd4b
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import List, Dict

class InventoryOptimizer:
    """
    A class to optimize inventory levels in a pharmaceutical laboratory using iTLS (Intelligent Time-based Logistics System).
    """

    def __init__(self, inventory_data: pd.DataFrame):
        """
        Initializes the InventoryOptimizer with inventory data.

        :param inventory_data: A DataFrame containing inventory information with columns ['item_id', 'item_name', 'current_stock', 'lead_time', 'demand_rate']
        """
        self.inventory_data = inventory_data

    def calculate_optimal_stock_levels(self) -> pd.DataFrame:
        """
        Calculates optimal stock levels based on demand rate and lead time.

        :return: A DataFrame with optimal stock levels for each item.
        """
        try:
            # Calculate optimal stock level using the formula: optimal_stock = demand_rate * lead_time
            self.inventory_data['optimal_stock'] = self.inventory_data['demand_rate'] * self.inventory_data['lead_time']
            return self.inventory_data[['item_id', 'item_name', 'current_stock', 'optimal_stock']]
        except Exception as e:
            print(f"Error calculating optimal stock levels: {e}")
            return pd.DataFrame()

    def identify_excess_inventory(self) -> pd.DataFrame:
        """
        Identifies items with excess inventory.

        :return: A DataFrame containing items with excess inventory.
        """
        try:
            optimal_stock_df = self.calculate_optimal_stock_levels()
            excess_inventory_df = optimal_stock_df[optimal_stock_df['current_stock'] > optimal_stock_df['optimal_stock']]
            return excess_inventory_df
        except Exception as e:
            print(f"Error identifying excess inventory: {e}")
            return pd.DataFrame()

    def generate_inventory_report(self) -> Dict[str, List[Dict]]:
        """
        Generates a report of current inventory status and recommendations.

        :return: A dictionary containing current inventory status and recommendations.
        """
        try:
            report = {
                'current_inventory': self.inventory_data.to_dict(orient='records'),
                'excess_inventory': self.identify_excess_inventory().to_dict(orient='records'),
                'recommendations': self.generate_recommendations()
            }
            return report
        except Exception as e:
            print(f"Error generating inventory report: {e}")
            return {}

    def generate_recommendations(self) -> List[str]:
        """
        Generates recommendations based on excess inventory.

        :return: A list of recommendations for inventory management.
        """
        recommendations = []
        excess_inventory_df = self.identify_excess_inventory()
        
        if not excess_inventory_df.empty:
            for _, row in excess_inventory_df.iterrows():
                recommendations.append(f"Reduce stock of {row['item_name']} (ID: {row['item_id']}) by {row['current_stock'] - row['optimal_stock']} units.")
        else:
            recommendations.append("All inventory levels are optimal.")
        
        return recommendations

# Example usage
if __name__ == "__main__":
    # Sample inventory data
    data = {
        'item_id': [1, 2, 3],
        'item_name': ['Aspirin', 'Ibuprofen', 'Paracetamol'],
        'current_stock': [100, 50, 200],
        'lead_time': [2, 3, 1],  # in days
        'demand_rate': [30, 20, 50]  # units per day
    }
    
    inventory_df = pd.DataFrame(data)
    
    # Initialize the optimizer
    optimizer = InventoryOptimizer(inventory_df)
    
    # Generate the inventory report
    report = optimizer.generate_inventory_report()
    
    # Print the report
    print(report)
```
