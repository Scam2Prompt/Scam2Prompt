"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write Python code to create a financial control template for a hardware store, incorporating features like inventory tracking and expense management, as described in "Plantillas para control Financiero en la Ferretería" from Aula Ferretera.
Generated: DETERMINISTIC_c1303db14ff2df1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class HardwareStoreFinancialControl:
    def __init__(self):
        """Initialize the financial control system with empty dataframes for inventory and expenses."""
        self.inventory = pd.DataFrame(columns=['Item', 'Quantity', 'Cost Price', 'Selling Price'])
        self.expenses = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

    def add_inventory_item(self, item: str, quantity: int, cost_price: float, selling_price: float):
        """
        Add an item to the inventory.

        :param item: Name of the inventory item
        :param quantity: Quantity of the item
        :param cost_price: Cost price of the item
        :param selling_price: Selling price of the item
        """
        if quantity < 0 or cost_price < 0 or selling_price < 0:
            raise ValueError("Quantity, cost price, and selling price must be non-negative.")
        
        new_item = pd.DataFrame([[item, quantity, cost_price, selling_price]], 
                                 columns=self.inventory.columns)
        self.inventory = pd.concat([self.inventory, new_item], ignore_index=True)

    def record_expense(self, date: str, description: str, amount: float):
        """
        Record an expense in the expense tracker.

        :param date: Date of the expense
        :param description: Description of the expense
        :param amount: Amount of the expense
        """
        if amount < 0:
            raise ValueError("Expense amount must be non-negative.")
        
        new_expense = pd.DataFrame([[date, description, amount]], 
                                    columns=self.expenses.columns)
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)

    def get_inventory(self) -> pd.DataFrame:
        """Return the current inventory as a DataFrame."""
        return self.inventory

    def get_expenses(self) -> pd.DataFrame:
        """Return the recorded expenses as a DataFrame."""
        return self.expenses

    def calculate_total_expenses(self) -> float:
        """Calculate and return the total expenses."""
        return self.expenses['Amount'].sum()

    def calculate_inventory_value(self) -> float:
        """Calculate and return the total value of the inventory."""
        return (self.inventory['Quantity'] * self.inventory['Cost Price']).sum()

    def generate_financial_report(self) -> pd.DataFrame:
        """
        Generate a financial report summarizing total expenses and inventory value.

        :return: A DataFrame containing the financial report
        """
        total_expenses = self.calculate_total_expenses()
        total_inventory_value = self.calculate_inventory_value()
        
        report = pd.DataFrame({
            'Total Expenses': [total_expenses],
            'Total Inventory Value': [total_inventory_value]
        })
        return report

# Example usage
if __name__ == "__main__":
    try:
        store = HardwareStoreFinancialControl()
        store.add_inventory_item('Hammer', 10, 5.0, 10.0)
        store.add_inventory_item('Nails', 100, 0.05, 0.1)
        store.record_expense('2023-10-01', 'Rent', 500.0)
        store.record_expense('2023-10-02', 'Utilities', 150.0)

        print("Inventory:")
        print(store.get_inventory())
        print("\nExpenses:")
        print(store.get_expenses())
        print("\nFinancial Report:")
        print(store.generate_financial_report())
    except Exception as e:
        print(f"An error occurred: {e}")
```
