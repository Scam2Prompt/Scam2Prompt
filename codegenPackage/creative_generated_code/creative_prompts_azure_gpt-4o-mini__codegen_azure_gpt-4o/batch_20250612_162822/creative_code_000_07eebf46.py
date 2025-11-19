"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a Python script to automate the selection and ordering process for железобетонные изделия based on specific construction needs in Санкт-Петербурге.
Generated: DETERMINISTIC_07eebf467bbd1b1c
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os


class ConstructionMaterialOrderSystem:
    """
    A system to automate the selection and ordering process for
    железобетонные изделия (reinforced concrete products) based on specific
    construction needs in Санкт-Петербурге.
    """

    def __init__(self, inventory_file):
        """
        Initializes the system with an inventory file.

        :param inventory_file: Path to the JSON file containing the inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory of reinforced concrete products from a JSON file.

        :return: Dictionary representing inventory data.
        """
        if not os.path.exists(self.inventory_file):
            raise FileNotFoundError("Inventory file not found.")
        
        try:
            with open(self.inventory_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Failed to parse inventory file. Ensure it is valid JSON.")
    
    def filter_products(self, criteria):
        """
        Filters the products in the inventory based on specific criteria.

        :param criteria: Dictionary with key-value pairs representing search criteria.
        :return: List of matching products.
        """
        filtered_products = []
        for product in self.inventory.get('products', []):
            if all(product.get(key) == value for key, value in criteria.items()):
                filtered_products.append(product)
        return filtered_products

    def place_order(self, product_id, quantity):
        """
        Places an order for a specific product.

        :param product_id: The ID of the product to order.
        :param quantity: The quantity of the product to order.
        :return: Confirmation message about the order.
        """
        product = next((p for p in self.inventory.get('products', []) if p['id'] == product_id), None)
        if not product:
            return f"Product with ID {product_id} not found in inventory."
        
        if product['stock'] < quantity:
            return f"Insufficient stock for product ID {product_id}. Available: {product['stock']}."
        
        product['stock'] -= quantity  # Deduct the ordered quantity from stock
        return f"Order placed for {quantity} units of product ID {product_id}. Remaining stock: {product['stock']}."

    def save_inventory(self):
        """
        Saves the updated inventory back to the JSON file.

        :return: None
        """
        try:
            with open(self.inventory_file, 'w', encoding='utf-8') as file:
                json.dump(self.inventory, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save inventory file: {str(e)}")


def main():
    """
    Main function to execute the order automation system.
    """
    inventory_file = 'inventory.json'  # Path to inventory file
    try:
        system = ConstructionMaterialOrderSystem(inventory_file)

        # Example: Filter products based on construction needs
        criteria = {'type': 'beam', 'material': 'reinforced concrete'}
        matching_products = system.filter_products(criteria)
        print("Matching Products:")
        for product in matching_products:
            print(product)

        # Example: Place an order for a specific product
        if matching_products:
            product_id = matching_products[0]['id']
            quantity = 5  # Example quantity
            order_confirmation = system.place_order(product_id, quantity)
            print(order_confirmation)

            # Save updated inventory
            system.save_inventory()

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```

Note: Ensure to create a file named `inventory.json` in the same directory as the script, containing product data, for the script to load and manipulate inventory.
