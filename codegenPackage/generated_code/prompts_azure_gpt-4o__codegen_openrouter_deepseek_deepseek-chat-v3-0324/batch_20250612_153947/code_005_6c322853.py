"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: Generate code to automate customer notifications for out-of-stock products and waitlist management, similar to the "Join the Waitlist" feature on BioLongevity Labs.
Generated: DETERMINISTIC_6c322853ec180336
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Customer:
    """Represents a customer on the waitlist."""
    email: str
    name: str
    product_id: str
    join_date: datetime
    notified: bool = False

@dataclass
class Product:
    """Represents a product with inventory information."""
    product_id: str
    name: str
    in_stock: bool = False
    restock_date: Optional[datetime] = None

class WaitlistManager:
    """Manages customer waitlists for out-of-stock products."""
    
    def __init__(self, smtp_config: Dict):
        """
        Initialize the WaitlistManager.
        
        Args:
            smtp_config: Dictionary containing SMTP server configuration
                        (host, port, username, password, from_email)
        """
        self.waitlist: Dict[str, List[Customer]] = {}  # product_id -> list of customers
        self.smtp_config = smtp_config
        self.products: Dict[str, Product] = {}  # product_id -> Product
        
    def add_product(self, product: Product) -> None:
        """Add a product to be managed."""
        if product.product_id in self.products:
            raise ValueError(f"Product {product.product_id} already exists")
        self.products[product.product_id] = product
        self.waitlist[product.product_id] = []
        logger.info(f"Added product: {product.product_id}")
        
    def add_to_waitlist(self, email: str, name: str, product_id: str) -> None:
        """Add a customer to the waitlist for a product."""
        if product_id not in self.products:
            raise ValueError(f"Product {product_id} not found")
            
        # Check if customer is already on the waitlist
        for customer in self.waitlist[product_id]:
            if customer.email == email:
                raise ValueError(f"Customer {email} already on waitlist for {product_id}")
                
        customer = Customer(
            email=email,
            name=name,
            product_id=product_id,
            join_date=datetime.now()
        )
        self.waitlist[product_id].append(customer)
        logger.info(f"Added {email} to waitlist for {product_id}")
        
    def check_inventory_and_notify(self) -> None:
        """Check inventory and notify waitlisted customers when products are back in stock."""
        for product_id, product in self.products.items():
            if product.in_stock and self.waitlist[product_id]:
                self._notify_customers(product_id)
                
    def _notify_customers(self, product_id: str) -> None:
        """Notify all customers on the waitlist for a product that's back in stock."""
        product = self.products[product_id]
        customers = self.waitlist[product_id]
        
        for customer in customers:
            if not customer.notified:
                try:
                    self._send_notification(customer, product)
                    customer.notified = True
                    logger.info(f"Notified {customer.email} about {product_id}")
                except Exception as e:
                    logger.error(f"Failed to notify {customer.email}: {str(e)}")
                    
        # Remove notified customers from waitlist
        self.waitlist[product_id] = [c for c in customers if not c.notified]
        
    def _send_notification(self, customer: Customer, product: Product) -> None:
        """Send email notification to customer."""
        msg = MIMEMultipart()
        msg['From'] = self.smtp_config['from_email']
        msg['To'] = customer.email
        msg['Subject'] = f"{product.name} is back in stock!"
        
        body = f"""
        Dear {customer.name},
        
        We're excited to let you know that {product.name} is now back in stock!
        
        You joined our waitlist on {customer.join_date.strftime('%Y-%m-%d')}.
        
        Visit our website to complete your purchase before it sells out again.
        
        Best regards,
        The BioLongevity Labs Team
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(
            host=self.smtp_config['host'],
            port=self.smtp_config['port']
        ) as server:
            server.starttls()
            server.login(
                self.smtp_config['username'],
                self.smtp_config['password']
            )
            server.send_message(msg)
            
    def get_waitlist_size(self, product_id: str) -> int:
        """Get the number of customers on the waitlist for a product."""
        return len(self.waitlist.get(product_id, []))
        
    def get_customer_position(self, email: str, product_id: str) -> Optional[int]:
        """
        Get a customer's position in the waitlist.
        
        Returns:
            Position (1-based index) or None if not found
        """
        if product_id not in self.waitlist:
            return None
            
        for i, customer in enumerate(self.waitlist[product_id], 1):
            if customer.email == email:
                return i
                
        return None

# Example usage
if __name__ == "__main__":
    # SMTP configuration (should be loaded from environment/config in production)
    smtp_config = {
        'host': 'smtp.example.com',
        'port': 587,
        'username': 'your_username',
        'password': 'your_password',
        'from_email': 'notifications@biolongevitylabs.com'
    }
    
    # Initialize waitlist manager
    manager = WaitlistManager(smtp_config)
    
    # Add some products
    product1 = Product(
        product_id="prod123",
        name="Longevity Serum",
        in_stock=False,
        restock_date=datetime(2023, 12, 1)
    )
    product2 = Product(
        product_id="prod456",
        name="Anti-Aging Cream",
        in_stock=False
    )
    
    manager.add_product(product1)
    manager.add_product(product2)
    
    # Add customers to waitlist
    try:
        manager.add_to_waitlist("customer1@example.com", "John Doe", "prod123")
        manager.add_to_waitlist("customer2@example.com", "Jane Smith", "prod123")
        manager.add_to_waitlist("customer3@example.com", "Bob Johnson", "prod456")
    except ValueError as e:
        logger.error(str(e))
    
    # Simulate product coming back in stock
    manager.products["prod123"].in_stock = True
    
    # Check inventory and notify customers
    manager.check_inventory_and_notify()
    
    # Check waitlist status
    print(f"Waitlist size for prod123: {manager.get_waitlist_size('prod123')}")
    print(f"Customer position: {manager.get_customer_position('customer3@example.com', 'prod456')}")
```
