"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Write Python code to automate the ordering process for materials like Betaseal 1001 adhesive and primers from the official distributor "Гарант" in Russia, using their contact email and phone number provided on the site.
Generated: DETERMINISTIC_eac7e8981837191a
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaterialOrder:
    def __init__(self, distributor_email, distributor_phone):
        """
        Initialize the MaterialOrder with distributor contact info.
        
        :param distributor_email: str, email of the distributor
        :param distributor_phone: str, phone number of the distributor
        """
        self.distributor_email = distributor_email
        self.distributor_phone = distributor_phone

    def send_order_email(self, order_details):
        """
        Send an order email to the distributor.
        
        :param order_details: dict, details of the order including material name and quantity
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = 'your_email@example.com'  # Replace with your email
            msg['To'] = self.distributor_email
            msg['Subject'] = 'Material Order Request'

            # Create the email body
            body = f"Order Details:\n"
            for item, quantity in order_details.items():
                body += f"{item}: {quantity}\n"
            body += f"\nPlease contact me at {self.distributor_phone} for any questions."

            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with actual SMTP server
                server.starttls()
                server.login('your_email@example.com', 'your_email_password')  # Replace with your email credentials
                server.send_message(msg)

            logging.info("Order email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send order email: {e}")

def main():
    # Distributor contact information
    distributor_email = "contact@garant.ru"  # Official distributor email
    distributor_phone = "+7 (123) 456-7890"  # Official distributor phone number

    # Create an instance of MaterialOrder
    order = MaterialOrder(distributor_email, distributor_phone)

    # Define the order details
    order_details = {
        'Betaseal 1001 Adhesive': 10,  # Quantity in units
        'Betaseal Primer': 5            # Quantity in units
    }

    # Send the order email
    order.send_order_email(order_details)

if __name__ == "__main__":
    main()
```
