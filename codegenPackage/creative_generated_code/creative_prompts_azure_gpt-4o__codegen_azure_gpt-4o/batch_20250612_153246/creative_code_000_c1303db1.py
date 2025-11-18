"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Write Python code to create a financial control template for a hardware store, incorporating features like inventory tracking and expense management, as described in "Plantillas para control Financiero en la Ferretería" from Aula Ferretera.
Generated: DETERMINISTIC_c1303db14ff2df1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

class HardwareStoreFinanceControl:
    """
    A class to manage financial control for a hardware store, including inventory tracking
    and expense management.
    """

    def __init__(self, inventory_file='inventory.csv', expenses_file='expenses.csv'):
        """
        Initialize the financial control system with inventory and expenses file paths.
        """
        self.inventory_file = inventory_file
        self.expenses_file = expenses_file

        # Ensure files exist
        self._initialize_file(self.inventory_file, ['Item ID', 'Item Name', 'Quantity', 'Unit Price'])
        self._initialize_file(self.expenses_file, ['Date', 'Category', 'Description', 'Amount'])

    def _initialize_file(self, file_path, headers):
        """
        Ensure a CSV file exists and has the correct headers; create it if necessary.
        """
        if not os.path.exists(file_path):
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    def add_inventory_item(self, item_id, item_name, quantity, unit_price):
        """
        Add a new item to the inventory or update an existing item's quantity and price.
        """
        inventory = self._read_csv(self.inventory_file)
        item_exists = False

        for item in inventory:
            if item['Item ID'] == item_id:
                item_exists = True
                item['Quantity'] = int(item['Quantity']) + quantity
                item['Unit Price'] = unit_price
                break

        if not item_exists:
            inventory.append({
                'Item ID': item_id,
                'Item Name': item_name,
                'Quantity': quantity,
                'Unit Price': unit_price
            })

        self._write_csv(self.inventory_file, inventory)

    def remove_inventory_item(self, item_id):
        """
        Remove an item from the inventory by its ID.
        """
        inventory = self._read_csv(self.inventory_file)
        updated_inventory = [item for item in inventory if item['Item ID'] != item_id]

        self._write_csv(self.inventory_file, updated_inventory)

    def record_expense(self, date, category, description, amount):
        """
        Record a new expense in the expenses file.
        """
        if amount < 0:
            raise ValueError("Expense amount must be positive.")

        with open(self.expenses_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

    def view_inventory(self):
        """
        View all inventory items.
        """
        inventory = self._read_csv(self.inventory_file)
        return inventory

    def view_expenses(self):
        """
        View all recorded expenses.
        """
        expenses = self._read_csv(self.expenses_file)
        return expenses

    def _read_csv(self, file_path):
        """
        Read data from a CSV file and return it as a list of dictionaries.
        """
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def _write_csv(self, file_path, data):
        """
        Write data to a CSV file from a list of dictionaries.
        """
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


# Example usage:
if __name__ == "__main__":
    # Initialize financial control system
    store_control = HardwareStoreFinanceControl()

    # Add inventory items
    store_control.add_inventory_item(item_id="001", item_name="Hammer", quantity=10, unit_price=15.99)
    store_control.add_inventory_item(item_id="002", item_name="Nails", quantity=100, unit_price=0.10)

    # Record an expense
    store_control.record_expense(date="2023-10-15", category="Maintenance", description="Repair of shelves", amount=200)

    # View inventory
    print("Current Inventory:")
    for item in store_control.view_inventory():
        print(item)

    # View expenses
    print("\nRecorded Expenses:")
    for expense in store_control.view_expenses():
        print(expense)
```
