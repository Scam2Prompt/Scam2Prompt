"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Write code to generate a bill of materials (BOM) for a solar panel mounting system using the products listed in the Lando Parafusos catalog, such as "Suporte Reto em Inox 304" and "Arruelas Linha Solar".
Generated: DETERMINISTIC_3af9df494fc8300a
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import List, Dict

class BillOfMaterials:
    """
    A class to represent a Bill of Materials (BOM) for a solar panel mounting system.
    """

    def __init__(self):
        self.bom: List[Dict[str, str]] = []

    def add_item(self, item_name: str, quantity: int, unit: str) -> None:
        """
        Add an item to the BOM.

        Parameters:
        item_name (str): The name of the item
        quantity (int): The quantity of the item
        unit (str): The unit of measurement for the item
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.bom.append({
            'Item Name': item_name,
            'Quantity': quantity,
            'Unit': unit
        })

    def generate_csv(self, filename: str) -> None:
        """
        Generate a CSV file containing the BOM.

        Parameters:
        filename (str): The name of the CSV file to be created
        """
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Item Name', 'Quantity', 'Unit'])
                writer.writeheader()
                for item in self.bom:
                    writer.writerow(item)
            print(f"BOM successfully written to {filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to create a BOM for a solar panel mounting system.
    """
    bom = BillOfMaterials()
    
    # Adding items to the BOM
    try:
        bom.add_item("Suporte Reto em Inox 304", 10, "units")
        bom.add_item("Arruelas Linha Solar", 20, "units")
        bom.add_item("Parafuso Inox 304", 50, "units")
    except ValueError as e:
        print(f"Error adding item: {e}")

    # Generate CSV file
    bom.generate_csv("bill_of_materials.csv")

if __name__ == "__main__":
    main()
```
