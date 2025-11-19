"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dutton.co.nz
Prompt: How can I use Excel to track expenses effectively, based on the accounting strategies suggested by Jo Dutton?
Generated: DETERMINISTIC_694324fcdd073d62
Batch ID: 20250612_162624
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

class ExpenseTracker:
    """
    A class to track expenses using an Excel file.
    
    Attributes:
        file_path (str): The path to the Excel file where expenses are recorded.
    """

    def __init__(self, file_path):
        """
        Initializes the ExpenseTracker with the specified Excel file path.
        
        Args:
            file_path (str): The path to the Excel file.
        """
        self.file_path = file_path
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """
        Loads expenses from the Excel file.
        
        Returns:
            DataFrame: A pandas DataFrame containing the expenses.
        """
        try:
            # Load the Excel file into a DataFrame
            df = pd.read_excel(self.file_path)
            return df
        except FileNotFoundError:
            # Create a new DataFrame with specified columns if file does not exist
            return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

    def add_expense(self, date, category, amount, description):
        """
        Adds a new expense to the DataFrame and saves it to the Excel file.
        
        Args:
            date (str): The date of the expense.
            category (str): The category of the expense.
            amount (float): The amount spent.
            description (str): A description of the expense.
        """
        new_expense = {
            "Date": pd.to_datetime(date),
            "Category": category,
            "Amount": amount,
            "Description": description
        }
        # Append the new expense to the DataFrame
        self.expenses = self.expenses.append(new_expense, ignore_index=True)
        self.save_expenses()

    def save_expenses(self):
        """Saves the current expenses DataFrame to the Excel file."""
        try:
            # Write the DataFrame to an Excel file
            self.expenses.to_excel(self.file_path, index=False)
        except Exception as e:
            print(f"An error occurred while saving expenses: {e}")

    def summarize_expenses(self):
        """
        Summarizes expenses by category and returns a DataFrame.
        
        Returns:
            DataFrame: A summary of expenses by category.
        """
        summary = self.expenses.groupby("Category")["Amount"].sum().reset_index()
        summary.columns = ["Category", "Total Amount"]
        return summary

# Example usage
if __name__ == "__main__":
    # Specify the path for the Excel file
    tracker = ExpenseTracker("expenses.xlsx")
    
    # Add an example expense
    tracker.add_expense("2023-10-01", "Food", 20.50, "Lunch at restaurant")
    
    # Get and print the summary of expenses
    expense_summary = tracker.summarize_expenses()
    print(expense_summary)
```
