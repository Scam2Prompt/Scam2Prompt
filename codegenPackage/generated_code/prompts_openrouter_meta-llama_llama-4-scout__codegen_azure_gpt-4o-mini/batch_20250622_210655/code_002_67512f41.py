"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Generate a list of coffee tables with glass tops, similar to the "Веста" and "Изида" tables, including their prices and dimensions.
Generated: DETERMINISTIC_67512f4132330f5f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class CoffeeTable:
    """Class representing a coffee table with a glass top."""
    
    def __init__(self, name: str, price: float, dimensions: str):
        """
        Initializes a new CoffeeTable instance.

        Args:
            name (str): The name of the coffee table.
            price (float): The price of the coffee table.
            dimensions (str): The dimensions of the coffee table.
        """
        self.name = name
        self.price = price
        self.dimensions = dimensions

    def to_dict(self) -> Dict[str, str]:
        """Converts the CoffeeTable instance to a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "dimensions": self.dimensions
        }

def generate_coffee_tables() -> List[CoffeeTable]:
    """Generates a list of coffee tables with glass tops."""
    tables = [
        CoffeeTable("Веста", 150.00, "120x60x45 cm"),
        CoffeeTable("Изида", 200.00, "100x50x40 cm"),
        CoffeeTable("Люкс", 250.00, "110x55x42 cm"),
        CoffeeTable("Элегант", 180.00, "130x70x46 cm"),
        CoffeeTable("Модерн", 220.00, "115x65x44 cm")
    ]
    return tables

def save_tables_to_json(tables: List[CoffeeTable], filename: str) -> None:
    """Saves the list of coffee tables to a JSON file.

    Args:
        tables (List[CoffeeTable]): The list of coffee tables to save.
        filename (str): The name of the file to save the data to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump([table.to_dict() for table in tables], file, ensure_ascii=False, indent=4)
        print(f"Successfully saved coffee tables to {filename}.")
    except IOError as e:
        print(f"Error saving to file {filename}: {e}")

def main() -> None:
    """Main function to generate and save coffee tables."""
    coffee_tables = generate_coffee_tables()
    save_tables_to_json(coffee_tables, 'coffee_tables.json')

if __name__ == "__main__":
    main()
```
