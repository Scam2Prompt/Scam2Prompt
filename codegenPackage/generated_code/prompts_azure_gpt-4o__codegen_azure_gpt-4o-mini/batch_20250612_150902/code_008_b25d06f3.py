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
import datetime
from typing import List, Dict, Optional

class RecycledProduct:
    """Class to represent a recycled product in the supply chain."""
    
    def __init__(self, product_id: str, name: str, weight: float):
        self.product_id = product_id
        self.name = name
        self.weight = weight
        self.collection_date: Optional[datetime.datetime] = None
        self.processing_date: Optional[datetime.datetime] = None
        self.sales_date: Optional[datetime.datetime] = None
        self.status: str = "Collected"  # Initial status

    def update_status(self, new_status: str):
        """Update the status of the recycled product."""
        self.status = new_status

    def set_collection_date(self):
        """Set the collection date to the current date."""
        self.collection_date = datetime.datetime.now()

    def set_processing_date(self):
        """Set the processing date to the current date."""
        self.processing_date = datetime.datetime.now()
        self.update_status("Processed")

    def set_sales_date(self):
        """Set the sales date to the current date."""
        self.sales_date = datetime.datetime.now()
        self.update_status("Sold")

class SupplyChainTracker:
    """Class to track the supply chain of recycled products."""
    
    def __init__(self):
        self.products: Dict[str, RecycledProduct] = {}

    def add_product(self, product: RecycledProduct):
        """Add a new recycled product to the supply chain."""
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def collect_product(self, product_id: str):
        """Mark a product as collected."""
        product = self.get_product(product_id)
        product.set_collection_date()

    def process_product(self, product_id: str):
        """Mark a product as processed."""
        product = self.get_product(product_id)
        product.set_processing_date()

    def sell_product(self, product_id: str):
        """Mark a product as sold."""
        product = self.get_product(product_id)
        product.set_sales_date()

    def get_product(self, product_id: str) -> RecycledProduct:
        """Retrieve a product by its ID."""
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found.")
        return self.products[product_id]

    def report_supply_chain(self) -> List[Dict]:
        """Generate a report of the supply chain."""
        report = []
        for product in self.products.values():
            report.append({
                "Product ID": product.product_id,
                "Name": product.name,
                "Weight": product.weight,
                "Collection Date": product.collection_date,
                "Processing Date": product.processing_date,
                "Sales Date": product.sales_date,
                "Status": product.status
            })
        return report

# Example usage
if __name__ == "__main__":
    tracker = SupplyChainTracker()
    
    # Create and add products
    product1 = RecycledProduct("001", "Recycled Paper", 10.5)
    product2 = RecycledProduct("002", "Recycled Plastic", 15.0)

    tracker.add_product(product1)
    tracker.add_product(product2)

    # Track the supply chain
    tracker.collect_product("001")
    tracker.process_product("001")
    tracker.sell_product("001")

    # Generate and print the supply chain report
    supply_chain_report = tracker.report_supply_chain()
    for entry in supply_chain_report:
        print(entry)
```
