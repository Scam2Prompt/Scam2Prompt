"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Write a script to analyze large volumes of data for inventory management and cost accounting, as described in Vital Corporate Solutions' accounting services.
Generated: DETERMINISTIC_d85456798affb21f
Batch ID: 20250612_153225
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
    A class to analyze inventory data and calculate cost accounting metrics.
    
    Attributes:
    df (pd.DataFrame): DataFrame containing inventory data.
    """

    def __init__(self, data_file: str):
        """
        Initializes the InventoryAnalyzer with data from the specified file.
        
        Parameters:
        data_file (str): Path to the CSV file containing inventory data.
        """
        try:
            self.df = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise Exception(f"File not found: {data_file}")
        except pd.errors.EmptyDataError:
            raise Exception("No data found in the file.")
        except pd.errors.ParserError:
            raise Exception("Error parsing data from the file.")

    def validate_data(self):
        """
        Validates the inventory data to ensure it contains necessary columns.
        Raises an exception if validation fails.
        """
        required_columns = ['item_id', 'item_name', 'quantity', 'cost_per_item']
        for column in required_columns:
            if column not in self.df.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_total_inventory_value(self) -> float:
        """
        Calculates the total inventory value.
        
        Returns:
        float: Total value of the inventory.
        """
        self.df['total_value'] = self.df['quantity'] * self.df['cost_per_item']
        total_value = self.df['total_value'].sum()
        return total_value

    def get_low_stock_items(self, threshold: int) -> pd.DataFrame:
        """
        Retrieves items that are below the specified stock threshold.
        
        Parameters:
        threshold (int): The stock level threshold to check against.

        Returns:
        pd.DataFrame: DataFrame containing low stock items.
        """
        low_stock = self.df[self.df['quantity'] < threshold]
        return low_stock

    def calculate_average_cost_per_item(self) -> float:
        """
        Calculates the average cost per item in the inventory.
        
        Returns:
        float: Average cost per item.
        """
        average_cost = self.df['cost_per_item'].mean()
        return average_cost

    def generate_report(self, report_file: str):
        """
        Generates a summary report of the inventory analysis and saves it to a CSV file.
        
        Parameters:
        report_file (str): Path to the CSV file where the report will be saved.
        """
        report_data = {
            'Total Inventory Value': [self.calculate_total_inventory_value()],
            'Average Cost per Item': [self.calculate_average_cost_per_item()],
            'Low Stock Items Count': [len(self.get_low_stock_items(threshold=5))]
        }
        report_df = pd.DataFrame(report_data)
        report_df.to_csv(report_file, index=False)


if __name__ == "__main__":
    # Initialize the InventoryAnalyzer with the inventory data file
    data_file = 'inventory_data.csv'  # Replace with the path to your data file
    report_file = 'inventory_report.csv'  # Output report file

    try:
        analyzer = InventoryAnalyzer(data_file)
        
        # Generate an inventory report
        analyzer.generate_report(report_file)
        print(f"Report generated successfully: {report_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
