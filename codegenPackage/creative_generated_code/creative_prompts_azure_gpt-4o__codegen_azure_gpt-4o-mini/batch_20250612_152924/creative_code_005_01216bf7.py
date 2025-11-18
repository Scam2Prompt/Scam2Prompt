"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Create a Python function to generate invoices for international buyers of Himalayan salt products, incorporating product categories, packaging details, and shipping costs.
Generated: DETERMINISTIC_01216bf7e70d867b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class Invoice:
    """Class to represent an invoice for Himalayan salt products."""
    
    def __init__(self, buyer_name, buyer_address, products, shipping_cost):
        """
        Initialize an invoice.
        
        Parameters:
            buyer_name (str): Name of the buyer.
            buyer_address (str): Address of the buyer.
            products (list): List of products (dict) with details.
            shipping_cost (float): Shipping cost for the products.
        """
        self.invoice_id = str(uuid.uuid4())
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.buyer_name = buyer_name
        self.buyer_address = buyer_address
        self.products = products
        self.shipping_cost = shipping_cost
        self.total_cost = self.calculate_total()

    def calculate_total(self):
        """Calculate the total cost including products and shipping."""
        total = sum(product['price'] * product['quantity'] for product in self.products)
        total += self.shipping_cost
        return total

    def generate_invoice(self):
        """Generate a formatted invoice string."""
        invoice_details = [
            f"Invoice ID: {self.invoice_id}",
            f"Date: {self.date}",
            f"Buyer: {self.buyer_name}",
            f"Address: {self.buyer_address}",
            "Products:"
        ]
        
        for product in self.products:
            invoice_details.append(f"  - {product['category']} ({product['quantity']} x {product['price']:.2f})")
        
        invoice_details.append(f"Shipping Cost: {self.shipping_cost:.2f}")
        invoice_details.append(f"Total Cost: {self.total_cost:.2f}")
        
        return "\n".join(invoice_details)

def create_invoice(buyer_name, buyer_address, products, shipping_cost):
    """
    Create and return an invoice for the given buyer and products.
    
    Parameters:
        buyer_name (str): Name of the buyer.
        buyer_address (str): Address of the buyer.
        products (list): List of products (dict) with details.
        shipping_cost (float): Shipping cost for the products.
    
    Returns:
        str: Formatted invoice string.
    
    Raises:
        ValueError: If any product has invalid data.
    """
    # Validate input parameters
    if not isinstance(buyer_name, str) or not buyer_name:
        raise ValueError("Invalid buyer name.")
    if not isinstance(buyer_address, str) or not buyer_address:
        raise ValueError("Invalid buyer address.")
    if not isinstance(products, list) or not products:
        raise ValueError("Product list must be a non-empty list.")
    
    for product in products:
        if not isinstance(product, dict) or 'category' not in product or 'price' not in product or 'quantity' not in product:
            raise ValueError("Each product must be a dictionary with 'category', 'price', and 'quantity'.")
        if not isinstance(product['price'], (int, float)) or not isinstance(product['quantity'], int) or product['quantity'] <= 0:
            raise ValueError("Product price must be a non-negative number and quantity must be a positive integer.")
    
    if not isinstance(shipping_cost, (int, float)) or shipping_cost < 0:
        raise ValueError("Shipping cost must be a non-negative number.")

    # Create and return the invoice
    invoice = Invoice(buyer_name, buyer_address, products, shipping_cost)
    return invoice.generate_invoice()

# Example usage (commented out for production-ready code)
# if __name__ == "__main__":
#     products = [
#         {'category': 'Fine Himalayan Salt', 'price': 10.00, 'quantity': 2},
#         {'category': 'Coarse Himalayan Salt', 'price': 8.50, 'quantity': 1},
#     ]
#     shipping_cost = 15.00
#     invoice = create_invoice("John Doe", "123 Salt Lane, Kathmandu, Nepal", products, shipping_cost)
#     print(invoice)
```
