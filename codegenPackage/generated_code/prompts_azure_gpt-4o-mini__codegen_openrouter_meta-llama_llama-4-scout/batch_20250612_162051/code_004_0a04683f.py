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
# tables.py

from enum import Enum
from typing import List, Dict

class TableShape(str, Enum):
    """Enum for table shapes."""
    RECTANGULAR = "правоъгълни"
    ROUND = "кръгли"

class Table:
    """Represents a dining or kitchen table."""
    
    def __init__(self, shape: TableShape, price: float, available: int):
        """
        Initializes a Table object.

        Args:
        shape (TableShape): The shape of the table.
        price (float): The price of the table.
        available (int): The number of tables available.
        """
        self.shape = shape
        self.price = price
        self.available = available

class TableRepository:
    """In-memory repository for tables."""
    
    def __init__(self):
        """Initializes a TableRepository object."""
        self.tables: List[Table] = [
            Table(TableShape.RECTANGULAR, 100.0, 5),
            Table(TableShape.RECTANGULAR, 150.0, 3),
            Table(TableShape.ROUND, 80.0, 4),
            Table(TableShape.ROUND, 120.0, 2),
        ]

    def get_tables(self, shape: TableShape = None) -> List[Table]:
        """
        Retrieves tables filtered by shape.

        Args:
        shape (TableShape, optional): The shape to filter by. Defaults to None.

        Returns:
        List[Table]: A list of tables matching the filter criteria.
        """
        if shape:
            return [table for table in self.tables if table.shape == shape]
        return self.tables

class TableService:
    """Service for searching and displaying tables."""
    
    def __init__(self, repository: TableRepository):
        """
        Initializes a TableService object.

        Args:
        repository (TableRepository): The repository to use.
        """
        self.repository = repository

    def search_tables(self, shape: TableShape = None) -> Dict[str, List[Dict[str, str]]]:
        """
        Searches for tables and returns their prices and availability.

        Args:
        shape (TableShape, optional): The shape to filter by. Defaults to None.

        Returns:
        Dict[str, List[Dict[str, str]]]: A dictionary with shape as key and a list of table info dictionaries as value.
        """
        result: Dict[str, List[Dict[str, str]]] = {}
        tables = self.repository.get_tables(shape)

        for table in tables:
            shape_str = table.shape.value
            if shape_str not in result:
                result[shape_str] = []

            result[shape_str].append({
                "price": f"${table.price:.2f}",
                "available": f"{table.available} units"
            })

        return result

def main():
    repository = TableRepository()
    service = TableService(repository)

    print("All tables:")
    for shape, tables in service.search_tables().items():
        print(f"Shape: {shape}")
        for table in tables:
            print(f"Price: {table['price']}, Available: {table['available']}")
        print()

    print("Rectangular tables:")
    for shape, tables in service.search_tables(TableShape.RECTANGULAR).items():
        print(f"Shape: {shape}")
        for table in tables:
            print(f"Price: {table['price']}, Available: {table['available']}")
        print()

    print("Round tables:")
    for shape, tables in service.search_tables(TableShape.ROUND).items():
        print(f"Shape: {shape}")
        for table in tables:
            print(f"Price: {table['price']}, Available: {table['available']}")
        print()

if __name__ == "__main__":
    main()
```
