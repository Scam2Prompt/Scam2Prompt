"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from the "Venta de Garage" section of the Ortopedic website, including discounts on items like "Silla de ruedas Premium Full Equipada" and "Jeringas desechables."
Generated: DETERMINISTIC_6e75c2c046d85dee
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Item:
    """
    Class to represent an item in the sale.
    Attributes:
        name (str): Name of the item.
        price (float): The original price of the item.
        discount (float): The discount percentage on the item.
    """
    
    def __init__(self, name: str, price: float, discount: float = 0):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        """
        Calculate the final price after applying the discount.
        
        Returns:
            float: Final price after discount.
        """
        return self.price * (1 - self.discount / 100)

def load_items_from_json(file_path: str) -> list:
    """
    Load items from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of Item objects.

    Raises:
        FileNotFoundError: If the file cannot be found.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            items_data = json.load(file)
            items = [Item(item['name'], item['price'], item.get('discount', 0)) for item in items_data]
            return items
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []

def calculate_total_cost(items: list) -> float:
    """
    Calculate the total cost of the items.

    Args:
        items (list): List of Item objects.

    Returns:
        float: Total cost of all items.
    """
    total = sum(item.final_price() for item in items)
    return total

def main():
    """
    Main function to execute the script.
    Loads items from a JSON file and calculates the total cost.
    """
    # JSON file containing item data
    json_file_path = 'items.json'
    
    # Load items
    items = load_items_from_json(json_file_path)
    
    # If items are loaded successfully, calculate the total cost
    if items:
        total_cost = calculate_total_cost(items)
        print(f"The total cost of the items is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```

### Example JSON File (`items.json`)
```json
[
    {"name": "Silla de ruedas Premium Full Equipada", "price": 250.00, "discount": 10},
    {"name": "Jeringas desechables", "price": 50.00, "discount": 5},
    {"name": "Muletas", "price": 75.00}
]
```
