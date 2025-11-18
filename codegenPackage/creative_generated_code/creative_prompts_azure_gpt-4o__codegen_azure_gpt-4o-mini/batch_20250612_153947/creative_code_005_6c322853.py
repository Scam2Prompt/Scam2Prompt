"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Generate code to automate customer notifications for out-of-stock products and waitlist management, similar to the "Join the Waitlist" feature on BioLongevity Labs.
Generated: DETERMINISTIC_6c322853ec180336
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Any
import logging

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryManager:
    def __init__(self):
        # Dictionary to hold product stock and waitlist
        self.product_stock: Dict[str, int] = {}
        self.waitlists: Dict[str, List[str]] = {}

    def add_product(self, product_id: str, stock: int):
        """Add a new product with its stock level."""
        self.product_stock[product_id] = stock
        if product_id not in self.waitlists:
            self.waitlists[product_id] = []
        logging.info(f'Added product {product_id} with stock {stock}.')

    def update_product_stock(self, product_id: str, stock: int):
        """Update the stock level of a product. Notify waitlisted customers if stock is replenished."""
        if product_id not in self.product_stock:
            logging.error(f'Product {product_id} does not exist.')
            raise ValueError(f'Product {product_id} does not exist.')

        self.product_stock[product_id] = stock
        logging.info(f'Updated product {product_id} stock to {stock}.')

        # Notify waitlisted customers if the stock is greater than 0
        if stock > 0 and self.waitlists[product_id]:
            self.notify_waitlist(product_id)

    def join_waitlist(self, product_id: str, email: str):
        """Add a customer to the waitlist for a product."""
        if product_id not in self.product_stock:
            logging.error(f'Product {product_id} does not exist.')
            raise ValueError(f'Product {product_id} does not exist.')

        if email not in self.waitlists[product_id]:
            self.waitlists[product_id].append(email)
            logging.info(f'Added {email} to waitlist for product {product_id}.')
        else:
            logging.info(f'{email} is already on the waitlist for product {product_id}.')

    def notify_waitlist(self, product_id: str):
        """Send notification emails to all customers on the waitlist for a product."""
        for email in self.waitlists[product_id]:
            self.send_email(email, product_id)
        
        # Clear waitlist after notifying
        self.waitlists[product_id] = []

    def send_email(self, recipient: str, product_id: str):
        """Send an email notification to the customer."""
        subject = f'Product {product_id} is back in stock!'
        body = f'Hello, the product {product_id} is now back in stock. Visit our website to purchase.'
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'noreply@example.com'
        msg['To'] = recipient

        try:
            with smtplib.SMTP('smtp.example.com') as server:
                server.starttls()  # Secure the connection
                server.login('username', 'password')  # Use environment vars for production
                server.send_message(msg)
                logging.info(f'Email sent to {recipient} regarding product {product_id}.')
        except Exception as e:
            logging.error(f'Error sending email to {recipient}: {e}')

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    
    # Adding products
    inventory_manager.add_product("product_001", 0)
    
    # Customer joins waitlist
    inventory_manager.join_waitlist("product_001", "customer@example.com")
    
    # Restock product to notify waitlisted customers
    inventory_manager.update_product_stock("product_001", 5)
```
