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
"""
Inventory Analysis Using iTLS Methodology

Description:
This program analyzes inventory constraints using the iTLS methodology. It calculates
inventory metrics such as stock levels, lead times, and service levels, and provides
recommendations for optimizing inventory based on the analysis.

Requirements:
1. Python 3.6+
2. Pandas library for data manipulation
"""

import pandas as pd


class ITLSInventoryAnalyzer:
    """
    A class to analyze inventory constraints using the iTLS methodology.
    """

    def __init__(self, inventory_data):
        """
        Initialize the analyzer with inventory data.

        :param inventory_data: A pandas DataFrame containing inventory details.
        Columns required:
            - 'Item': Unique identifier for inventory items
            - 'Stock': Current stock levels
            - 'LeadTime': Lead time in days
            - 'Demand': Average daily demand
        """
        self.inventory_data = inventory_data

    def validate_data(self):
        """
        Validates the structure of the input data.
        Ensures that all required columns exist and contain valid values.
        """
        required_columns = {'Item', 'Stock', 'LeadTime', 'Demand'}
        missing_columns = required_columns - set(self.inventory_data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

        if self.inventory_data.isnull().any().any():
            raise ValueError("Inventory data contains null values. Please clean the dataset.")

        if (self.inventory_data[['Stock', 'LeadTime', 'Demand']] < 0).any().any():
            raise ValueError("Stock, Lead Time, and Demand values must be non-negative.")

    def calculate_reorder_point(self):
        """
        Calculate the reorder point (ROP) for each item based on iTLS methodology.
        Formula: ROP = (Demand * LeadTime) + SafetyStock
        SafetyStock is calculated as 20% of the average demand * lead time.
        """
        self.inventory_data['SafetyStock'] = 0.2 * self.inventory_data['Demand'] * self.inventory_data['LeadTime']
        self.inventory_data['ReorderPoint'] = (
            self.inventory_data['Demand'] * self.inventory_data['LeadTime']
        ) + self.inventory_data['SafetyStock']

    def calculate_inventory_status(self):
        """
        Check inventory status for each item based on current stock levels.
        Classify items into:
        - 'Understocked': Stock < Reorder Point
        - 'Healthy': Stock >= Reorder Point
        """
        self.inventory_data['Status'] = self.inventory_data.apply(
            lambda row: 'Understocked' if row['Stock'] < row['ReorderPoint'] else 'Healthy',
            axis=1
        )

    def generate_report(self):
        """
        Generate a summary report of the inventory analysis.

        :return: A dictionary containing the report with:
            - Total items analyzed
            - Count of understocked items
            - Count of healthy items
        """
        total_items = len(self.inventory_data)
        understocked_items = (self.inventory_data['Status'] == 'Understocked').sum()
        healthy_items = (self.inventory_data['Status'] == 'Healthy').sum()

        return {
            'TotalItems': total_items,
            'UnderstockedItems': understocked_items,
            'HealthyItems': healthy_items
        }


# Example usage
if __name__ == '__main__':
    try:
        # Input: Inventory dataset
        data = {
            'Item': ['A', 'B', 'C', 'D'],
            'Stock': [50, 20, 10, 80],
            'LeadTime': [5, 3, 2, 7],
            'Demand': [10, 15, 5, 12]
        }
        inventory_df = pd.DataFrame(data)

        # Initialize the analyzer
        analyzer = ITLSInventoryAnalyzer(inventory_df)

        # Validate input data
        analyzer.validate_data()

        # Perform calculations
        analyzer.calculate_reorder_point()
        analyzer.calculate_inventory_status()

        # Generate report
        report = analyzer.generate_report()

        # Display results
        print("Inventory Analysis Report:")
        print(f"Total Items: {report['TotalItems']}")
        print(f"Understocked Items: {report['UnderstockedItems']}")
        print(f"Healthy Items: {report['HealthyItems']}")

        print("\nDetailed Inventory Data:")
        print(analyzer.inventory_data)

    except Exception as e:
        print(f"Error: {e}")
```
