"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Develop a POS system for a cafe using DemirSoft's "Cafe Restoran Masa Adisyon Takip Sistemi," including table management and receipt generation.
Generated: DETERMINISTIC_1c405970a17ff93b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Table:
    """
    Class representing a table in the cafe.
    """
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.order = []

    def occupy(self):
        """Mark the table as occupied."""
        if self.is_occupied:
            raise ValueError(f"Table {self.table_number} is already occupied.")
        self.is_occupied = True

    def vacate(self):
        """Mark the table as vacated and clear the order."""
        if not self.is_occupied:
            raise ValueError(f"Table {self.table_number} is already vacant.")
        self.is_occupied = False
        self.order.clear()

    def add_order(self, item):
        """Add an item to the table's order."""
        self.order.append(item)

    def generate_receipt(self):
        """Generate a receipt for the current order."""
        if not self.order:
            raise ValueError(f"No orders for table {self.table_number}.")
        receipt = f"Receipt for Table {self.table_number}\n"
        receipt += "=" * 30 + "\n"
        for item in self.order:
            receipt += f"- {item}\n"
        receipt += "=" * 30 + "\n"
        return receipt


class Cafe:
    """
    Class representing the cafe's management system.
    """
    def __init__(self):
        self.tables = {}

    def add_table(self, table_number):
        """Add a new table to the cafe."""
        if table_number in self.tables:
            raise ValueError(f"Table {table_number} already exists.")
        self.tables[table_number] = Table(table_number)

    def occupy_table(self, table_number):
        """Occupy a specified table."""
        table = self.tables.get(table_number)
        if table is None:
            raise ValueError(f"Table {table_number} does not exist.")
        table.occupy()

    def vacate_table(self, table_number):
        """Vacate a specified table."""
        table = self.tables.get(table_number)
        if table is None:
            raise ValueError(f"Table {table_number} does not exist.")
        table.vacate()

    def add_order_to_table(self, table_number, item):
        """Add an order item to a specified table."""
        table = self.tables.get(table_number)
        if table is None:
            raise ValueError(f"Table {table_number} does not exist.")
        table.add_order(item)

    def generate_receipt_for_table(self, table_number):
        """Generate receipt for the specified table."""
        table = self.tables.get(table_number)
        if table is None:
            raise ValueError(f"Table {table_number} does not exist.")
        return table.generate_receipt()


# Example usage
if __name__ == "__main__":
    cafe = Cafe()
    cafe.add_table(1)
    cafe.add_table(2)

    try:
        # Occupy table 1 and add orders
        cafe.occupy_table(1)
        cafe.add_order_to_table(1, "Coffee")
        cafe.add_order_to_table(1, "Croissant")

        # Generate receipt for table 1
        print(cafe.generate_receipt_for_table(1))

        # Vacate table 1
        cafe.vacate_table(1)

        # Attempt to generate receipt for vacated table
        print(cafe.generate_receipt_for_table(1))  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
