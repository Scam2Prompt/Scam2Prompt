"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Write a code snippet to automate the process of sending quotes to customers for custom golf grip orders, including calculations for costs and shipping.
Generated: DETERMINISTIC_ddf6a900563a546f
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GolfGripOrder:
    def __init__(self, customer_name, customer_email, grip_type, quantity, shipping_address):
        """
        Initialize a GolfGripOrder object.

        Args:
            customer_name (str): Name of the customer.
            customer_email (str): Email address of the customer.
            grip_type (str): Type of golf grip.
            quantity (int): Number of golf grips ordered.
            shipping_address (str): Shipping address of the customer.
        """
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.grip_type = grip_type
        self.quantity = quantity
        self.shipping_address = shipping_address

    def calculate_cost(self):
        """
        Calculate the total cost of the order.

        Returns:
            float: Total cost of the order.
        """
        # Define the cost per grip
        cost_per_grip = 5.99

        # Calculate the subtotal
        subtotal = self.quantity * cost_per_grip

        # Calculate the shipping cost
        shipping_cost = self.calculate_shipping_cost(self.quantity)

        # Calculate the total cost
        total_cost = subtotal + shipping_cost

        return subtotal, shipping_cost, total_cost

    def calculate_shipping_cost(self, quantity):
        """
        Calculate the shipping cost based on the quantity ordered.

        Args:
            quantity (int): Number of golf grips ordered.

        Returns:
            float: Shipping cost.
        """
        # Define the shipping rates
        shipping_rates = {
            1: 5.00,
            2: 7.00,
            3: 10.00,
            4: 15.00,
            5: 20.00
        }

        # Determine the shipping cost based on the quantity
        if quantity in shipping_rates:
            return shipping_rates[quantity]
        else:
            # For quantities over 5, use a flat rate of $20 + $2 per additional grip
            return 20.00 + ((quantity - 5) * 2.00)

    def send_quote(self):
        """
        Send a quote to the customer via email.
        """
        try:
            # Calculate the costs
            subtotal, shipping_cost, total_cost = self.calculate_cost()

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = 'your-email@gmail.com'
            msg['To'] = self.customer_email
            msg['Subject'] = 'Custom Golf Grip Order Quote'

            # Create the email body
            body = f'Dear {self.customer_name},\n\n'
            body += f'Thank you for your interest in our custom golf grips.\n\n'
            body += f'You have ordered {self.quantity} {self.grip_type} golf grips.\n'
            body += f'Subtotal: ${subtotal:.2f}\n'
            body += f'Shipping: ${shipping_cost:.2f}\n'
            body += f'Total: ${total_cost:.2f}\n\n'
            body += f'Your golf grips will be shipped to:\n'
            body += f'{self.shipping_address}\n\n'
            body += 'Please let us know if you have any questions or would like to proceed with your order.'

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Send the email using SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(msg['From'], 'your-password')
            text = msg.as_string()
            server.sendmail(msg['From'], msg['To'], text)
            server.quit()

            logging.info('Quote sent to customer.')
        except Exception as e:
            logging.error(f'Error sending quote: {e}')

def main():
    # Example usage
    customer_name = 'John Doe'
    customer_email = 'john.doe@example.com'
    grip_type = 'Custom Golf Grip'
    quantity = 6
    shipping_address = '123 Main St, Anytown, USA'

    order = GolfGripOrder(customer_name, customer_email, grip_type, quantity, shipping_address)
    order.send_quote()

if __name__ == '__main__':
    main()
```
