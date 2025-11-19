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
# ticom_rms_benefits.py

class PharmacyOperations:
    """
    A class to demonstrate the benefits of using a software retail system like TICOM RMS for a pharmacy in Peru.
    """

    def __init__(self, pharmacy_name, location):
        """
        Initializes a PharmacyOperations object.

        Args:
            pharmacy_name (str): The name of the pharmacy.
            location (str): The location of the pharmacy.
        """
        self.pharmacy_name = pharmacy_name
        self.location = location
        self.inventory = {}
        self.sales = []

    def manage_inventory(self, product_name, quantity):
        """
        Manages the inventory of the pharmacy.

        Args:
            product_name (str): The name of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

    def record_sale(self, product_name, quantity, price):
        """
        Records a sale in the pharmacy.

        Args:
            product_name (str): The name of the product.
            quantity (int): The quantity of the product sold.
            price (float): The price of the product.

        Raises:
            ValueError: If the quantity or price is negative.
            KeyError: If the product is not in the inventory.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative")

        if product_name not in self.inventory:
            raise KeyError("Product not found in inventory")

        if self.inventory[product_name] < quantity:
            raise ValueError("Insufficient quantity in stock")

        self.sales.append({"product_name": product_name, "quantity": quantity, "price": price})
        self.inventory[product_name] -= quantity

    def calculate_revenue(self):
        """
        Calculates the total revenue of the pharmacy.

        Returns:
            float: The total revenue.
        """
        return sum(sale["quantity"] * sale["price"] for sale in self.sales)

    def get_inventory(self):
        """
        Gets the current inventory of the pharmacy.

        Returns:
            dict: The current inventory.
        """
        return self.inventory.copy()


def main():
    try:
        pharmacy = PharmacyOperations("Farmacia Peru", "Lima")

        # Manage inventory
        pharmacy.manage_inventory("Paracetamol", 100)
        pharmacy.manage_inventory("Ibuprofen", 50)

        # Record sales
        pharmacy.record_sale("Paracetamol", 20, 5.99)
        pharmacy.record_sale("Ibuprofen", 10, 7.99)

        # Calculate revenue
        revenue = pharmacy.calculate_revenue()
        print(f"Total Revenue: S/ {revenue:.2f}")

        # Get inventory
        inventory = pharmacy.get_inventory()
        print("Current Inventory:")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
