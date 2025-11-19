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
    """
    Represents a coffee table with glass top.
    """
    def __init__(self, name: str, price: float, length: float, width: float, height: float):
        self.name = name
        self.price = price
        self.length = length
        self.width = width
        self.height = height

    def to_dict(self) -> Dict:
        """
        Convert the table data to a dictionary.
        """
        return {
            "name": self.name,
            "price": self.price,
            "dimensions": {
                "length": self.length,
                "width": self.width,
                "height": self.height
            }
        }

def generate_coffee_tables() -> List[Dict]:
    """
    Generate a list of coffee tables with glass tops similar to "Веста" and "Изида".
    Returns a list of dictionaries containing table information.
    """
    tables = [
        CoffeeTable("Веста", 249.99, 120.0, 60.0, 45.0),
        CoffeeTable("Изида", 299.99, 140.0, 70.0, 50.0),
        CoffeeTable("Модерн", 199.99, 100.0, 50.0, 40.0),
        CoffeeTable("Элегант", 349.99, 150.0, 75.0, 55.0),
        CoffeeTable("Минимал", 179.99, 90.0, 45.0, 38.0),
        CoffeeTable("Люкс", 399.99, 160.0, 80.0, 60.0)
    ]
    
    return [table.to_dict() for table in tables]

def save_to_json(data: List[Dict], filename: str = "coffee_tables.json") -> None:
    """
    Save the coffee tables data to a JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    coffee_tables = generate_coffee_tables()
    save_to_json(coffee_tables)
    print("Coffee tables data generated successfully.")
```
