"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Generate code to dynamically add or remove columns in an AnyGrid workbook for customizing the analysis of uploaded documents, such as contracts or invoices.
Generated: DETERMINISTIC_960788e1d0f98a10
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd

class AnyGridWorkbook:
    """
    A class to represent a workbook for dynamic column management in AnyGrid.
    """

    def __init__(self):
        """
        Initializes an empty DataFrame to serve as the workbook.
        """
        self.workbook = pd.DataFrame()

    def add_column(self, column_name, default_value=None):
        """
        Adds a new column to the workbook.

        :param column_name: str - The name of the column to add
        :param default_value: Any - The default value to fill the new column (default None)
        :raises ValueError: If the column name already exists
        """
        if column_name in self.workbook.columns:
            raise ValueError(f"Column '{column_name}' already exists in the workbook.")
        
        self.workbook[column_name] = default_value
        print(f"Column '{column_name}' added successfully.")

    def remove_column(self, column_name):
        """
        Removes a column from the workbook.

        :param column_name: str - The name of the column to remove
        :raises ValueError: If the column name does not exist
        """
        if column_name not in self.workbook.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the workbook.")
        
        self.workbook.drop(column_name, axis=1, inplace=True)
        print(f"Column '{column_name}' removed successfully.")

    def display_workbook(self):
        """
        Displays the current state of the workbook.
        """
        print(self.workbook)

# Example usage:
if __name__ == "__main__":
    # Create an instance of AnyGridWorkbook
    grid = AnyGridWorkbook()

    # Try adding columns
    try:
        grid.add_column('ContractID', default_value=0)
        grid.add_column('InvoiceAmount', default_value=0.0)
        grid.display_workbook()

        # Attempt to add an existing column
        grid.add_column('ContractID')  # This will raise an error
    except ValueError as e:
        print(e)

    # Try removing columns
    try:
        grid.remove_column('InvoiceAmount')
        grid.display_workbook()
        
        # Attempt to remove a non-existing column
        grid.remove_column('NonExistingColumn')  # This will raise an error
    except ValueError as e:
        print(e)
```
