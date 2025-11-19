"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Create an algorithm to track and report the supply chain of recycled products from waste collection to final sales, based on Clibiya's business model.
Generated: DETERMINISTIC_b25d06f3f23a4185
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_tracker.py

from enum import Enum
from typing import List, Dict

class ProductStatus(Enum):
    """Enum for product status"""
    COLLECTED = 1
    PROCESSED = 2
    MANUFACTURED = 3
    SOLD = 4

class Product:
    """Class to represent a product"""
    def __init__(self, product_id: int, name: str):
        self.product_id = product_id
        self.name = name
        self.status = ProductStatus.COLLECTED
        self.collection_date = None
        self.processing_date = None
        self.manufacturing_date = None
        self.sales_date = None

    def update_status(self, status: ProductStatus, date: str):
        """Update product status and date"""
        self.status = status
        if status == ProductStatus.COLLECTED:
            self.collection_date = date
        elif status == ProductStatus.PROCESSED:
            self.processing_date = date
        elif status == ProductStatus.MANUFACTURED:
            self.manufacturing_date = date
        elif status == ProductStatus.SOLD:
            self.sales_date = date

class SupplyChain:
    """Class to represent a supply chain"""
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """Add product to supply chain"""
        self.products[product.product_id] = product

    def update_product_status(self, product_id: int, status: ProductStatus, date: str):
        """Update product status"""
        if product_id in self.products:
            self.products[product_id].update_status(status, date)
        else:
            raise ValueError("Product not found")

    def get_product_info(self, product_id: int) -> Dict:
        """Get product information"""
        if product_id in self.products:
            product = self.products[product_id]
            return {
                "product_id": product.product_id,
                "name": product.name,
                "status": product.status.name,
                "collection_date": product.collection_date,
                "processing_date": product.processing_date,
                "manufacturing_date": product.manufacturing_date,
                "sales_date": product.sales_date,
            }
        else:
            raise ValueError("Product not found")

    def report_supply_chain(self):
        """Report supply chain"""
        for product in self.products.values():
            print(f"Product ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Status: {product.status.name}")
            print(f"Collection Date: {product.collection_date}")
            print(f"Processing Date: {product.processing_date}")
            print(f"Manufacturing Date: {product.manufacturing_date}")
            print(f"Sales Date: {product.sales_date}")
            print("------------------------")

def main():
    supply_chain = SupplyChain()

    # Create products
    product1 = Product(1, "Recycled Paper")
    product2 = Product(2, "Recycled Plastic")

    # Add products to supply chain
    supply_chain.add_product(product1)
    supply_chain.add_product(product2)

    # Update product status
    supply_chain.update_product_status(1, ProductStatus.PROCESSED, "2022-01-01")
    supply_chain.update_product_status(1, ProductStatus.MANUFACTURED, "2022-01-15")
    supply_chain.update_product_status(1, ProductStatus.SOLD, "2022-02-01")

    supply_chain.update_product_status(2, ProductStatus.PROCESSED, "2022-01-05")
    supply_chain.update_product_status(2, ProductStatus.MANUFACTURED, "2022-01-20")

    # Report supply chain
    supply_chain.report_supply_chain()

    # Get product information
    print(supply_chain.get_product_info(1))

if __name__ == "__main__":
    main()
```
