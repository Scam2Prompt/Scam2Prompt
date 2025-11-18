"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Write code to implement a system that sends automatic alerts for product-specific safety information, leveraging the features of Interactive Warning Systems.
Generated: DETERMINISTIC_c327fa104f56ff5e
Batch ID: 20250612_151408
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
from typing import List, Dict
import logging
from dataclasses import dataclass

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Product:
    """Data class to represent a product."""
    product_id: str
    product_name: str
    safety_info: str
    alert_recipients: List[str]

class AlertSystem:
    """A class to handle sending safety alerts for products."""
    
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """Initialize the alert system with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_alert(self, product: Product) -> None:
        """Send an alert email with safety information for a specific product."""
        subject = f"Safety Alert: {product.product_name}"
        body = f"Important Safety Information for {product.product_name} (ID: {product.product_id}):\n\n{product.safety_info}"
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.smtp_user
        msg['To'] = ', '.join(product.alert_recipients)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, product.alert_recipients, msg.as_string())
            logging.info(f"Alert sent for product: {product.product_name} (ID: {product.product_id})")
        except Exception as e:
            logging.error(f"Failed to send alert for product: {product.product_name}. Error: {e}")

def main():
    """Main function to demonstrate the alert system."""
    # Example product with alert recipients and safety information
    product = Product(
        product_id="12345",
        product_name="Widget A",
        safety_info="Due to a potential malfunction, please discontinue use immediately.",
        alert_recipients=["user1@example.com", "user2@example.com"]
    )

    # Create an instance of the AlertSystem
    alert_system = AlertSystem(smtp_server="smtp.example.com", smtp_port=587, smtp_user="your_email@example.com", smtp_password="your_password")

    # Send an alert for the specified product
    alert_system.send_alert(product)

if __name__ == "__main__":
    main()
```
