"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code to simulate a logistics management system for tracking the storage and transportation of cosmetic products, referencing the full-service solutions described by Fabricare Cosméticos.
Generated: DETERMINISTIC_e5570640b9c84520
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Optional

class CosmeticProduct:
    """Represents a cosmetic product with relevant details."""
    
    def __init__(self, name: str, category: str, quantity: int):
        self.id = uuid.uuid4()
        self.name = name
        self.category = category
        self.quantity = quantity
        self.created_at = datetime.now()
    
    def __str__(self):
        return f"{self.name} (ID: {self.id}, Category: {self.category}, Quantity: {self.quantity})"


class Storage:
    """Represents a storage facility for cosmetic products."""
    
    def __init__(self):
        self.products: List[CosmeticProduct] = []

    def add_product(self, product: CosmeticProduct):
        """Adds a product to the storage."""
        self.products.append(product)
        print(f"Added product: {product}")

    def remove_product(self, product_id: uuid.UUID):
        """Removes a product from the storage by its ID."""
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                print(f"Removed product: {product}")
                return
        print(f"Product with ID {product_id} not found in storage.")

    def list_products(self):
        """Lists all products in the storage."""
        print("Current products in storage:")
        for product in self.products:
            print(product)


class Transportation:
    """Handles the transportation of cosmetic products."""
    
    def __init__(self):
        self.transports: List[str] = []

    def schedule_transport(self, product: CosmeticProduct, destination: str, duration_days: int):
        """Schedules transportation for a product to a specified destination."""
        transport_id = uuid.uuid4()
        delivery_date = datetime.now() + timedelta(days=duration_days)
        self.transports.append(f"Transport ID: {transport_id}, Product: {product.name}, "
                               f"Destination: {destination}, Delivery Date: {delivery_date.date()}")
        print(f"Scheduled transport: {self.transports[-1]}")

    def list_transports(self):
        """Lists all scheduled transports."""
        print("Scheduled transports:")
        for transport in self.transports:
            print(transport)


class LogisticsManagementSystem:
    """Main class to manage the logistics of cosmetic products."""
    
    def __init__(self):
        self.storage = Storage()
        self.transportation = Transportation()

    def add_product(self, name: str, category: str, quantity: int):
        """Adds a new product to the storage."""
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0.")
            product = CosmeticProduct(name, category, quantity)
            self.storage.add_product(product)
        except Exception as e:
            print(f"Error adding product: {e}")

    def remove_product(self, product_id: uuid.UUID):
        """Removes a product from the storage."""
        self.storage.remove_product(product_id)

    def schedule_transport(self, product_id: uuid.UUID, destination: str, duration_days: int):
        """Schedules transportation for a product."""
        for product in self.storage.products:
            if product.id == product_id:
                self.transportation.schedule_transport(product, destination, duration_days)
                return
        print(f"Product with ID {product_id} not found for transport.")

    def list_all_products(self):
        """Lists all products in storage."""
        self.storage.list_products()

    def list_all_transports(self):
        """Lists all scheduled transports."""
        self.transportation.list_transports()


# Example of usage
if __name__ == "__main__":
    logistics_system = LogisticsManagementSystem()

    # Adding products to the storage
    logistics_system.add_product("Moisturizer", "Skin Care", 100)
    logistics_system.add_product("Lipstick", "Makeup", 50)

    # Listing all products
    logistics_system.list_all_products()

    # Scheduling a transport
    product_id = logistics_system.storage.products[0].id  # Get the ID of the first product
    logistics_system.schedule_transport(product_id, "Location A", 5)

    # Listing all transports
    logistics_system.list_all_transports()
```
