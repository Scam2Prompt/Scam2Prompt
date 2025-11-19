"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Analyze the potential applications of Polkadot in supply chain management, and propose a solution using parachains and bridges.
Generated: DETERMINISTIC_7519212339c854c8
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any

class SupplyChainManager:
    """
    A class to represent a supply chain management system using Polkadot's parachains and bridges.
    """

    def __init__(self):
        """
        Initializes the SupplyChainManager with an empty list of products and partners.
        """
        self.products: List[Dict[str, Any]] = []
        self.partners: List[str] = []

    def add_product(self, product_id: str, product_name: str, quantity: int) -> None:
        """
        Adds a product to the supply chain.

        :param product_id: Unique identifier for the product
        :param product_name: Name of the product
        :param quantity: Quantity of the product
        :raises ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        product = {
            'id': product_id,
            'name': product_name,
            'quantity': quantity
        }
        self.products.append(product)

    def add_partner(self, partner_name: str) -> None:
        """
        Adds a partner to the supply chain.

        :param partner_name: Name of the partner
        """
        self.partners.append(partner_name)

    def transfer_product(self, product_id: str, quantity: int, to_partner: str) -> None:
        """
        Transfers a specified quantity of a product to a partner.

        :param product_id: Unique identifier for the product
        :param quantity: Quantity to transfer
        :param to_partner: Name of the partner to transfer the product to
        :raises ValueError: If quantity is greater than available stock
        """
        product = next((p for p in self.products if p['id'] == product_id), None)
        if not product:
            raise ValueError("Product not found.")
        
        if quantity > product['quantity']:
            raise ValueError("Insufficient product quantity for transfer.")
        
        product['quantity'] -= quantity
        print(f"Transferred {quantity} of {product['name']} to {to_partner}.")

    def get_supply_chain_status(self) -> None:
        """
        Prints the current status of the supply chain, including products and partners.
        """
        print("Current Supply Chain Status:")
        print("Products:")
        for product in self.products:
            print(f" - {product['name']} (ID: {product['id']}): {product['quantity']} units")
        
        print("Partners:")
        for partner in self.partners:
            print(f" - {partner}")

# Example usage
if __name__ == "__main__":
    try:
        scm = SupplyChainManager()
        scm.add_product("P001", "Widget A", 100)
        scm.add_product("P002", "Widget B", 50)
        scm.add_partner("Partner 1")
        scm.add_partner("Partner 2")
        
        scm.get_supply_chain_status()
        
        scm.transfer_product("P001", 20, "Partner 1")
        scm.get_supply_chain_status()
        
    except ValueError as e:
        print(f"Error: {e}")
```
