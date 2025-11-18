"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Write a code snippet to automate WhatsApp-based sales for a hardware store, inspired by the "Manual de Ventas por Whatsapp para el negocio Ferretero" from Aula Ferretera.
Generated: DETERMINISTIC_300c69a1a258491b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import logging
from datetime import datetime
from twilio.rest import Client

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WhatsAppSalesAutomation:
    def __init__(self, account_sid, auth_token, from_whatsapp_number):
        """
        Initialize the WhatsAppSalesAutomation class with Twilio credentials.

        :param account_sid: Twilio Account SID
        :param auth_token: Twilio Auth Token
        :param from_whatsapp_number: WhatsApp number linked to Twilio account
        """
        self.client = Client(account_sid, auth_token)
        self.from_whatsapp_number = from_whatsapp_number

    def send_message(self, to_whatsapp_number, message):
        """
        Send a WhatsApp message.

        :param to_whatsapp_number: Recipient's WhatsApp number
        :param message: Message to be sent
        :return: None
        """
        try:
            self.client.messages.create(
                body=message,
                from_=f'whatsapp:{self.from_whatsapp_number}',
                to=f'whatsapp:{to_whatsapp_number}'
            )
            logging.info(f'Message sent to {to_whatsapp_number}: {message}')
        except Exception as e:
            logging.error(f'Failed to send message to {to_whatsapp_number}: {e}')
            sys.exit(1)

    def generate_sales_message(self, product_name, price, stock):
        """
        Generate a sales message for a specific product.

        :param product_name: Name of the product
        :param price: Price of the product
        :param stock: Stock availability of the product
        :return: Formatted sales message
        """
        return f"🌟 ¡Oferta especial! 🌟\n" \
               f"Producto: {product_name}\n" \
               f"Precio: ${price:.2f}\n" \
               f"Disponibilidad: {stock} en stock.\n" \
               f"¡Contáctanos para realizar tu pedido! 📞"

    def create_order(self, customer_name, customer_number, product_name, price, stock):
        """
        Create an order and send confirmation message via WhatsApp.

        :param customer_name: Name of the customer
        :param customer_number: Customer's WhatsApp number
        :param product_name: Name of the product being ordered
        :param price: Price of the product
        :param stock: Stock availability of the product
        :return: None
        """
        logging.info(f'Creating order for {customer_name}...')
        if stock <= 0:
            logging.warning(f'Insufficient stock for {product_name}. Cannot complete the order.')
            self.send_message(customer_number, f"Lo siento, {customer_name}. No hay suficiente stock para {product_name}.")
            return
        
        message = self.generate_sales_message(product_name, price, stock)
        self.send_message(customer_number, message)

        # Update stock availability here (in a real application, this would interact with a database)
        # stock -= 1

        logging.info(f'Order created successfully for {customer_name}.')

if __name__ == '__main__':
    # Replace with your actual Twilio credentials
    ACCOUNT_SID = 'your_account_sid'
    AUTH_TOKEN = 'your_auth_token'
    FROM_WHATSAPP_NUMBER = 'your_twilio_whatsapp_number'

    # Initialize the WhatsApp sales automation
    sales_automation = WhatsAppSalesAutomation(ACCOUNT_SID, AUTH_TOKEN, FROM_WHATSAPP_NUMBER)

    # Example usage
    customer_name = 'Juan Perez'
    customer_number = '123456789'  # Customer's WhatsApp number
    product_name = 'Taladro Percutor'
    price = 150.00
    stock = 5

    # Create an order
    sales_automation.create_order(customer_name, customer_number, product_name, price, stock)
```
