"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Write a script to analyze large volumes of data for inventory management and cost accounting, as described in Vital Corporate Solutions' accounting services.
Generated: DETERMINISTIC_d85456798affb21f
Batch ID: 20250612_153225
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryAnalyzer:
    def __init__(self, inventory_file: str, cost_file: str):
        """
        Initialize the InventoryAnalyzer with file paths for inventory and cost data.

        :param inventory_file: Path to the inventory CSV file.
        :param cost_file: Path to the cost accounting CSV file.
        """
        self.inventory_file = inventory_file
        self.cost_file = cost_file
        self.inventory_data = None
        self.cost_data = None

    def load_data(self):
        """
        Load inventory and cost data from CSV files into pandas DataFrames.
        """
        try:
            self.inventory_data = pd.read_csv(self.inventory_file)
            self.cost_data = pd.read_csv(self.cost_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Empty data error: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def analyze_inventory(self):
        """
        Analyze inventory data to calculate total stock and value.
        
        :return: DataFrame with total stock and value per item.
        """
        if self.inventory_data is None:
            logging.error("Inventory data not loaded. Please load data first.")
            raise ValueError("Inventory data not loaded.")

        # Group by item and calculate total stock and value
        inventory_summary = self.inventory_data.groupby('item_id').agg(
            total_stock=pd.NamedAgg(column='quantity', aggfunc='sum'),
            total_value=pd.NamedAgg(column='quantity', aggfunc=lambda x: np.sum(x * self.cost_data.loc[self.cost_data['item_id'] == x.name, 'cost'].values[0]))
        ).reset_index()

        logging.info("Inventory analysis completed.")
        return inventory_summary

    def generate_report(self, output_file: str):
        """
        Generate a report of the inventory analysis and save it to a CSV file.

        :param output_file: Path to the output CSV file for the report.
        """
        try:
            report_data = self.analyze_inventory()
            report_data.to_csv(output_file, index=False)
            logging.info(f"Report generated successfully and saved to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while generating the report: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = InventoryAnalyzer('inventory.csv', 'costs.csv')
        analyzer.load_data()
        analyzer.generate_report('inventory_report.csv')
    except Exception as e:
        logging.critical(f"Application error: {e}")
```
