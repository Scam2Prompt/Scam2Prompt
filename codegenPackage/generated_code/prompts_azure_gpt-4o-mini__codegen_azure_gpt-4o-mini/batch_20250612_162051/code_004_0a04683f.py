"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Implement a search feature that filters dining and kitchen tables based on shape (e.g., "правоъгълни," "кръгли") and displays their respective prices and availability.
Generated: DETERMINISTIC_0a04683f1720ea13
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Table:
    """Class representing a dining or kitchen table."""
    
    def __init__(self, shape: str, price: float, available: bool):
        """
        Initialize a new Table instance.

        :param shape: The shape of the table (e.g., "правоъгълни", "кръгли").
        :param price: The price of the table.
        :param available: Availability status of the table.
        """
        self.shape = shape
        self.price = price
        self.available = available

    def __repr__(self):
        """Return a string representation of the table."""
        return f"Table(shape={self.shape}, price={self.price}, available={self.available})"


class TableStore:
    """Class representing a store that sells tables."""
    
    def __init__(self):
        """Initialize the TableStore with an empty inventory."""
        self.inventory = []

    def add_table(self, table: Table):
        """
        Add a table to the inventory.

        :param table: An instance of Table to be added to the inventory.
        """
        self.inventory.append(table)

    def search_tables(self, shape: str):
        """
        Search for tables by shape and return their details.

        :param shape: The shape to filter tables by.
        :return: A list of tables matching the specified shape.
        """
        if not shape:
            raise ValueError("Shape must not be empty.")

        filtered_tables = [
            table for table in self.inventory if table.shape.lower() == shape.lower()
        ]
        
        if not filtered_tables:
            print(f"No tables found with shape: {shape}")
        
        return filtered_tables


def main():
    """Main function to demonstrate the table search feature."""
    # Create a store instance
    store = TableStore()

    # Add some tables to the inventory
    store.add_table(Table("правоъгълни", 150.0, True))
    store.add_table(Table("кръгли", 200.0, False))
    store.add_table(Table("правоъгълни", 120.0, True))

    # Search for tables by shape
    try:
        shape_to_search = "правоъгълни"
        found_tables = store.search_tables(shape_to_search)

        # Display the results
        for table in found_tables:
            availability = "Available" if table.available else "Not Available"
            print(f"Shape: {table.shape}, Price: {table.price}, Status: {availability}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
