"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: "What are the benefits of using a software retail system like TICOM RMS for a pharmacy in Peru, and how can it improve business operations?"
Generated: DETERMINISTIC_0988ad20034abc19
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PharmacyRetailSystem:
    """
    A class to represent a software retail system for pharmacies.
    This system aims to improve business operations by managing inventory,
    sales, and customer relationships effectively.
    """

    def __init__(self):
        """
        Initializes the PharmacyRetailSystem with empty inventory and sales records.
        """
        self.inventory = {}
        self.sales_records = []

    def add_product(self, product_id, product_name, price, quantity):
        """
        Adds a new product to the inventory.

        Parameters:
        product_id (str): Unique identifier for the product.
        product_name (str): Name of the product.
        price (float): Price of the product.
        quantity (int): Quantity of the product in stock.

        Raises:
        ValueError: If the quantity is less than 0 or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        self.inventory[product_id] = {
            'name': product_name,
            'price': price,
            'quantity': quantity
        }

    def sell_product(self, product_id, quantity):
        """
        Processes a sale of a product.

        Parameters:
        product_id (str): Unique identifier for the product.
        quantity (int): Quantity of the product to sell.

        Raises:
        ValueError: If the product is not found or insufficient stock.
        """
        if product_id not in self.inventory:
            raise ValueError("Product not found in inventory.")

        product = self.inventory[product_id]
        if product['quantity'] < quantity:
            raise ValueError("Insufficient stock for the product.")

        # Update inventory and record the sale
        product['quantity'] -= quantity
        sale_record = {
            'product_id': product_id,
            'quantity': quantity,
            'total_price': product['price'] * quantity
        }
        self.sales_records.append(sale_record)

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
        dict: A dictionary representing the inventory.
        """
        return self.inventory

    def get_sales_records(self):
        """
        Returns the sales records.

        Returns:
        list: A list of sales records.
        """
        return self.sales_records

    def calculate_total_sales(self):
        """
        Calculates the total sales amount from all sales records.

        Returns:
        float: Total sales amount.
        """
        return sum(record['total_price'] for record in self.sales_records)

# Example usage
if __name__ == "__main__":
    try:
        pharmacy_system = PharmacyRetailSystem()
        pharmacy_system.add_product("001", "Aspirin", 10.0, 100)
        pharmacy_system.add_product("002", "Ibuprofen", 15.0, 50)

        pharmacy_system.sell_product("001", 2)
        pharmacy_system.sell_product("002", 1)

        print("Current Inventory:", pharmacy_system.get_inventory())
        print("Sales Records:", pharmacy_system.get_sales_records())
        print("Total Sales Amount:", pharmacy_system.calculate_total_sales())
    except ValueError as e:
        print(f"Error: {e}")
```
