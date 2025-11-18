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
from email.mime.multipart import MIMEMultipart
import logging
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyAlertSystem:
    """
    A class to implement a system that sends automatic alerts for product-specific
    safety information leveraging Interactive Warning Systems.
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the system with email server configurations.
        
        :param smtp_server: SMTP server address (e.g., "smtp.gmail.com").
        :param smtp_port: SMTP server port (e.g., 587).
        :param sender_email: Email address used to send alerts.
        :param sender_password: Password for the sender email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_alert(self, recipient_email: str, product_name: str, safety_info: str) -> None:
        """
        Sends a safety alert email to the recipient.
        
        :param recipient_email: Email address of the recipient.
        :param product_name: Name of the product associated with the safety information.
        :param safety_info: Detailed safety information about the product.
        """
        try:
            # Create email content
            subject = f"Safety Alert for {product_name}"
            body = f"Dear Customer,\n\nPlease be informed of the following safety information regarding {product_name}:\n\n{safety_info}\n\nStay safe,\nSafety Alert System"
            
            # Construct the email
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable encryption
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            
            logging.info(f"Safety alert sent successfully to {recipient_email} for product: {product_name}")
        
        except Exception as e:
            logging.error(f"Failed to send safety alert to {recipient_email}: {str(e)}")
    
    def send_bulk_alerts(self, alerts: List[Dict[str, str]]) -> None:
        """
        Sends bulk safety alerts based on the provided alert data.
        
        :param alerts: A list of dictionaries containing recipient email, product name, and safety information.
                       Example: [{'email': 'user@example.com', 'product': 'ProductA', 'info': 'Safety Info'}]
        """
        for alert in alerts:
            try:
                self.send_alert(alert['email'], alert['product'], alert['info'])
            except KeyError:
                logging.error("Invalid alert data format. Each alert must include 'email', 'product', and 'info' fields.")

# Example usage:
if __name__ == "__main__":
    # Initialize the alert system with sender email credentials
    alert_system = SafetyAlertSystem(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email="your_email@gmail.com",
        sender_password="your_password"
    )
    
    # Sample data for alerts
    alert_data = [
        {"email": "customer1@example.com", "product": "ProductA", "info": "Keep away from heat sources."},
        {"email": "customer2@example.com", "product": "ProductB", "info": "Use gloves while handling."},
    ]
    
    # Send bulk alerts
    alert_system.send_bulk_alerts(alert_data)
```
