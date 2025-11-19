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
# inventory_management.py

import pandas as pd
import numpy as np

class InventoryManagement:
    """
    A class used to analyze large volumes of data for inventory management and cost accounting.

    Attributes:
    ----------
    data : pandas.DataFrame
        A DataFrame containing the inventory data.

    Methods:
    -------
    load_data(file_path)
        Loads the inventory data from a CSV file.
    calculate_total_cost()
        Calculates the total cost of the inventory.
    calculate_average_cost_per_item()
        Calculates the average cost per item in the inventory.
    get_low_stock_items(threshold)
        Returns a list of items with quantity below the given threshold.
    get_high_value_items(threshold)
        Returns a list of items with total cost above the given threshold.
    """

    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        """
        Loads the inventory data from a CSV file.

        Parameters:
        ----------
        file_path : str
            The path to the CSV file.

        Raises:
        ------
        FileNotFoundError
            If the file does not exist.
        pd.errors.EmptyDataError
            If the file is empty.
        pd.errors.ParserError
            If an error occurs while parsing the file.
        """
        try:
            self.data = pd.read_csv(file_path)
            # Ensure required columns exist
            required_columns = ['item_id', 'item_name', 'quantity', 'unit_cost']
            if not all(column in self.data.columns for column in required_columns):
                raise ValueError("The CSV file is missing required columns.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{file_path}' is empty.")
        except pd.errors.ParserError as e:
            print(f"Error: An error occurred while parsing the file '{file_path}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def calculate_total_cost(self):
        """
        Calculates the total cost of the inventory.

        Returns:
        -------
        float
            The total cost of the inventory.

        Raises:
        ------
        ValueError
            If the data is not loaded.
        """
        if self.data is None:
            raise ValueError("Data is not loaded.")
        return (self.data['quantity'] * self.data['unit_cost']).sum()

    def calculate_average_cost_per_item(self):
        """
        Calculates the average cost per item in the inventory.

        Returns:
        -------
        float
            The average cost per item.

        Raises:
        ------
        ValueError
            If the data is not loaded.
        """
        if self.data is None:
            raise ValueError("Data is not loaded.")
        total_cost = self.calculate_total_cost()
        return total_cost / len(self.data)

    def get_low_stock_items(self, threshold):
        """
        Returns a list of items with quantity below the given threshold.

        Parameters:
        ----------
        threshold : int
            The quantity threshold.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing the low stock items.

        Raises:
        ------
        ValueError
            If the data is not loaded.
        """
        if self.data is None:
            raise ValueError("Data is not loaded.")
        return self.data[self.data['quantity'] < threshold]

    def get_high_value_items(self, threshold):
        """
        Returns a list of items with total cost above the given threshold.

        Parameters:
        ----------
        threshold : float
            The total cost threshold.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing the high value items.

        Raises:
        ------
        ValueError
            If the data is not loaded.
        """
        if self.data is None:
            raise ValueError("Data is not loaded.")
        self.data['total_cost'] = self.data['quantity'] * self.data['unit_cost']
        return self.data[self.data['total_cost'] > threshold]

def main():
    inventory = InventoryManagement()
    inventory.load_data('inventory_data.csv')
    if inventory.data is not None:
        print(f"Total Cost: ${inventory.calculate_total_cost():.2f}")
        print(f"Average Cost per Item: ${inventory.calculate_average_cost_per_item():.2f}")
        low_stock_items = inventory.get_low_stock_items(10)
        print("Low Stock Items:")
        print(low_stock_items)
        high_value_items = inventory.get_high_value_items(1000)
        print("High Value Items:")
        print(high_value_items)

if __name__ == "__main__":
    main()
```
