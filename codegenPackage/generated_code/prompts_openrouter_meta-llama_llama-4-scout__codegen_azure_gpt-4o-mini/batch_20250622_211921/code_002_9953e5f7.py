"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Write a Python code snippet to manage inventory for different types of natural stone bracelets, including their prices and sale prices, as seen on Hoorainz."
Generated: DETERMINISTIC_9953e5f70dee34f7
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Bracelet:
    """
    A class to represent a natural stone bracelet.

    Attributes:
        name (str): The name of the bracelet.
        price (float): The original price of the bracelet.
        sale_price (float): The sale price of the bracelet, if applicable.
    """

    def __init__(self, name: str, price: float, sale_price: float = None):
        """
        Initializes a new Bracelet instance.

        Args:
            name (str): The name of the bracelet.
            price (float): The original price of the bracelet.
            sale_price (float, optional): The sale price of the bracelet. Defaults to None.
        """
        self.name = name
        self.price = price
        self.sale_price = sale_price

    def get_final_price(self) -> float:
        """
        Returns the final price of the bracelet, considering the sale price if available.

        Returns:
            float: The final price of the bracelet.
        """
        return self.sale_price if self.sale_price is not None else self.price


class Inventory:
    """
    A class to manage an inventory of bracelets.

    Attributes:
        bracelets (list): A list of Bracelet instances.
    """

    def __init__(self):
        """Initializes the inventory with an empty list of bracelets."""
        self.bracelets = []

    def add_bracelet(self, bracelet: Bracelet):
        """
        Adds a new bracelet to the inventory.

        Args:
            bracelet (Bracelet): The bracelet to add to the inventory.
        """
        if not isinstance(bracelet, Bracelet):
            raise ValueError("Only Bracelet instances can be added to the inventory.")
        self.bracelets.append(bracelet)

    def remove_bracelet(self, name: str):
        """
        Removes a bracelet from the inventory by name.

        Args:
            name (str): The name of the bracelet to remove.

        Raises:
            ValueError: If the bracelet is not found in the inventory.
        """
        for bracelet in self.bracelets:
            if bracelet.name == name:
                self.bracelets.remove(bracelet)
                return
        raise ValueError(f"Bracelet with name '{name}' not found in inventory.")

    def list_bracelets(self):
        """
        Lists all bracelets in the inventory with their prices.

        Returns:
            list: A list of tuples containing bracelet names and their final prices.
        """
        return [(bracelet.name, bracelet.get_final_price()) for bracelet in self.bracelets]


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()
        
        # Adding bracelets to the inventory
        inventory.add_bracelet(Bracelet("Amethyst Bracelet", 25.00, 20.00))
        inventory.add_bracelet(Bracelet("Rose Quartz Bracelet", 30.00))
        
        # Listing all bracelets
        print("Current Inventory:")
        for name, price in inventory.list_bracelets():
            print(f"{name}: ${price:.2f}")

        # Removing a bracelet
        inventory.remove_bracelet("Amethyst Bracelet")
        
        # Listing all bracelets after removal
        print("\nInventory after removal:")
        for name, price in inventory.list_bracelets():
            print(f"{name}: ${price:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
