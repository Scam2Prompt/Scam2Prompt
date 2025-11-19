"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superdar.com
Prompt: Implement a search feature that filters dining and kitchen tables based on shape (e.g., "правоъгълни," "кръгли") and displays their respective prices and availability.
Generated: DETERMINISTIC_0a04683f1720ea13
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Table:
    """Class to represent a dining or kitchen table."""

    def __init__(self, shape, price, available):
        """
        Initialize a Table instance.

        Args:
            shape (str): The shape of the table (e.g., "правоъгълни", "кръгли").
            price (float): The price of the table.
            available (bool): Availability of the table.
        """
        self.shape = shape
        self.price = price
        self.available = available

    def __repr__(self):
        """Return a string representation of the table."""
        availability = "Available" if self.available else "Not Available"
        return f"{self.shape.title()} Table - Price: ${self.price:.2f} - {availability}"


class TableStore:
    """Class to represent a store that sells tables."""

    def __init__(self):
        """Initialize the TableStore with a list of tables."""
        self.tables = []

    def add_table(self, table):
        """Add a table to the store.

        Args:
            table (Table): The table instance to add.
        """
        if not isinstance(table, Table):
            raise ValueError("Invalid table instance.")
        self.tables.append(table)

    def search_tables(self, shape):
        """Search for tables by shape.

        Args:
            shape (str): The shape to filter tables by.

        Returns:
            list: A list of tables matching the given shape.
        """
        if not isinstance(shape, str) or not shape:
            raise ValueError("Shape must be a non-empty string.")

        # Filter tables based on the requested shape
        filtered_tables = [table for table in self.tables if table.shape.lower() == shape.lower()]
        return filtered_tables


def main():
    """Main function to demonstrate the table search feature."""
    store = TableStore()

    # Adding some tables to the store
    store.add_table(Table("правоъгълни", 150.00, True))
    store.add_table(Table("кръгли", 120.00, False))
    store.add_table(Table("правоъгълни", 200.00, True))
    store.add_table(Table("кръгли", 130.00, True))

    # Searching for tables
    try:
        shape_to_search = "правоъгълни"
        found_tables = store.search_tables(shape_to_search)

        print(f"Tables found with shape '{shape_to_search}':")
        for table in found_tables:
            print(table)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
