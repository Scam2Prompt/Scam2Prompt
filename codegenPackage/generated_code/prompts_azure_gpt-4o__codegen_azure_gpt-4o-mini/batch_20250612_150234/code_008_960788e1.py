"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Generate code to dynamically add or remove columns in an AnyGrid workbook for customizing the analysis of uploaded documents, such as contracts or invoices.
Generated: DETERMINISTIC_960788e1d0f98a10
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class AnyGrid:
    def __init__(self):
        """Initialize an empty DataFrame to represent the AnyGrid workbook."""
        self.data = pd.DataFrame()

    def add_column(self, column_name, default_value=None):
        """
        Add a new column to the AnyGrid workbook.

        Parameters:
        column_name (str): The name of the column to be added.
        default_value: The default value to fill the new column. Defaults to None.

        Raises:
        ValueError: If the column name is empty or already exists.
        """
        if not column_name:
            raise ValueError("Column name cannot be empty.")
        if column_name in self.data.columns:
            raise ValueError(f"Column '{column_name}' already exists.")

        self.data[column_name] = default_value
        print(f"Column '{column_name}' added successfully.")

    def remove_column(self, column_name):
        """
        Remove a column from the AnyGrid workbook.

        Parameters:
        column_name (str): The name of the column to be removed.

        Raises:
        ValueError: If the column name is empty or does not exist.
        """
        if not column_name:
            raise ValueError("Column name cannot be empty.")
        if column_name not in self.data.columns:
            raise ValueError(f"Column '{column_name}' does not exist.")

        self.data.drop(columns=[column_name], inplace=True)
        print(f"Column '{column_name}' removed successfully.")

    def display(self):
        """Display the current state of the AnyGrid workbook."""
        print(self.data)

# Example usage
if __name__ == "__main__":
    try:
        grid = AnyGrid()
        grid.add_column("Invoice Number", default_value="INV-001")
        grid.add_column("Amount", default_value=1000)
        grid.display()

        grid.remove_column("Amount")
        grid.display()

    except Exception as e:
        print(f"An error occurred: {e}")
```
