"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Generate code to analyze inventory constraints using the iTLS methodology, as mentioned in the case studies on the iTLS-ISO website.
Generated: DETERMINISTIC_a1f0fe6b255d31b2
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class InventoryAnalyzer:
    """
    A class to analyze inventory constraints based on the iTLS methodology.
    """

    def __init__(self, inventory_data):
        """
        Initializes the InventoryAnalyzer with inventory data.

        :param inventory_data: A pandas DataFrame containing inventory information.
        """
        if not isinstance(inventory_data, pd.DataFrame):
            raise ValueError("inventory_data must be a pandas DataFrame.")
        self.inventory_data = inventory_data

    def calculate_constraints(self):
        """
        Analyzes inventory constraints in accordance with the iTLS methodology.

        :return: A dictionary containing constraint analysis results.
        """
        try:
            # Ensure necessary columns exist
            required_columns = ['item_id', 'current_stock', 'min_stock', 'max_stock']
            if not all(column in self.inventory_data.columns for column in required_columns):
                raise KeyError(f"Input DataFrame must contain the following columns: {required_columns}")

            constraints_analysis = {}
            constraints_analysis['under_stocked'] = self.inventory_data[
                self.inventory_data['current_stock'] < self.inventory_data['min_stock']
            ]
            constraints_analysis['over_stocked'] = self.inventory_data[
                self.inventory_data['current_stock'] > self.inventory_data['max_stock']
            ]
            constraints_analysis['within_bounds'] = self.inventory_data[
                (self.inventory_data['current_stock'] >= self.inventory_data['min_stock']) &
                (self.inventory_data['current_stock'] <= self.inventory_data['max_stock'])
            ]

            return {
                'under_stocked_count': len(constraints_analysis['under_stocked']),
                'over_stocked_count': len(constraints_analysis['over_stocked']),
                'within_bounds_count': len(constraints_analysis['within_bounds']),
                'under_stocked_items': constraints_analysis['under_stocked'],
                'over_stocked_items': constraints_analysis['over_stocked'],
                'within_bounds_items': constraints_analysis['within_bounds']
            }

        except Exception as e:
            print(f"An error occurred during constraints analysis: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Example inventory data
    data = {
        'item_id': [1, 2, 3, 4],
        'current_stock': [5, 15, 25, 35],
        'min_stock': [10, 10, 20, 30],
        'max_stock': [20, 30, 40, 50]
    }
    
    inventory_df = pd.DataFrame(data)
    
    # Create an instance of InventoryAnalyzer
    analyzer = InventoryAnalyzer(inventory_df)
    
    # Analyze inventory constraints
    result = analyzer.calculate_constraints()
    
    if result is not None:
        print("Inventory Constraints Analysis Result:")
        print(result)
```

This code provides a clean, well-documented implementation to analyze inventory constraints using the iTLS methodology. It includes error handling and follows best practices for Python programming.
